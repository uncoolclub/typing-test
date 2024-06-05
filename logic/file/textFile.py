import os

class TextFile():
    def __init__(self, file_name, base_path=None):
        if base_path is None:
            # 현재 파일의 부모 디렉토리로부터 기본 경로 설정
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../resource/text'))
        self.file_path = ""
        self.file_name = file_name
        self.readText(file_name, base_path)

    def readText(self, file_name, base_path, _encoding="UTF-8"):
        self.file_name = file_name.split(".")[0]
        self.file_path = os.path.join(base_path, file_name)

        self.text_list = []
        with open(self.file_path, 'r', encoding=_encoding) as f:
            for line in f:
                line = line.strip()  # 좌우 공백 제거
                line = line.replace('\n', '')  # 개행 문자 제거
                if line:  # 빈 줄이 아닌 경우에만 리스트에 추가
                    self.text_list.append(line)

    def getText(self):
        return self.text_list
