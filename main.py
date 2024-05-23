import os
import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication, QTextEdit
from config import FONT_LOCATION, IMG_LOCATION, SVG_LOCATION
from ui.longTestWindow import LongTestWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("타자 연습")
        self.setFixedSize(1024, 768)

        self.background_pixmap = QPixmap(os.path.join(IMG_LOCATION, 'wood_background.png'))
        self.scaled_pixmap = self.background_pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.scaled_pixmap))  # Convert QPixmap to QBrush
        self.setPalette(palette)

        self.setStyleSheet("""
            QMainWindow {
                background-color: transparent;
            }
            QPushButton {
                color: black;
                background-color: #d7bf93;
                border: 2px solid black;
                border-radius: 10px;
                font-size: 14px;
                padding: 10px;
                min-width: 200px;
                max-height: 60px;
            }
            QPushButton:pressed {
                background-color: #caa472;
            }
            QLabel {
                font-size: 22px;
                color: black;
            }
            QLabel#titleLabel {
                font-size: 24px;
                font-weight: bold;
                color: black;
            }
            QWidget#infoContainer {
                background-color: #193d36;
                border-radius: 10px;
            }
            QLabel#infoText {
                font-size: 18px;
                color: white;
                text-align: left;
            }
            QLabel#iconLabel {
                border: 2px solid black;
                border-radius: 25px;
                background-color: #d7bf93;
            }
            QPushButton#customButton {
                font-size: 22px;
            }
        """)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setAlignment(Qt.AlignTop)

        info_container = QWidget(self)
        info_container.setObjectName("infoContainer")
        info_layout = QHBoxLayout(info_container)

        info_image = QLabel(self)
        info_pixmap = QPixmap(os.path.join(IMG_LOCATION, 'character.png')).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        info_image.setPixmap(info_pixmap)
        info_image.setFixedSize(40, 40)
        info_layout.addWidget(info_image)

        info_text = QLabel("오프라인에서도 가능한 타자 연습을 즐겨 보아요! (ᗒᗊᗕ)", self)
        info_text.setObjectName("infoText")
        info_layout.addWidget(info_text)

        main_layout.addWidget(info_container)

        horizontal_layout = QHBoxLayout()

        button_container = QWidget()
        button_layout = QVBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)

        button_texts = ["자리 연습", "낱말 연습", "짧은 글 연습", "긴 글 연습", "놀이", "환경 설정", "끝"]
        icons = [
            os.path.join(SVG_LOCATION, 'ic_documents.svg'),
            os.path.join(SVG_LOCATION, 'ic_chat.svg'),
            os.path.join(SVG_LOCATION, 'ic_document_text.svg'),
            os.path.join(SVG_LOCATION, 'ic_documents.svg'),
            os.path.join(SVG_LOCATION, 'ic_rank.svg'),
            os.path.join(SVG_LOCATION, 'ic_documents.svg'),
            os.path.join(SVG_LOCATION, 'ic_documents.svg')
        ]

        for text, icon_path in zip(button_texts, icons):
            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setSpacing(0)

            icon_label = QLabel(container)
            icon_label.setObjectName("iconLabel")
            icon_pixmap = QPixmap(icon_path).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(icon_pixmap)
            icon_label.setFixedSize(50, 50)
            icon_label.setAlignment(Qt.AlignCenter)

            button = QPushButton(text, container)
            button.clicked.connect(self.showWindow)
            button.setObjectName("customButton")
            button.setFixedHeight(50)
            button.setStyleSheet("border: none; text-align: left; padding-left: 60px;")

            container_layout.addWidget(icon_label)
            container_layout.addWidget(button)

            button_layout.addWidget(container)

        horizontal_layout.addWidget(button_container)

        info_text_area = QLabel("글자판의 위치를 익히는 곳입니다. 글자판에 익숙하지 않다면 제일 먼저 자리 연습을 합니다.\n"
                                "좌우 화살표 글쇠나 마우스로 자리 연습 단계를 바꿀 수 있습니다. 화면에서 연습할 글쇠를 미리 볼 수 있으며, "
                                "어떤 손가락으로 글쇠를 눌러야 하는지 보여 줍니다.", self)
        info_text_area.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        info_text_area.setStyleSheet("font-size: 18px; color: black; padding: 10px;")
        info_text_area.setFixedSize(500, 200)
        horizontal_layout.addWidget(info_text_area)

        main_layout.addLayout(horizontal_layout)

    def resizeEvent(self, event):
        self.scaled_pixmap = self.background_pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(self.scaled_pixmap))
        self.setPalette(palette)
        super(MainWindow, self).resizeEvent(event)

    def showWindow(self):
        self.hide()
        self.longTestWin =LongTestWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    font_path = os.path.join(FONT_LOCATION, 'DungGeunMo.ttf')
    if os.path.exists(font_path):
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app.setFont(QFont(font_family))
            print(f"Font loaded: {font_family}")
        else:
            print("Failed to load font:", font_path)
    else:
        print(f"Font not found: {font_path}")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
