import time
from utils.broken_hangul import break_hangul


class MeasureManager:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None
        self.sentence = ""
        self.total_len = 0
        self.input_field_text = ""
        self.before_text = ""
        self.num_chars = 0
        self.max_cpm = 0
        self.current_cpm = 0
        self.mismatched_characters = 0
        self.total_mismatched_characters = 0
        self.total_characters = 0
        self.all_total_characters = 0
        self.correct_characters = 0
        self.total_correct_characters = 0
        self.next = False;
        self.overall_accuracy = 100

    def startTest(self, sentence):
        self.start_time = time.time()
        self.sentence = sentence

    def nextTest(self, sentence):
        self.total_mismatched_characters += self.mismatched_characters
        self.all_total_characters += self.total_characters
        self.total_len += len(self.input_field_text)
        self.sentence = sentence

    def resetTest(self):
        self.total_len = 0
        self.sentence = ""
        self.start_time = None

    def onTextChanged(self, input_text):
        self.input_field_text = input_text

        if self.start_time is None:
            self.start_time = time.time()

    def updateSpeed(self):
        if self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time

            # if self.elapsed_time > 1:
            correct_characters = self.total_len
            for index, i in enumerate(self.input_field_text):
                if index >= len(self.sentence):
                    return self.current_cpm, self.max_cpm

                if self.sentence[index] == i:
                    correct_characters += 1
            self.num_chars = len(self.input_field_text) + self.total_len
            self.correct_characters = correct_characters
            self.current_cpm = int((correct_characters / self.elapsed_time) * 60)

            if self.current_cpm < 1000:
                if self.max_cpm < self.current_cpm:
                    self.max_cpm = self.current_cpm

            return self.current_cpm, self.max_cpm

        return self.current_cpm, self.max_cpm

    def calculate_overall_accuracy(self, input_fields, texts):
        for input_field, base_text in zip(input_fields, texts):
            typed_text = input_field.get()
            separated_typed_text = break_hangul(typed_text)
            separated_correct_text = break_hangul(base_text)

            self.mismatched_characters = sum(
                1 for typed_char, correct_char in zip(separated_typed_text, separated_correct_text) if
                typed_char != correct_char)

            self.total_characters = len(separated_correct_text)
        if self.total_characters > 0:
            total = self.all_total_characters + self.total_characters
            mis = self.mismatched_characters + self.total_mismatched_characters
            overall_accuracy = int(((total - mis) / total) * 100)
        else:
            overall_accuracy = 100

        self.overall_accuracy = overall_accuracy
