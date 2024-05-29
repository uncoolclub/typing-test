from PyQt5.QtWidgets import QWidget, QVBoxLayout
from typing_input_widget import TypingInputWidget


class TextDisplayWidget(QWidget):
    def __init__(self, texts, start_test_callback, reset_test_callback, move_to_next_callback):
        super().__init__()
        self.texts = texts
        self.current_sentence_index = 0
        self.start_test_callback = start_test_callback
        self.reset_test_callback = reset_test_callback
        self.move_to_next_callback = move_to_next_callback
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.typing_input_widget = TypingInputWidget(self.texts[self.current_sentence_index], self.start_test_callback,
                                                     self.reset_test_callback, self.move_to_next_callback)
        layout.addWidget(self.typing_input_widget)
        self.setLayout(layout)

    def showNextSentence(self):
        self.current_sentence_index += 1

        if self.current_sentence_index < len(self.texts):
            self.typing_input_widget.setText(self.texts[self.current_sentence_index])
