import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
import constants as c

class WordTestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        grid = QGridLayout()

        grid.addWidget(self.createCurrentPracticeBox(), 0, 0)
        grid.addWidget(self.createTypingBox(), 0, 1)
        grid.addWidget(self.createProgressBox(), 2, 0)
        grid.addWidget(self.createInfoBox(), 2, 1)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 3)

        upper_spacer = QSpacerItem(20, 160)
        lower_spacer = QSpacerItem(20, 160)

        main_layout.addItem(upper_spacer)
        main_layout.addLayout(grid)
        main_layout.addItem(lower_spacer)

        self.setLayout(main_layout)
        self.setStyleSheet('background-color:#b67e36')
        self.setWindowTitle('낱말 연습')
        self.move(0, 0)
        self.setFixedSize(c.MAIN_WIDTH, c.MAIN_HEIGHT)
        self.show()

    def createCurrentPracticeBox(self):
        groupbox = QGroupBox()

        label = QLabel("현재 연습 단계")
        label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(label)

        groupbox.setLayout(vbox)
        groupbox.setStyleSheet("color: black;font-size: 17px;text-align:center;")

        return groupbox

    def createProgressBox(self):
        groupbox = QGroupBox()

        label = QLabel(" 진행 상황 : 7 / 8 ")
        label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(label)

        hbox = QHBoxLayout()
        for _ in range(7):
            rectangle_widget = RectangleWidget()
            hbox.addWidget(rectangle_widget)

        vbox.addLayout(hbox)
        groupbox.setLayout(vbox)
        groupbox.setStyleSheet("color: black;font-size: 17px;text-align:center;")

        return groupbox

    def createTypingBox(self):
        groupbox = QGroupBox()

        label = QLabel("낱말")
        label.setAlignment(Qt.AlignCenter)

        te = QTextEdit()
        te.setAcceptRichText(False)
        te.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(te)

        groupbox.setLayout(vbox)
        groupbox.setStyleSheet("background-color: white;color: black;font-size: 25px;")

        return groupbox

    def createInfoBox(self):
        groupbox = QGroupBox()

        label1 = QLabel("진행도 : 0%")
        label2 = QLabel("오타수 : 0")
        label3 = QLabel("정확도 : 0%")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)


        groupbox.setLayout(vbox)
        groupbox.setStyleSheet("background-color: green;")

        return groupbox

class RectangleWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        rect_x = 0
        rect_y = 0
        rect_width = 10
        rect_height = 40
        painter.drawRect(rect_x, rect_y, rect_width, rect_height)