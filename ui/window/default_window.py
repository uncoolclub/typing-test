import os
from tkinter import Frame, RAISED
from PIL import Image, ImageTk

from ui.menu.main_menu import MainMenu
from ui.widgets.tklabel import TKLabel
from config import IMG_LOCATION


class DefaultWindow:
    def __init__(self, root, master, fill="both", title="짧은글 연습", icon_name="ic_keyboard.png", window_size="1024x768", bg_color="#AAAAAA"):
        self.root = root
        self.master = master
        self.fill = fill
        self.window_size = window_size
        self.bg_color = bg_color
        self.icon_name = icon_name

        MainMenu(root=self.root, master=self.master)

        self.master.title(title)
        self.master.geometry(self.window_size)
        self.master.configure(bg=self.bg_color)

        self.frame = Frame(self.master, relief=RAISED, bd=2, bg=self.bg_color)
        self.frame.pack(side="top", fill=self.fill, padx=50, pady=100)

        self.set_icon()
        self.add_title(title)

    def set_icon(self):
        icon_path = os.path.join(IMG_LOCATION, self.icon_name)
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.icon_photo = ImageTk.PhotoImage(icon_image)

    def add_title(self, title):
        title_label = TKLabel(master=self.frame, text=title, font_size=22).create_label(
            height=30, fg_color="#000088", anchor="w", text_color="white", image=self.icon_photo, compound="left",
            padx=10)
        title_label.pack(side="top", fill='x', padx=10, pady=10)

    def get_frame(self):
        return self.frame
