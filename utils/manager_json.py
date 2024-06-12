import json
import os
from datetime import datetime


def set_file_path(nickname): # default 파일 경로
    return f"../User/personal/{nickname}.json"

def create_file(nickname): # 파일 생성
    file_path = set_file_path(nickname)
    if not os.path.exists(file_path): # 경로에 있는지 없는지 체크
        with open(file_path, 'w', encoding="UTF-8") as file:
            json.dump({}, file, indent=4)

def read_json(nickname): # 파일 읽어오기
    file_path = set_file_path(nickname)
    with open(file_path, 'r', encoding="UTF-8") as file:
        return json.load(file)

def save_json(nickname, text_name, info): # 파일에 값 저장
    now = datetime.now() # 현재 시간
    file_path = set_file_path(nickname)
    data = read_json(nickname)
    check_flag = True # 이미 저장된 글 데이터가 있는지 확인할 flag

    result = {
        '쓰인글수': info.num_chars,
        '맞은글수': info.correct_characters,
        '연습시간': info.elapsed_time,
        '정확도': info.overall_accuracy,
        '최고타수': info.max_cpm,
        '평균타수': info.max_cpm,
        '날짜': now.strftime("%Y-%m-%d %H:%M:%S")
    }
    for item in list(map(str, data.keys())):
        if item == text_name: # 이미 저장된 글 데이터가 있다면 덧붙이기
            data[item].append(result)
            check_flag = False
            break

    if check_flag:
        data[text_name] = [result]

    with open(file_path, 'w', encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)