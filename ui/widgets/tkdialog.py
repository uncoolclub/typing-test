import tkinter as tk
from tkinter import Frame, RAISED
from PIL import Image, ImageTk
import os

from config import IMG_LOCATION
from ui.widgets.tklabel import TKLabel


class TKDialog(tk.Toplevel):
    def __init__(self, root, master, fill="both", title="다이얼로그", icon_name="ic_keyboard.png", window_size="720x480",
                 bg_color="#AAAAAA", content_frame_builder=None):
        super().__init__(master)
        self.root = root
        self.master = master
        self.fill = fill
        self.window_size = window_size
        self.bg_color = bg_color
        self.icon_name = icon_name
        self.result = None
        self.content_frame_builder = content_frame_builder

        self.configure(bg=self.bg_color, relief=RAISED)  # 배경색 설정
        self.overrideredirect(True)  # 창의 제목 표시줄 제거
        self.geometry(self.window_size)  # 윈도우 크기 설정

        self.create_widgets(title)  # 위젯 생성 함수 호출

    def create_widgets(self, title):
        # 헤더 프레임 생성
        header_frame = Frame(self, bg="#000088", height=30)
        header_frame.pack(fill="x")

        # 아이콘 설정
        self.set_icon(header_frame)

        # 제목 추가
        self.add_title(header_frame, title)

        # 닫기 버튼 추가
        self.add_close_button(header_frame)

        # 윈도우 드래그 기능 활성화
        self.bind_draggable(self)

        # 내용 프레임 생성
        content_frame = Frame(self, bg=self.bg_color)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # 커스텀 내용 구성
        if self.content_frame_builder:
            self.content_frame_builder(content_frame, self)

    def set_icon(self, header_frame):
        icon_path = os.path.join(IMG_LOCATION, self.icon_name)  # 아이콘 경로 설정
        icon_image = Image.open(icon_path)  # 아이콘 이미지 불러오기
        icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)  # 아이콘 크기 조정
        self.icon_photo = ImageTk.PhotoImage(icon_image)  # PhotoImage 객체 생성
        icon_label = tk.Label(header_frame, image=self.icon_photo, bg="#000088")  # 아이콘 라벨 생성
        icon_label.pack(side="left", padx=5)

    @staticmethod
    def add_title(header_frame, title):
        title_label = TKLabel(header_frame, text=title, font_size=22).create_label(
            bg_color="#000088", fg_color="#000088", text_color="white", padx=10)
        title_label.pack(side="left", fill='x', expand=True, padx=10, pady=5)  # 제목 라벨 배치

    def add_close_button(self, header_frame):
        close_icon_path = os.path.join(IMG_LOCATION, "ic_close.png")  # 닫기 아이콘 경로 설정
        close_icon_image = Image.open(close_icon_path)  # 닫기 아이콘 이미지 불러오기
        close_icon_image = close_icon_image.resize((20, 20), Image.Resampling.LANCZOS)  # 크기 조정
        close_icon_photo = ImageTk.PhotoImage(close_icon_image)  # PhotoImage 객체 생성

        close_button = tk.Button(
            header_frame,
            image=close_icon_photo,
            text="",
            bg="#000088",
            fg="white",
            command=self.destroy,  # 클릭 시 창 닫기
            borderwidth=0,
            width=20,
            height=20
        )
        close_button.image = close_icon_photo  # 이미지 참조 유지
        close_button.pack(side="right", padx=10, pady=5)

    def bind_draggable(self, widget):
        widget.bind("<ButtonPress-1>", self.start_move)  # 마우스 버튼 누름 이벤트 바인드
        widget.bind("<ButtonRelease-1>", self.stop_move)  # 마우스 버튼 뗌 이벤트 바인드
        widget.bind("<B1-Motion>", self.on_motion)  # 마우스 이동 이벤트 바인드

    def start_move(self, event):
        self.x = event.x  # 현재 마우스 x 위치
        self.y = event.y  # 현재 마우스 y 위치

    def stop_move(self, event):
        self.x = None  # 마우스 x 위치 초기화
        self.y = None  # 마우스 y 위치 초기화

    def on_motion(self, event):
        x = self.winfo_pointerx() - self.x  # 이동한 마우스 x 위치 계산
        y = self.winfo_pointery() - self.y  # 이동한 마우스 y 위치 계산
        self.geometry(f"+{x}+{y}")  # 윈도우 위치 업데이트
