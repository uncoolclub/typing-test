from ui.global_font import GlobalFont
import customtkinter as ctk

from ui.views.user.nickname import NicknameInputDialog


class Index:
    def __init__(self, master):
        self.master = master
        self.user = None
        self.nickname_input_dialog = None
        self.show_nickname_input_dialog() # 첫 인입 시, 닉네임 입력 창 노출

    def show_nickname_input_dialog(self):
        self.nickname_input_dialog = NicknameInputDialog(self.master, self)
        self.master.mainloop()


if __name__ == "__main__":
    font_family, font_size = GlobalFont.get_font()
    tk_font = (font_family, font_size)

    root = ctk.CTk()
    Index(root)
