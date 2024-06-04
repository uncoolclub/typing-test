# ui/menu/main_menu.py
import customtkinter as ctk
from PIL import Image, ImageTk

from ui.view.short_text.short_text import ShortTextWindow
from ui.widgets.button import Button
from tkinter import Toplevel

from ui.widgets.label import Label


class MainMenu:
    def __init__(self, master, labels, default_font=None):
        self.master = master
        self.labels = labels
        self.default_font = default_font
        self.create_menu_bar()

    def create_menu_bar(self):
        icon_path = "../../../resource/images/ic_keyboard.png"
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)

        title_label = Label(master=self.master, text="한컴타자연습", default_font=self.default_font).create_label(
            height=30, fg_color="#666666", anchor="w", text_color="white", image=icon_photo, compound="left", padx=10)
        title_label.pack(side="top", fill='x')

        menu_container = ctk.CTkFrame(master=self.master, width=640, height=40, fg_color="#AAAAAA", border_width=1,
                                      border_color="black", corner_radius=0)
        menu_container.pack(side="top", fill="x", pady=5)

        for label in self.labels:
            onclick = lambda l=label: self.open_new_window(l)

            if label == "짧은 글 연습":
                onclick = lambda: ShortTextWindow(self.master, self.default_font)

            button_frame = Button(
                master=menu_container,
                text=label,
                default_font=self.default_font,
                onclick=onclick
            ).create_button(fg_color="#AAAAAA")
            button_frame.pack(side="left", padx=1, pady=1, fill='y')

        for i in range(len(self.labels)):
            menu_container.grid_columnconfigure(i, weight=1, minsize=70)

    def open_new_window(self, label):
        new_window = Toplevel(self.master)
        new_window.title(label)
        new_window.geometry("400x300")
        Label(new_window, text=f"{label} 창").pack(pady=20)
