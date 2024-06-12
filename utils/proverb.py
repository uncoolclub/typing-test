import random
import os

class Proverb:
    def __init__(self, filename="data.txt", base_path=None):
        if base_path is None:
            # 현재 파일의 부모 디렉토리로부터 기본 경로 설정
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resource/text'))
        self.initProverb(filename, base_path)

    def initProverb(self, _filename, _base_path):
        self.out_index_list = []
        self.proverb_index_list = []
        # file_name = _filename.split(".")[0]
        file_path = os.path.join(_base_path, _filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        self.proverb_list = [line.strip() for line in lines if line.strip()]
        # `proverb_index_list`를 속담 리스트의 크기로 초기화
        self.proverb_index_list = list(range(len(self.proverb_list)))

    def getRandomProverb(self, num_lines=10):
        if num_lines > len(self.proverb_index_list):
            raise ValueError(f"Cannot select {num_lines} lines from a list of {len(self.proverb_index_list)} elements")

        # 랜덤으로 num_lines 개의 인덱스 선택
        random_indices = random.sample(self.proverb_index_list, num_lines)
        
        # 선택된 인덱스를 out_index_list에 추가하고 proverb_index_list에서 제거
        self.out_index_list += random_indices
        self.proverb_index_list = [index for index in self.proverb_index_list if index not in random_indices]

        # 선택된 인덱스에 해당하는 속담들 반환
        random_proverbs = [self.proverb_list[index] for index in random_indices]

        return random_proverbs
