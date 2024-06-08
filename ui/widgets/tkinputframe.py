from tkinter import Frame, Entry, StringVar
from ui.widgets.tklabel import TKLabel
from ui.widgets.tktimer import TKTimer


class TKInputFrame:
    def __init__(self, master, on_enter_callback, on_text_changed_callback=None, label_text="한글-2", font=None):
        self.master = master
        self.on_enter_callback = on_enter_callback  # Enter 키 입력 시 호출될 콜백 함수
        self.on_text_changed_callback = on_text_changed_callback  # 텍스트 변경 시 호출될 콜백 함수
        self.font = font
        self.input_entry = None  # 입력 필드를 저장할 변수
        self.input_text_var = StringVar()
        self.input_text_var.trace_add("write", self.on_text_changed)  # 텍스트 변경 시 호출될 함수 등록

        self.create_frame(label_text)  # 프레임 생성 함수 호출

    def create_frame(self, label_text):
        # 프레임 생성
        self.frame = Frame(self.master, relief="raised", bd=2, bg="#AAAAAA")
        self.frame.pack(side="bottom", fill="x", padx=10, pady=5)

        # 입력 레이블 생성
        input_label = TKLabel(master=self.frame, text=label_text).create_label(
            anchor="w", fg_color="#AAAAAA")
        input_label.pack(side="left", padx=5, pady=5)

        # 입력 필드 생성
        self.input_entry = Entry(self.frame, textvariable=self.input_text_var, font=self.font, relief="flat", bd=0,
                                 bg="white", insertbackground="black", selectbackground="black",
                                 selectforeground="white")
        self.input_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.input_entry.bind("<Return>", self.on_enter)  # Enter 키 입력 시 호출될 함수 등록

        # 타이머 레이블 생성
        timer_label = TKTimer(master=self.frame, text="00:00", font=self.font, bg="#AAAAAA", anchor="e")
        timer_label.pack(side="right", padx=5, pady=5)
        timer_label.start()  # 타이머 시작

    def on_enter(self, event):
        text = self.input_entry.get()  # 입력된 텍스트 가져오기
        should_delete = self.on_enter_callback(text)  # 콜백 함수 호출

        if should_delete:
            self.input_entry.delete(0, 'end')  # 입력 필드 초기화

    def on_text_changed(self, *args):
        if self.on_text_changed_callback:
            self.on_text_changed_callback(self.input_text_var.get())  # 콜백 함수 호출
