import json
import os
from datetime import datetime


def set_file_path(nickname):
    return f"../User/personal/{nickname}.json"

def create_file(nickname):
    file_path = set_file_path(nickname)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="UTF-8") as file:
            json.dump({}, file, indent=4)

def read_json(nickname):
    file_path = set_file_path(nickname)
    with open(file_path, 'r', encoding="UTF-8") as file:
        return json.load(file)

def save_json(nickname, text_name, info):
    now = datetime.now()
    file_path = set_file_path(nickname)
    data = read_json(nickname)
    check_flag = True
    for item in list(map(str, data.keys())):
        if item == text_name:
            data[item].append({
                '쓰인글수': info.num_chars,
                '맞은글수': info.correct_characters,
                '연습시간': info.elapsed_time,
                '정확도': info.overall_accuracy,
                '최고타수': info.max_cpm,
                '평균타수': info.max_cpm,
                '날짜': now.strftime("%Y-%m-%d %H:%M:%S")
            })
            check_flag = False
            break

    if check_flag:
        data[text_name] = [info]

    with open(file_path, 'w', encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)