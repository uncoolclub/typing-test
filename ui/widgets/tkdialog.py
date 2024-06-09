import tkinter as tk
from tkinter import Frame
from PIL import Image, ImageTk
import os

from config import IMG_LOCATION
from ui.widgets.tklabel import TKLabel


class TKDialog(tk.Toplevel):
    def __init__(self, root, master, fill="both", title="다이얼로그", icon_name="ic_keyboard.png", window_size="720x480", bg_color="#AAAAAA", content_frame_builder=None):
        super().__init__(master)
        self.root = root
        self.master = master
        self.fill = fill
        self.window_size = window_size
        self.bg_color = bg_color
        self.icon_name = icon_name
        self.result = None
        self.content_frame_builder = content_frame_builder

        self.configure(bg=self.bg_color)
        self.overrideredirect(True)
        self.geometry(self.window_size)

        self.create_widgets(title)

    def create_widgets(self, title):
        # Create header frame
        header_frame = Frame(self, bg="#000088", height=30)
        header_frame.pack(fill="x")

        # Set icon
        self.set_icon(header_frame)

        # Add title
        self.add_title(header_frame, title)

        # Add close button
        self.add_close_button(header_frame)

        # Allow window dragging
        self.bind_draggable(self)

        # Create content frame
        content_frame = Frame(self, bg=self.bg_color)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Build the custom content inside content_frame
        if self.content_frame_builder:
            self.content_frame_builder(frame=content_frame, dialog=self)

    def set_icon(self, header_frame):
        icon_path = os.path.join(IMG_LOCATION, self.icon_name)
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.icon_photo = ImageTk.PhotoImage(icon_image)
        icon_label = tk.Label(header_frame, image=self.icon_photo, bg="#000088")
        icon_label.pack(side="left", padx=5)

    def add_title(self, header_frame, title):
        title_label = TKLabel(header_frame, text=title, font_size=22).create_label(
            bg_color="#000088", fg_color="#000088", text_color="white", padx=10)
        title_label.pack(side="left", fill='x', expand=True, padx=10, pady=5)

    def add_close_button(self, header_frame):
        close_icon_path = os.path.join(IMG_LOCATION, "ic_close.png")
        close_icon_image = Image.open(close_icon_path)
        close_icon_image = close_icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        close_icon_photo = ImageTk.PhotoImage(close_icon_image)

        close_button = tk.Button(
            header_frame,
            image=close_icon_photo,
            text="",
            bg="#000088",
            fg="white",
            command=self.destroy,
            borderwidth=0,
            width=20,
            height=20
        )
        close_button.image = close_icon_photo
        close_button.pack(side="right", padx=10, pady=5)

    def bind_draggable(self, widget):
        widget.bind("<ButtonPress-1>", self.start_move)
        widget.bind("<ButtonRelease-1>", self.stop_move)
        widget.bind("<B1-Motion>", self.on_motion)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_motion(self, event):
        x = self.winfo_pointerx() - self.x
        y = self.winfo_pointery() - self.y
        self.geometry(f"+{x}+{y}")