import time
from utils.broken_hangul import break_hangul


class MeasureManager:
    def __init__(self):
        self.start_time = None
        self.next_time = None
        self.end_time = None
        self.max_typing_speed = 0
        self.results = list()

    def startTest(self):
        self.start_time = time.time()
        self.next_time = self.start_time

    def endTest(self):
        self.end_time = time.time()

    def resetTest(self):
        self.start_time = None
        self.next_time = None
        self.results = list()
        self.max_typing_speed = 0

    def append_result(self, accuracy, matches, mismatches, typing_speed):
        self.next_time = time.time()
        self.results.append({"accuracy": accuracy, "matches": matches, "mismatches": mismatches, "typing_speed": typing_speed})

    def get_result(self):
        total_accuracy = 0
        total_matches = 0
        total_mismatches = 0
        total_typing_speed = 0
        count = len(self.results)

        for result in self.results:
            total_accuracy += result["accuracy"]
            total_matches += result["matches"]
            total_mismatches += result["mismatches"]
            total_typing_speed += result["typing_speed"]


        # 평균타수 최고타수 날짜 정확도
        average_accuracy = total_accuracy / count
        average_typing_speed = total_typing_speed / count

        return {
            "total_matches" : total_matches,
            "total_mismatches" : total_mismatches,
            "average_accuracy" : average_accuracy,
            "average_typing_speed": average_typing_speed,
            "max_typing_speed" : self.max_typing_speed,
            "running_time" : self.end_time - self.start_time
        }


    def levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def calculate(self, original, comparison):
        if self.next_time == None or len(original) < len(comparison):
            return None, None, None, None

        time_taken = time.time() - self.next_time
        self.elapsed_time = time_taken
        distance = self.levenshtein_distance(original, comparison)
        max_length = max(len(original), len(comparison))
        if max_length == 0:
            return 100.00, 0, 0, 0.0

        # 맞은 문자와 틀린 문자 계산
        matches = sum(1 for o, c in zip(original, comparison) if o == c)
        mismatches = max_length - matches

        accuracy = (1 - distance / max_length) * 100
        accuracy = round(accuracy, 2)  # 정확도를 소수점 두 자리로 반올림

        # 타자 속도 계산 (초당 입력된 문자 수, KPM 방식)
        typing_speed = matches / time_taken * 60 if time_taken > 0 else 0
        if typing_speed > self.max_typing_speed:
            self.max_typing_speed = typing_speed

        print(self.results)
        return accuracy, matches, mismatches, typing_speed


