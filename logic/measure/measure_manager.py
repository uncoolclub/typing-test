# measure_manager.py
import time
from utils.broken_hangul import break_hangul


class MeasureManager:
    def __init__(self):
        self.start_time = None
        self.is_finished = False
        self.sentence = ""
        self.input_field_text = ""
        self.max_cpm = 0

    def startTest(self, sentence):
        self.start_time = time.time()
        self.sentence = sentence
        self.is_finished = False

    def onTextChanged(self, input_text):
        self.input_field_text = input_text
        if self.start_time is None:
            self.start_time = time.time()

        if self.input_field_text == "":
            self.resetTest()

        if self.input_field_text == self.sentence and not self.is_finished:
            self.is_finished = True
            self.start_time = None

    def updateSpeed(self):
        if self.start_time is not None and not self.is_finished:
            elapsed_time = time.time() - self.start_time

            if elapsed_time > 1:
                num_chars = len(self.input_field_text)
                cpm = (num_chars / elapsed_time) * 60

                if cpm < 1000:
                    if self.max_cpm < cpm:
                        self.max_cpm = cpm

                return cpm, self.max_cpm

        return 0, self.max_cpm

    def resetTest(self):
        self.start_time = None
        self.is_finished = False

    @staticmethod
    def calculate_overall_accuracy(input_fields, texts):
        total_mismatched_characters = 0
        total_characters = 0

        for input_field, base_text in zip(input_fields, texts):
            typed_text = input_field.text()
            separated_typed_text = break_hangul(typed_text)
            separated_correct_text = break_hangul(base_text)

            # 비교하여 불일치하는 글자 수를 계산
            mismatched_characters = sum(
                1 for typed_char, correct_char in zip(separated_typed_text, separated_correct_text) if
                typed_char != correct_char)

            total_mismatched_characters += mismatched_characters
            total_characters += len(separated_correct_text)

        # 전체 문자의 수를 기준으로 정확도 계산
        if total_characters > 0:
            overall_accuracy = ((total_characters - total_mismatched_characters) / total_characters) * 100
        else:
            # 입력 필드가 비어있다면 정확도는 100%로 가정
            overall_accuracy = 100

        return overall_accuracy
