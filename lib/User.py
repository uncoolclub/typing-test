import ManagerJSON as MJ
import os

class User:
    # num_characters_typed = 100  # 쓰인 글자 수
    # num_characters_correct = 90  # 맞은 글자 수
    # practice_time_minutes = 30  # 연습 시간 (분)
    # accuracy_percentage = 90.0  # 정확도 (%)
    # max_keystrokes = 120  # 최대 타수
    # avg_keystrokes = 80  # 평균 타수

    def __init__(self, username):
        file_path = f"./User/{username}/.json"
        self.userMJ = MJ.ManagerJSON(file_path)
        self.data = self.userMJ.data
        
    def appendRecord(self, info):
        self.data.append(info)
        self.userMJ.saveJSON(self.data)

    def getTextInfo(self, text_name):
        self.userJSON.data

    def filterText(self, text_name):
        filterData = []
        for record in self.data:
            if record["글"] == text_name:
                filterData.append(record)

        return filterData
    
    