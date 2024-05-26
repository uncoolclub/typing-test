import sys
import time

class TypingSpeedTest():
    def __init__(self):
        # 시작시간
        self.start_time = None
        # 종료 여부
        self.is_finished = False
        # 비교해야할 원본 문자열
        self.sentence = ""
        # 입력 받은 텍스트
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


if __name__ == '__main__':
    TypingSpeedTest()
