from tkinter import Frame, RAISED
import customtkinter as ctk
from ui.font_loader import FontLoader


class Button:
    def __init__(self, master, text, default_font=None, onclick=None):
        self.master = master
        self.text = text
        self.default_font = default_font
        self.onclick = onclick

    def create_button(self, font=None, text_color="black", fg_color="#AAAAAA", **kwargs):
        if font is None:
            font = self.default_font

        font_family, font_size = FontLoader.load_custom_font(font[0], size=font[1])

        tk_font = (font_family, font_size)
        text_width = self.master.font.measure(self.text)

        button_width = max(text_width + 20, 70)

        button_frame = Frame(self.master, relief=RAISED, bd=2, bg=fg_color, width=button_width, height=40)
        button_frame.pack_propagate(False)

        button = ctk.CTkButton(
            master=button_frame,
            font=tk_font,  # 로딩한 폰트 사용
            text=self.text,
            text_color=text_color,
            fg_color=fg_color,
            hover_color="#D3D3D3",
            border_width=0,
            corner_radius=0,
            command=self.onclick,
            **kwargs
        )
        button.pack(fill="both", expand=True)

        return button_frame
