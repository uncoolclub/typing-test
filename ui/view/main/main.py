import os
import customtkinter as ctk
from PIL import Image, ImageTk

from lib.image_resizer import ImageResizer
from ui.font_loader import FontLoader
from ui.menu.main_menu import MainMenu
from ui.widgets.label import Label


def main():
    root = ctk.CTk()
    root.title("한컴타자연습")
    root.geometry("1024x768")
    root.configure(fg_color="#AAAAAA")

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    font_path = os.path.abspath("../../../resource/fonts/DOSMyungjo.ttf")
    font_family, font_size = FontLoader.load_custom_font(font_path, size=18)
    tk_font = (font_family, font_size)

    frame = ctk.CTkFrame(master=root, width=1024, height=728, fg_color="#AAAAAA")
    frame.pack(pady=10, padx=10, fill="both", expand=True)

    menu_labels = ["낱말 연습", "짧은글 연습", "긴글 연습", "통계", "도움말"]
    MainMenu(master=frame, labels=menu_labels, default_font=tk_font)

    parent_frame = ctk.CTkFrame(frame, fg_color="white", corner_radius=0)
    parent_frame.pack(pady=50, padx=10, anchor="center")  # Center align the parent_frame

    image_path = "../../../resource/images/bg_main.jpg"
    image = Image.open(image_path)
    image = ImageResizer.resize_and_crop(image, (740, 270))
    photo = ImageTk.PhotoImage(image)

    image_label = Label(parent_frame, text=None, default_font=tk_font).create_label(image=photo, fg_color="white")
    image_label.pack(side="top")

    text_label = Label(parent_frame, text="한컴타자연습은 컴퓨터 초보자를 위한\n프로그램입니다.\n\n"
                                          "한컴타자연습의 단계별 학습을 하루하루 따라하다\n"
                                          "보면, 자신도 모르는 사이에 기본 좋은 타자 실력을 갖추게 됩니다.\n\n",
                       default_font=tk_font).create_label(fg_color="white", text_color="black", justify="left")
    text_label.pack(pady=40, padx=40, anchor='w')

    bottom_label = Label(master=frame, text="아무 메뉴나 누르세요", default_font=tk_font).create_label(
        width=640, height=20, fg_color="#AAAAAA", text_color="#FFFF00")
    bottom_label.pack(side="bottom", pady=10, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()
