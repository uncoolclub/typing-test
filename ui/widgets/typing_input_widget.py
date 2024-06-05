from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from typing_line_edit import TypingLineEdit


class TypingInputWidget(QWidget):
    def __init__(self, text, start_test_callback, reset_test_callback, move_to_next_callback):
        super().__init__()
        self.text = text
        self.start_test_callback = start_test_callback
        self.reset_test_callback = reset_test_callback
        self.move_to_next_callback = move_to_next_callback
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.text_label = QLabel(self.text, self)
        self.text_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(self.text_label)

        self.input_field = TypingLineEdit(self.text, self.start_test_callback, self.reset_test_callback, self)
        layout.addWidget(self.input_field)

        self.setLayout(layout)

    def getInputField(self):
        return self.input_field

    def setText(self, text):
        self.text = text
        self.text_label.setText(text)
        self.input_field.setTargetText(text)
