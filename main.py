
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.nicknameDialogBox import NicknameDialog
from ui.index import Index
from lib.User import User


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        nickname, ok = NicknameDialog.getNickname(self)
        if ok and nickname:
            self.user = User(nickname)
            print(f'Nickname entered: {nickname}')
            self.setFixedSize(1024, 768)
            self.index = Index(self)
        else:
            print('No nickname entered')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())