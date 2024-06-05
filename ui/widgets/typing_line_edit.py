from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt


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

    def setTargetText(self, text):
        self.target_text = text
