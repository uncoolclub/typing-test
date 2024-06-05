from tkinter import Frame, RAISED, Label
import customtkinter as ctk

from ui.global_font import GlobalFont


class TKButton:
    def __init__(self, master, text, onclick=None):
        self.master = master
        self.text = text
        self.onclick = onclick

    def create_button(self, text_color="black", fg_color="#AAAAAA", **kwargs):
        global_font = GlobalFont.get_global_font(use_type='ctk')

        temp_label = Label(self.master, text=self.text, font=global_font)
        temp_label.pack_forget()
        text_width = temp_label.winfo_reqwidth()
        temp_label.destroy()

        button_width = max(text_width + 20, 70)
        button_frame = Frame(self.master, relief=RAISED, bd=2, bg=fg_color, width=button_width, height=40)
        button_frame.pack_propagate(False)

        button = ctk.CTkButton(
            master=button_frame,
            text=self.text,
            text_color=text_color,
            fg_color=fg_color,
            hover_color="#D3D3D3",
            border_width=0,
            corner_radius=0,
            command=self.onclick,
            font=global_font,
            **kwargs
        )
        button.pack(fill="both", expand=True)

        return button_frame
