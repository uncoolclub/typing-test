from ui.global_font import GlobalFont
import tkinter as tk

from ui.views.main.main import Main
from ui.views.user.nickname import NicknameInputDialog
from lib.User import User


class Index:
    def __init__(self, master):
        self.master = master
        self.user = None
        NicknameInputDialog(self.master, self)

    def create_user(self, nickname):
        self.user = User(nickname)
        Main(self.master, self.user)


if __name__ == "__main__":
    font_family, font_size = GlobalFont.get_font()
    tk_font = (font_family, font_size)

    root = tk.Tk()
    root.withdraw()
    Index(root)
    # root.title("메인 윈도우")
    # root.geometry("1024x768")
    root.mainloop()