import tkinter as tk
from tkinter import messagebox, Toplevel, Frame, RAISED
from ui.global_font import GlobalFont
from ui.views.main.main import Main
from ui.widgets.tklabel import TKLabel
from utils.user import User


class NicknameInputDialog:
    def __init__(self, master, root):
        self.master = master
        self.root = root
        self.nickname = None
        self.create_dialog()

    def create_dialog(self):
        # 기본 창 설정
        self.window = Toplevel(self.master)
        self.window.title("닉네임 입력")
        self.window.geometry("720x280")
        self.window.configure(bg="#AAAAAA")

        frame = Frame(self.window, relief=RAISED, bd=2, bg="#AAAAAA")
        frame.pack(fill="both", padx=30, pady=20)

        message_label = TKLabel(frame, text="닉네임을 입력해 주세요", font_size=24).create_label()
        message_label.pack(fill="both", expand=True, padx=10, pady=10)

        font = GlobalFont.get_global_font(font_size=20, use_type='tk')
        input_entry = tk.Entry(frame, font=font, relief="flat",bd=0, bg="white", fg="black",
                                    insertbackground="black", selectbackground="black", selectforeground="white")
        input_entry.pack(side="left", fill="x", expand=True, padx=5)

        submit_button = tk.Button(frame, text="확인", command=lambda: self.enter_nickname(input_entry.get())) # 버튼 이벤트 연결
        submit_button.pack(pady=10)

    def enter_nickname(self, nickname):
        # 텍스트가 영어인지 체크
        if nickname.isalpha() and nickname.isascii():
            self.nickname = nickname
            User().set_nickname(nickname) # user 생성
            self.window.destroy() # 현재 떠있는 닉네임 입력 창 닫기
            Main(self.master) # 메인 노출
        else:
            messagebox.showwarning("warning", "영어만 입력 가능합니다.")
