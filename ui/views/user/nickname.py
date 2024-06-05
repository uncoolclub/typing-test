import tkinter as tk

from ui.global_font import GlobalFont
from ui.widgets.tkdialog import TKDialog

from ui.widgets.tklabel import TKLabel


class NicknameInputDialog:
    def __init__(self, master):
        self.master = master
        self.nickname = None
        self.create_dialog(master)

    def create_dialog(self, master):
        def build_example_content(frame, dialog):
            message_label = TKLabel(frame, text="닉네임을 입력해 주세요", font_size=24).create_label()
            message_label.pack(fill="both", expand=True, padx=10, pady=10)

            font = GlobalFont.get_global_font(font_size=20, use_type='tk')
            self.input_entry = tk.Entry(frame, textvariable=self.nickname, font=font, relief="flat",
                                        bd=0, bg="white",
                                        insertbackground="black", selectbackground="black", selectforeground="white")
            self.input_entry.pack(side="left", fill="x", expand=True, padx=5)

            submit_button = tk.Button(frame, text="확인", command=lambda: print("nickname", self.nickname))
            submit_button.pack(pady=10)

        dialog = TKDialog(master, master, title="닉네임", content_frame_builder=build_example_content)
        dialog.wait_window()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    NicknameInputDialog(root)
    root.mainloop()
