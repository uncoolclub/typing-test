from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QFrame, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from logic.measure.measure_manager import MeasureManager
from logic.file.textFile import TextFile
from ui.widgets.typing_line_edit import TypingLineEdit


class LongTextPractice(QMainWindow):
    def __init__(self, file_name='default1.txt'):
        super().__init__()
        self.textFile = TextFile(file_name)
        self.MeasureManager = MeasureManager()
        self.current_typing_text_list = []
        self.current_sentence_index = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('한컴타자연습 - 긴글연습')
        self.setFixedSize(1024, 768)

        self.texts = self.textFile.getText()[:9]

        main_layout = QVBoxLayout()
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
        text_frame = QFrame(self)
        text_frame.setFrameShape(QFrame.Box)
        text_layout = QVBoxLayout(text_frame)

        layout = QVBoxLayout()
        self.text_labels = []
        self.input_fields = []

        for line in self.texts:
            textLabel = QLabel(line, self)
            textLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            textLabel.setStyleSheet("font-size: 14px;")
            self.text_labels.append(textLabel)
            layout.addWidget(textLabel)
            layout.addSpacing(5)

            input_field = TypingLineEdit(line, self.MeasureManager, self)
            input_field.setStyleSheet("font-size: 14px;")
            input_field.setFixedHeight(25)
            self.input_fields.append(input_field)
            layout.addWidget(input_field)
            input_field.textChanged.connect(lambda text, t=line: self.onTextChanged(text))

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
        self.show()

    def onTextChanged(self, text):
        active_field = QApplication.focusWidget()
        if isinstance(active_field, QLineEdit):
            self.MeasureManager.onTextChanged(active_field.text())
        self.check_accuracy_and_move_to_next_line(text)

    def updateSpeed(self):
        cpm, max_cpm = self.MeasureManager.updateSpeed()
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

    def check_accuracy_and_move_to_next_line(self, text):
        accuracy = self.MeasureManager.calculate_overall_accuracy(self.input_fields, self.texts)
        self.accuracy_label.setText(f"정확도: {accuracy:.2f}%")

        self.move_to_next_line(text)
        self.disable_all_input_fields_except_current()
