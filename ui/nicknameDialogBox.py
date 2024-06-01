import sys
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QLabel, QLineEdit, QPushButton, QHBoxLayout


class NicknameDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Enter Nickname')

        label = QLabel('Enter your nickname:', self)

        self.line_edit = QLineEdit(self)

        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.on_ok)

        cancel_button = QPushButton('Cancel', self)
        cancel_button.clicked.connect(self.on_cancel)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.line_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def on_ok(self):
        self.nickname = self.line_edit.text()
        self.accept()

    def on_cancel(self):
        self.nickname = None
        self.reject()
        self.close()

    @staticmethod
    def getNickname(parent=None):
        dialog = NicknameDialog()
        result = dialog.exec_()
        nickname = dialog.nickname
        return nickname, result == QDialog.Accepted