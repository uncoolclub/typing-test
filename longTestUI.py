import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QFrame
from PyQt5.QtCore import Qt

class LongTextPractice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('한컴타자연습 - 긴글연습')
        self.setFixedSize(1024, 768)  # 창 크기 고정

        self.texts = [
            "동해물과 백두산이 마르고 닳도록",
            "하느님이 보우하사 우리나라 만세",
            "무궁화 삼천리 화려 강산",
            "대한 사람, 대한으로 길이 보전하세",
            "남산 위에 저 소나무 철갑을 두른 듯",
            "바람 서리 불변함은 우리 기상일세",
            "무궁화 삼천리 화려 강산",
            "대한 사람, 대한으로 길이 보전하세",
            "가을 하늘 공활한데 높고 구름 없이",
            "밝은 달은 우리 가슴 일편단심일세",
            "무궁화 삼천리 화려 강산",
            "대한 사람, 대한으로 길이 보전하세",
            "이 기상과 이 맘으로 충성을 다하여",
            "괴로우나 즐거우나 나라 사랑하세",
            "무궁화 삼천리 화려 강산",
            "대한 사람, 대한으로 길이 보전하세"
        ]


        self.current_text = self.texts[:9]
        main_layout = QVBoxLayout()

        # Add frame for stats display
        stats_frame = QFrame(self)
        stats_frame.setStyleSheet("border: 1px solid black;")
        stats_layout = QVBoxLayout(stats_frame)

        self.speed_label = QLabel("타자 속도: 0 타/분", self)
        stats_layout.addWidget(self.speed_label)

        self.accuracy_label = QLabel("정확도: 0%", self)
        stats_layout.addWidget(self.accuracy_label)

        self.max_speed_label = QLabel("최고 타자 속도: 0 타/분", self)
        stats_layout.addWidget(self.max_speed_label)

        main_layout.addWidget(stats_frame)

        # Add frame for text display and input field
        text_frame = QFrame(self)
        text_frame.setFrameShape(QFrame.Box)  # Set frame shape to Box for a border
        text_layout = QVBoxLayout(text_frame)

        layout = QVBoxLayout()
        self.text_labels = []
        self.input_fields = []

        for line in self.current_text:
            textLabel = QLabel(line, self)
            textLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            textLabel.setStyleSheet("font-size: 14px;")
            self.text_labels.append(textLabel)
            layout.addWidget(textLabel)
            layout.addSpacing(5)

            inputText = QLineEdit(self)
            inputText.setStyleSheet("font-size: 14px;")
            inputText.setFixedHeight(25)
            self.input_fields.append(inputText)
            layout.addWidget(inputText)

        text_layout.addLayout(layout)
        text_frame.setLayout(text_layout)
        main_layout.addWidget(text_frame)

        # Add stretch to fill remaining space
        main_layout.addStretch(1)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LongTextPractice()
    ex.show()
    sys.exit(app.exec_())
