from tkinter import LabelFrame, Label, Tk, GROOVE, Frame
from ui.global_font import GlobalFont
from ui.widgets.tklistbox import TKListbox
from ui.window.default_window import DefaultWindow


class SelectTextWindow:
    def __init__(self, master):
        self.master = master
        self.create_window(master)

    @staticmethod
    def create_window(master):
        custom_window = DefaultWindow(root=master, master=master, title="글 선택", window_size="720x768")
        frame = custom_window.get_frame()

        font = GlobalFont.get_global_font(font_size=24)
        select_text_frame = LabelFrame(frame, text="  글  ", relief=GROOVE, bd=3, bg="#AAAAAA", fg="white",
                                       font=font, labelanchor="n")
        select_text_frame.pack(padx=70, pady=10, fill="both", expand=True)

        # Sample items (글 목록)
        items = [
            {"label": "패밀꽃 필 무렵", "on_item_selected": lambda label: print(f"Selected: {label}")},
            {"label": "마지막 잎새", "on_item_selected": lambda label: print(f"Selected: {label}")},
            {"label": "동백꽃", "on_item_selected": lambda label: print(f"Selected: {label}")},
            {"label": "별 헤는 밤", "on_item_selected": lambda label: print(f"Selected: {label}")},
            {"label": "부서와 안나귀", "on_item_selected": lambda label: print(f"Selected: {label}")},
            {"label": "성산도", "on_item_selected": lambda label: print(f"Selected: {label}")},
            {"label": "보고싶어", "on_item_selected": lambda label: print(f"Selected: {label}")},
            {"label": "나의 사랑", "on_item_selected": lambda label: print(f"Selected: {label}")},
        ]

        custom_listbox = TKListbox(select_text_frame, items)
        custom_listbox.create_listbox()

        label_frame = Frame(frame, relief=GROOVE, bd=2, bg="#AAAAAA")
        label_frame.pack(padx=5, pady=(20, 5), fill="x", expand=True)

        notice_font = GlobalFont.get_global_font(font_size=20)
        label = Label(label_frame, text="연습하고자 하는 글을 선택하세요", font=notice_font, bg="#AAAAAA", fg="white", anchor="w")
        label.pack(fill="both")


if __name__ == "__main__":
    root = Tk()
    root.geometry("1024x768")
    root.configure(bg="#AAAAAA", padx=10)

    SelectTextWindow(root)
    root.mainloop()
