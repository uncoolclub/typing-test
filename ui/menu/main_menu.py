import os
import customtkinter as ctk
from PIL import Image, ImageTk

from ui.views.short_text.short_text import ShortTextWindow
from ui.widgets.tkbutton import TKButton
from tkinter import Toplevel, Frame, LEFT, RIGHT, X
from config import IMG_LOCATION
from ui.widgets.tklabel import TKLabel

MAIN_MENU = ["낱말 연습", "짧은글 연습", "긴글 연습", "파일 불러오기", "통계", "도움말"]


class MainMenu:
    def __init__(self, root, master, default_text_color="white"):
        self.root = root
        self.master = master
        self.default_text_color = default_text_color
        self.create_menu_bar()

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
            command=self.master.quit,
            width=20,
            height=20
        )
        close_button.image = close_icon_photo
        close_button.pack(side=RIGHT, pady=5)

        menu_container = ctk.CTkFrame(self.master, width=640, height=30, fg_color="#AAAAAA", border_width=1,
                                      border_color="black", corner_radius=0)
        menu_container.pack(side="top", fill="x", pady=5)

        # Define actions for each menu item
        actions = {
            "낱말 연습": lambda: self.open_new_window("낱말 연습"),
            "짧은글 연습": self.show_short_text_window,
            "긴글 연습": lambda: self.open_new_window("긴글 연습"),
            "파일 불러오기": lambda: self.open_new_window("파일 불러오기"),
            "통계": lambda: self.open_new_window("통계"),
            "도움말": lambda: self.open_new_window("도움말")
        }

        for label in MAIN_MENU:
            action = actions.get(label, lambda: self.open_new_window(label))  # Default action if not defined
            button_frame = TKButton(
                master=menu_container,
                text=label,
                onclick=action
            ).create_button(fg_color="#AAAAAA")
            button_frame.pack(side="left", padx=1, pady=1, fill='y')

        for i in range(len(MAIN_MENU)):
            menu_container.grid_columnconfigure(i, weight=1, minsize=70)

    def open_new_window(self, label):
        self.root.withdraw()
        new_window = Toplevel(self.root)
        new_window.title(label)
        new_window.geometry("400x300")
        tk_label = TKLabel(new_window, text=f"{label} 창")
        label_widget = tk_label.create_label()
        label_widget.pack(pady=10)

    def show_short_text_window(self):
        self.root.withdraw()
        new_window = Toplevel(self.root)
        new_window.title("짧은글 연습")
        ShortTextWindow(master=new_window)
