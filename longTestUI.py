import sys
import measure

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QFrame, QMainWindow
from PyQt5.QtCore import Qt, QTimer

CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ',
       'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ',
        'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONG = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ',
        'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ',
        'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def break_hangul(string):
    break_words = []

    for k in string:
        if ord("가") <= ord(k) <= ord("힣"):
            index = ord(k) - ord("가")
            c_cho = int((index / 28) / 21)
            c_jung = int((index / 28) % 21)
            c_jong = int(index % 28)

            break_words.append(CHO[c_cho])
            break_words.append(JUNG[c_jung])

            if c_jong > 0:
                break_words.append(JONG[c_jong])
        else:
            break_words.append(k)
    return break_words


class LongTextPractice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_typing_text_list = []
        self.current_sentence_index = 0
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

    def onTextChanged(self, text, base_text):
        print("current_text", text, base_text)

        active_field = QApplication.focusWidget()
        if isinstance(active_field, QLineEdit):
            self.SpeedTest.onTextChanged(active_field.text())
        self.check_accuracy_and_move_to_next_line(text, base_text)

    def updateSpeed(self):
        cpm, max_cpm = self.SpeedTest.updateSpeed()
        self.speed_label.setText(f"타자 속도: {cpm:.0f} 타/분")
        self.max_speed_label.setText(f"최고 타자 속도: {max_cpm:.0f} 타/분")

    def disable_all_input_fields_except_current(self):
        for index, input_field in enumerate(self.input_fields):
            if index != self.current_sentence_index:
                input_field.setDisabled(True)
            else:
                input_field.setEnabled(True)

    def can_move_to_next_line(self, text):
        typing_text_length = len(text.rstrip())
        current_sentence_length = len(self.texts[self.current_sentence_index])

        return typing_text_length >= current_sentence_length

    def move_to_next_line(self, text):
        if self.can_move_to_next_line(text):
            self.current_sentence_index += 1

            if self.current_sentence_index < len(self.input_fields):
                next_input_field = self.input_fields[self.current_sentence_index]
                next_input_field.setFocus()

    def check_accuracy_and_move_to_next_line(self, text, base_text):
        self.calculate_overall_accuracy()
        self.move_to_next_line(text)
        self.disable_all_input_fields_except_current()

    def calculate_overall_accuracy(self):
        total_mismatched_characters = 0
        total_characters = 0

        # 모든 입력 필드와 해당 기준 텍스트를 비교
        for input_field, base_text in zip(self.input_fields, self.texts):
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

        self.accuracy_label.setText(f"정확도: {overall_accuracy:.2f}%")

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
