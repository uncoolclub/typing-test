import customtkinter as ctk

class Label:
    def __init__(self, master, text, default_font, default_text_color="black"):
        self.master = master
        self.text = text
        self.default_font = default_font
        self.default_text_color = default_text_color

    def create_label(self, font=None, text_color=None, font_size=None, **kwargs):
        if font is None:
            font = self.default_font
        if text_color is None:
            text_color = self.default_text_color

        label = ctk.CTkLabel(
            master=self.master,
            font=font,
            text=self.text,
            text_color=text_color,
            **kwargs  # Add additional keyword arguments
        )
        return label
