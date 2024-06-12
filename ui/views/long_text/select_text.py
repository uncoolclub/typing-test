from tkinter import LabelFrame, Label, GROOVE, Frame
from ui.global_font import GlobalFont
from ui.widgets.tklistbox import TKListbox
import customtkinter as ctk

# @TODO: 파일명에 맞게 파일을 추가해 주세요.
SELECT_LIST_BOX = [
    {"label": "하늘과 바람과 별과 시", "file_name": "default2.txt"},
    {"label": "애국가", "file_name": "default1.txt"},
    {"label": "동백꽃", "file_name": "default4.txt"},
    {"label": "별 헤는 밤", "file_name": "default5.txt"},
    {"label": "부서와 안나귀", "file_name": "default6.txt"},
    {"label": "성산도", "file_name": "default7.txt"},
    {"label": "보고싶어", "file_name": "default8.txt"},
    {"label": "나의 사랑", "file_name": "default9.txt"},
]


class SelectTextWindow:
    def __init__(self, master):
        self.master = master
        self.create_window(master)

    def create_window(self, master):
        from ui.window.default_window import DefaultWindow
        custom_window = DefaultWindow(root=master, master=master, title="글 선택", window_size="720x768")
        frame = custom_window.get_frame()

        font = GlobalFont.get_global_font(font_size=24)
        select_text_frame = LabelFrame(frame, text="  글  ", relief=GROOVE, bd=3, bg="#AAAAAA", fg="white",
                                       font=font, labelanchor="n")
        select_text_frame.pack(padx=70, pady=10, fill="both", expand=True)

        custom_listbox = TKListbox(select_text_frame, SELECT_LIST_BOX, on_item_selected=self.on_item_selected)
        custom_listbox.create_listbox()

        label_frame = Frame(frame, relief=GROOVE, bd=2, bg="#AAAAAA")
        label_frame.pack(padx=5, pady=(20, 5), fill="x", expand=True)

        notice_font = GlobalFont.get_global_font(font_size=20)
        label = Label(label_frame, text="연습하고자 하는 글을 선택하세요", font=notice_font, bg="#AAAAAA", fg="#FFFF00", anchor="w")
        label.pack(fill="both")

    def on_item_selected(self, item):
        self.open_long_text_window(item)

    def open_long_text_window(self, item):
        self.master.destroy()

        new_root = ctk.CTk()
        new_root.geometry("1024x768")
        new_root.configure(fg_color="#AAAAAA")

        from ui.views.long_text.long_text import LongTextWindow
        LongTextWindow(new_root, file_name=item['file_name'], label=item['label'])
        new_root.mainloop()


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1024x768")
    root.configure(fg_color="#AAAAAA", padx=10)

    SelectTextWindow(root)
    root.mainloop()
