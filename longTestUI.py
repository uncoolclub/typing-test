import sys
import measure
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QFrame
from PyQt5.QtCore import Qt, QTimer

class LongTextPractice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.SpeedTest = measure.TypingSpeedTest()
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

            input_field = TypingLineEdit(line, self.SpeedTest, self)
            input_field.setStyleSheet("font-size: 14px;")
            input_field.setFixedHeight(25)
            self.input_fields.append(input_field)
            layout.addWidget(input_field)
            input_field.textChanged.connect(lambda text, t=line: self.onTextChanged(text, t))

        text_layout.addLayout(layout)
        text_frame.setLayout(text_layout)
        main_layout.addWidget(text_frame)

        main_layout.addStretch(1)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateSpeed)
        self.timer.start(100)


    
    def onTextChanged(self, text, target_text):
        active_field = QApplication.focusWidget()
        if isinstance(active_field, QLineEdit):
            self.SpeedTest.onTextChanged(active_field.text())
            accuracy = self.calculateAccuracy(active_field.text(), target_text)
            self.accuracy_label.setText(f"정확도: {accuracy:.2f}%")

    def updateSpeed(self):
        cpm, max_cpm = self.SpeedTest.updateSpeed()
        self.speed_label.setText(f"타자 속도: {cpm:.0f} 타/분")
        self.max_speed_label.setText(f"최고 타자 속도: {max_cpm:.0f} 타/분")


    def calculateAccuracy(self, input_text, target_text):
        matches = sum(1 for a, b in zip(input_text, target_text) if a == b)
        accuracy = (matches / len(target_text)) * 100 if target_text else 0
        return accuracy
    
class TypingLineEdit(QLineEdit):
    def __init__(self, target_text, speed_test, parent=None):
        super().__init__(parent)
        self.target_text = target_text
        self.speed_test = speed_test
        self.parent = parent

    def focusInEvent(self, event):
        self.speed_test.startTest(self.target_text)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.speed_test.resetTest()
        super().focusOutEvent(event)

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Backspace, Qt.Key_Delete] and self.text() == "":
            self.speed_test.resetTest()
        super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LongTextPractice()
    ex.show()
    sys.exit(app.exec_())
