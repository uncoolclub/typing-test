import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class WordTestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('낱말 연습')
        self.move(0, 0)
        self.setFixedSize(1024, 768)
        self.show()


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def showWordTestWindow(self):
        self.hide()  # 현재 창 숨기기
        self.wordTestWin = WordTestWindow()  # 낱말 연습 창 인스턴스 생성 및 보여주기

    def initUI(self):
        wordTestButton = QPushButton('낱말 연습')
        shortTestButton = QPushButton('짧은 글 연습')
        longTestButton = QPushButton('긴글 연습')
        rankButton = QPushButton('랭킹')

        wordTestButton.clicked.connect(self.showWordTestWindow)  # 버튼 클릭 시 showWordTestWindow 메소드 연결

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addWidget(wordTestButton)
        vbox.addWidget(shortTestButton)
        vbox.addWidget(longTestButton)
        vbox.addWidget(rankButton)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('타자 연습')
        self.move(0, 0)
        self.setFixedSize(1024, 768)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
