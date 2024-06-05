from tkinter import Frame, SUNKEN, Label
from ui.global_font import GlobalFont
import customtkinter as ctk


class Progressbar:
    def __init__(self, master, text, default_font, value=0, max_value=100, progress_color="#0000A0", **kwargs):
        self.progressbar = None
        self.value_label = None
        self.master = master
        self.text = text
        self.default_font = default_font
        self.value = value
        self.max_value = max_value
        self.progress_color = progress_color
        self.kwargs = kwargs
        self.frame = self.create_widgets()

    def create_widgets(self, font=None):
        if font is None:
            font = self.default_font

        font_family, font_size = GlobalFont.get_font()
        tk_font = (font_family, font_size)

        # 프레임 생성
        frame = Frame(self.master, bg="#AAAAAA")

        # Label 생성 및 배치
        label = Label(frame, text=self.text, font=tk_font, bg="#AAAAAA")
        label.pack(side="left", padx=5)

        # Progressbar 값 표시할 Label
        self.value_label = Label(frame, text=f"{self.value}", font=tk_font, bg="#666666", fg="white", width=5)
        self.value_label.pack(side="left")

        progressbar_frame = Frame(frame, relief=SUNKEN, bd=2, bg="#AAAAAA", width=200, height=30)
        progressbar_frame.pack_propagate(False)
        progressbar_frame.pack(side="left", fill="x", padx=20, expand=True)

        # ProgressBar 생성 및 배치
        self.progressbar = ctk.CTkProgressBar(
            master=progressbar_frame,
            corner_radius=0,
            fg_color="#AAAAAA",
            progress_color=self.progress_color,
            border_width=1,
            **self.kwargs
        )
        self.progressbar.pack(fill="both", expand=True)
        self.progressbar.set(self.value / self.max_value)

        # 프레임 반환
        return frame

    def update_value(self, new_value, unit="%"):
        self.value = new_value
        if unit == "%":
            self.value_label.config(text=f"{self.value}{unit}")
        else:
            self.value_label.config(text=f"{self.value:.0f}{unit}")
        self.progressbar.set(self.value / self.max_value)

