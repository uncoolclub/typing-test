from ui.global_font import GlobalFont
import customtkinter as ctk

from ui.views.user.nickname import NicknameInputDialog
from utils.user import User


class Index:
    def __init__(self, master):
        self.master = master
        self.user = None
        self.nickname_input_dialog = None
        self.show_nickname_input_dialog()

    def show_nickname_input_dialog(self):
        self.nickname_input_dialog = NicknameInputDialog(self.master, self)
        self.master.mainloop()  # 여기서 mainloop 호출

    def create_user(self, nickname):
        self.user = User().set_nickname(nickname)


if __name__ == "__main__":
    font_family, font_size = GlobalFont.get_font()
    tk_font = (font_family, font_size)

    root = ctk.CTk()
    Index(root)
