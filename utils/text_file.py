import os

DEFAULT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resource/text'))

class TextFile:
    def __init__(self, file_name, base_path=None):
        if base_path is None:
            # 현재 파일의 부모 디렉토리로부터 기본 경로 설정
            base_path = DEFAULT_PATH
        self.file_path = ""
        self.file_name = file_name
        self.read_text(file_name, base_path)

    def read_text(self, file_name, base_path, _encoding="UTF-8"):
        self.file_name = file_name.split(".")[0]
        self.file_path = os.path.join(base_path, file_name)

        self.text_list = []
        with open(self.file_path, 'r', encoding=_encoding) as f:
            for line in f:
                line = line.strip()  # 좌우 공백 제거
                line = line.replace('\n', '')  # 개행 문자 제거
                if line:  # 빈 줄이 아닌 경우에만 리스트에 추가
                    self.text_list.append(line)

    def get_text(self):
        return self.text_list

    def save_text_file(self, content):
        with open(DEFAULT_PATH+"/"+self.file_name+".txt", 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)

    @staticmethod
    def get_text_file_list():
        txt_files = []
        for filename in os.listdir(DEFAULT_PATH):
            if filename.endswith('.txt'):
                file_base_name, file_extension = os.path.splitext(filename)
                txt_files.append({"label": file_base_name, "file_name": filename})
        return txt_files
