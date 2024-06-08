import time
from utils.broken_hangul import break_hangul


class MeasureManager:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None
        self.is_finished = False
        self.sentence = ""
        self.total_len = 0
        self.input_field_text = ""
        self.max_cpm = 0
        self.current_cpm = 0

    def startTest(self, sentence):
        self.start_time = time.time()
        self.sentence = sentence
        self.is_finished = False

    def nextTest(self, sentence):
        self.sentence = sentence
        self.is_finished = False

    def resetTest(self):
        self.start_time = None
        self.is_finished = False

    def onTextChanged(self, input_text):
        self.input_field_text = input_text
        if self.start_time is None:
            self.start_time = time.time()

        if self.input_field_text == self.sentence and not self.is_finished:
            self.total_len += len(self.input_field_text)
            # self.is_finished = True
            # self.start_time = None

    def updateSpeed(self):
        if self.start_time is not None and not self.is_finished:
            self.elapsed_time = int(time.time() - self.start_time)

            # if self.elapsed_time > 1:
            num_chars = self.total_len + len(self.input_field_text)
            self.current_cpm = (num_chars / self.elapsed_time) * 60

            if self.current_cpm < 1000:
                if self.max_cpm < self.current_cpm:
                    self.max_cpm = self.current_cpm

            return self.current_cpm, self.max_cpm

        return self.current_cpm, self.max_cpm

    @staticmethod
    def calculate_overall_accuracy(input_fields, texts):
        print(texts)
        total_mismatched_characters = 0
        total_characters = 0

        for input_field, base_text in zip(input_fields, texts):
            typed_text = input_field.get()
            print(typed_text)
            separated_typed_text = break_hangul(typed_text)
            separated_correct_text = break_hangul(base_text)

            mismatched_characters = sum(
                1 for typed_char, correct_char in zip(separated_typed_text, separated_correct_text) if
                typed_char != correct_char)

            total_mismatched_characters += mismatched_characters
            total_characters += len(separated_correct_text)

        if total_characters > 0:
            overall_accuracy = int(((total_characters - total_mismatched_characters) / total_characters) * 100)
        else:
            overall_accuracy = 100

        return overall_accuracy
