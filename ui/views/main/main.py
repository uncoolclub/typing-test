import os
import customtkinter as ctk
from PIL import Image, ImageTk

from config import IMG_LOCATION
from lib.image_resizer import ImageResizer
from ui.menu.main_menu import MainMenu
from ui.widgets.tklabel import TKLabel


def main():
    root = ctk.CTk()
    root.title("한컴타자연습")
    root.geometry("1024x768")
    root.configure(fg_color="#AAAAAA")

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    frame = ctk.CTkFrame(master=root, width=1024, height=728, fg_color="#AAAAAA")
    frame.pack(pady=10, padx=10, fill="both", expand=True)

    MainMenu(root=root, master=frame)

    parent_frame = ctk.CTkFrame(frame, fg_color="white", corner_radius=0)
    parent_frame.pack(pady=50, padx=10, anchor="center")

    image_path = os.path.join(IMG_LOCATION, 'bg_main.jpg')
    image = Image.open(image_path)
    image = ImageResizer.resize_and_crop(image, (740, 270))
    photo = ImageTk.PhotoImage(image)

    image_label = TKLabel(parent_frame, text=None).create_label(image=photo, fg_color="white")
    image_label.pack(side="top")

    text_label = TKLabel(parent_frame, text="한컴타자연습은 컴퓨터 초보자를 위한\n프로그램입니다.\n\n"
                                            "한컴타자연습의 단계별 학습을 하루하루 따라하다\n"
                                            "보면, 자신도 모르는 사이에 기본 좋은 타자 실력을 갖추게 됩니다.\n\n").create_label(fg_color="white",
                                                                                                      text_color="black",
                                                                                                      justify="left")
    text_label.pack(pady=40, padx=40, anchor='w')

    bottom_label = TKLabel(master=frame, text="아무 메뉴나 누르세요").create_label(
        width=640, height=20, fg_color="#AAAAAA", text_color="#FFFF00")
    bottom_label.pack(side="bottom", pady=10, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()