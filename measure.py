import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer

class TypingSpeedTest(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.max_cpm = 0

    def initUI(self):
        self.test_sentence = "빠른 갈색 여우가 게으른 개를 뛰어넘습니다."
        self.start_time = None
        self.is_finished = False

        self.label = QLabel("다음 문장을 빠르고 정확하게 입력하세요:")
        self.sentence_label = QLabel(self.test_sentence)
        self.input_field = QLineEdit()
        self.speed_label = QLabel("타이핑 속도: 0 타/분 (CPM)")
        self.max_speed_label = QLabel("최대 타이핑 속도 : 0 타/분 (CPM)")
        self.reset_button = QPushButton("다시 시작")
        self.reset_button.clicked.connect(self.resetTest)

        self.input_field.textChanged.connect(self.onTextChanged)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.sentence_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.max_speed_label)
        layout.addWidget(self.reset_button)
        self.setLayout(layout)

        self.setWindowTitle("한글 타자 속도 측정기")
        self.setGeometry(300, 300, 400, 200)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateSpeed)
        self.timer.start(100)

    def onTextChanged(self):
        if self.start_time is None:
            self.start_time = time.time()

        if self.input_field.text() == "":
            self.resetTest()
            
        if self.input_field.text() == self.test_sentence and not self.is_finished:
            self.is_finished = True
            self.timer.stop()

    def updateSpeed(self):
        if self.start_time is not None and not self.is_finished:
            elapsed_time = time.time() - self.start_time
            if elapsed_time > 1:  # 최소 1초 이상 지나야 타이핑 속도를 계산
                num_chars = len(self.input_field.text())
                cpm = (num_chars / elapsed_time) * 60
                self.speed_label.setText(f"타이핑 속도: {cpm:.0f} 타/분 (CPM)")

                if cpm < 1000:  # 비정상적으로 높은 속도를 필터링
                    if self.max_cpm < cpm:
                        self.max_cpm = cpm

                self.max_speed_label.setText(f"최대 타이핑 속도 : {self.max_cpm:.0f} 타/분 (CPM)")

    def resetTest(self):
        self.start_time = None
        self.is_finished = False
        self.input_field.clear()
        self.speed_label.setText("타이핑 속도: 0 타/분 (CPM)")
        self.max_speed_label.setText(f"최대 타이핑 속도 : {self.max_cpm:.0f} 타/분 (CPM)")
        self.timer.start(100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TypingSpeedTest()
    ex.show()
    sys.exit(app.exec_())
