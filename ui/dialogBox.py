from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QDialog, QLabel, QWidget

class DialogBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setWindowTitle("긴글 선택")
        self.setFixedSize(320, 480)
        self.setStyleSheet("""
            QLabel {
                font-size: 22px;
                color: white;
                border: 1px solid white;
            }
            QPushButton {
                color: white;
                border: 2px solid black;
                border-radius: 10px;
                font-size: 14px;
                padding: 10px;
                min-width: 200px;
                max-height: 30px;
            }
        """)

        # 레이블 추가
        label = QLabel('긴 글 선 택', self)
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(50)

        button_container = QWidget()
        button_layout = QVBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(0)
        button_container.setFixedHeight(200)

        # 버튼 생성
        button1 = QPushButton('애국가', self)
        button2 = QPushButton('별 헤는 밤', self)

        # 버튼 클릭 시 호출할 메서드 연결
        button1.clicked.connect(lambda: self.openWindow('default1.txt'))
        button2.clicked.connect(lambda: self.openWindow('default2.txt'))

        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button_container)

        self.setLayout(layout)

    def openWindow(self, file_name):
        self.close()
        self.parent.showWindow(file_name)