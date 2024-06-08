import os
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Frame, LEFT, RIGHT, X

from config import IMG_LOCATION
from ui.widgets.tklabel import TKLabel
from ui.widgets.tkbutton import TKButton

from ui.views.short_text.short_text import ShortTextWindow
from ui.views.long_text.select_text import SelectTextWindow

# TODO: 이름을 필요한 창 클래스로 변경해 주세요.
MAIN_MENU = {
    "낱말 연습": "WordPracticeWindow",
    "짧은글 연습": ShortTextWindow,
    "긴글 연습": SelectTextWindow,
    "파일 불러오기": "FileLoadWindow",
    "통계": "StatisticsWindow",
    "도움말": "HelpWindow"
}


class MainMenu:
    def __init__(self, root, master, default_text_color="white"):
        self.root = root
        self.master = master
        self.default_text_color = default_text_color
        self.create_menu_bar()
        self.root.protocol("WM_DELETE_WINDOW", self.quit_function)
        self.pending_tasks = []

    def create_menu_bar(self):
        icon_path = os.path.join(IMG_LOCATION, "ic_keyboard.png")
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)

        title_frame = Frame(self.master, bg="#666666")
        title_frame.pack(side="top", fill=X)

        icon_label = TKLabel(title_frame, text="").create_label(
            image=icon_photo, fg_color="#666666")
        icon_label.pack(side=LEFT, padx=5)

        title_label = TKLabel(title_frame, text="한컴타자연습").create_label(
            fg_color="#666666", text_color="white", anchor="w")
        title_label.pack(side=LEFT, fill=X, expand=True, padx=10)

        close_icon_path = os.path.join(IMG_LOCATION, "ic_close.png")
        close_icon_image = Image.open(close_icon_path)
        close_icon_image = close_icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        close_icon_photo = ImageTk.PhotoImage(close_icon_image)

        close_button = ctk.CTkButton(
            title_frame,
            image=close_icon_photo,
            text="",
            fg_color="#666666",
            hover_color="#666666",
            command=self.quit_function,
            width=20,
            height=20
        )
        close_button.image = close_icon_photo
        close_button.pack(side=RIGHT, pady=5)

        menu_container = ctk.CTkFrame(self.master, width=640, height=30, fg_color="#AAAAAA", border_width=1,
                                      border_color="black", corner_radius=0)
        menu_container.pack(side="top", fill="x", pady=5)

        for label, window_class in MAIN_MENU.items():
            button_frame = TKButton(
                master=menu_container,
                text=label,
                onclick=lambda wc=window_class: self.open_window(wc)
            ).create_button(fg_color="#AAAAAA")
            button_frame.pack(side="left", padx=1, pady=1, fill='y')

    def open_window(self, window_class):
        if isinstance(window_class, str):
            print(f"{window_class} 구현 되었나요? 🤔")  # 미구현 클래스를 위한 메시지 출력
            return

        self.quit_function()  # 창을 닫기 전에 quit_function을 호출하여 안전하게 종료 처리

        new_root = ctk.CTk()  # 새 root 인스턴스 생성
        new_root.geometry("1024x768")
        new_root.configure(fg_color="#AAAAAA")

        new_root.title(window_class.__name__)  # 클래스 이름을 제목으로 사용
        window_class(master=new_root)  # 윈도우 클래스 인스턴스 생성
        new_root.mainloop()  # 새 창의 mainloop를 시작

    def quit_function(self):
        # 모든 after 작업을 취소
        for task in self.pending_tasks:
            self.root.after_cancel(task)
        try:
            self.root.quit()
            self.root.destroy()
        except Exception as e:
            print(f"Error during closing window: {e}")
