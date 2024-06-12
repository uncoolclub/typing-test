import customtkinter as ctk

from ui.global_font import GlobalFont


class TKLabel:
    def __init__(self, master, text, font_size=18, default_text_color="black"):
        self.master = master
        self.text = text
        self.font_size = font_size
        self.default_text_color = default_text_color

    def create_label(self, text_color=None, fg_color="#AAAAAA", **kwargs):
        if text_color is None:
            text_color = self.default_text_color
        font = GlobalFont.get_global_font(font_size=self.font_size, use_type='ctk')

        label = ctk.CTkLabel(
            master=self.master,
            text=self.text,
            text_color=text_color,
            fg_color=fg_color,
            font=font,
            **kwargs
        )

        return label
