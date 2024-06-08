import os.path
import customtkinter as ctk
from tkinter import Frame, RAISED, SUNKEN, LabelFrame, Label, Entry, StringVar
from PIL import Image, ImageTk

from config import IMG_LOCATION
from logic.file.textFile import TextFile
from ui.global_font import GlobalFont
from ui.widgets.progressbar import Progressbar
from logic.measure.measure_manager import MeasureManager
from ui.widgets.timer import Timer
from ui.widgets.tklabel import TKLabel


class ShortTextWindow:
    def __init__(self, master):
        # 기본 창 설정
        self.master = master
        self.master.title("짧은글 연습")
        self.master.geometry("1024x768")
        self.master.configure(bg="#AAAAAA")

        # 측정 관리자와 텍스트 파일 로드
        self.measure_manager = MeasureManager()
        self.current_sentence_index = 0
        self.text_file = TextFile('default1.txt')
        self.texts = self.text_file.getText()

        # 사용자 입력 관리를 위한 StringVar 초기화
        self.input_text_var = StringVar()
        self.input_text_var.trace_add("write", self.on_text_changed)

        # 사용자 인터페이스 생성
        self.create_window()

    def create_window(self):
        # 메인 프레임 설정
        frame = Frame(self.master, relief=RAISED, bd=2, bg="#AAAAAA")
        frame.pack(side="top", fill="both", padx=30, pady=20)

        # 타이틀 아이콘 로드 및 표시
        icon_path = os.path.join(IMG_LOCATION, 'ic_keyboard.png')
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)

        title_label = TKLabel(master=frame, text="짧은글 연습").create_label(
            height=30, fg_color="#000088", anchor="w", text_color="white", image=icon_photo, compound="left", padx=10)
        title_label.pack(side="top", fill='x', padx=10, pady=10)

        # 짧은 텍스트 표시 프레임
        short_text_frame = Frame(frame, relief=SUNKEN, bd=2, bg="#AAAAAA")
        short_text_frame.pack(side="top", fill="both", padx=10)
        self.short_text_label = TKLabel(master=short_text_frame,
                                        text=self.texts[self.current_sentence_index]).create_label(height=60,
                                                                                                   anchor="w")
        self.short_text_label.pack(side="top", fill="x", padx=15, pady=20)

        # 진행 상황 프레임 설정
        global_font = GlobalFont.get_global_font()
        progress_frame = LabelFrame(frame, text="  빠르기·정확도  ", relief=SUNKEN, bd=2, bg="#AAAAAA",
                                    fg="black", font=global_font, background="#AAAAAA", labelanchor="n")
        progress_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # 최대 속도 및 현재 속도 진행률 표시
        inner_frame = Frame(progress_frame, bg="#AAAAAA")
        inner_frame.pack(fill="both", pady=30)
        self.max_speed_label = Progressbar(master=inner_frame, text="최고 속도: ", default_font=global_font, value=0,
                                           max_value=500, progress_color="#A80000")
        self.max_speed_label_frame = self.max_speed_label.create_widgets()
        self.max_speed_label_frame.pack(padx=20, pady=10, fill="x")

        self.current_speed_label = Progressbar(master=inner_frame, text="현재 속도: ", default_font=global_font, value=0,
                                               max_value=500, progress_color="#0000A8")
        self.current_speed_label_frame = self.current_speed_label.create_widgets()
        self.current_speed_label_frame.pack(padx=20, pady=10, fill="x")

        # 정확도 진행률 표시
        self.accuracy_label = Progressbar(master=inner_frame, text="정확도: ", default_font=global_font, value=0,
                                          max_value=100, progress_color="#00A8A8")
        self.accuracy_label_frame = self.accuracy_label.create_widgets()
        self.accuracy_label_frame.pack(padx=20, pady=10, fill="x")

        # 결과 프레임 설정
        result_frame = LabelFrame(frame, text="  결과  ", relief=SUNKEN, bd=2, bg="#AAAAAA", fg="black",
                                  font=global_font, background="#AAAAAA", labelanchor="n")
        result_frame.pack(side="right", fill="both", padx=10, pady=10)

        self.results = {
            "typed_chars": Label(result_frame, text="0타", font=global_font, bg="#AAAAAA", anchor="e",
                                 justify="right"),
            "correct_chars": Label(result_frame, text="0타", font=global_font, bg="#AAAAAA", anchor="e",
                                   justify="right"),
            "practice_time": Label(result_frame, text="0.0초", font=global_font, bg="#AAAAAA", anchor="e",
                                   justify="right"),
            "current_speed": Label(result_frame, text="0타/분", font=global_font, bg="#AAAAAA", anchor="e",
                                   justify="right"),
            "accuracy": Label(result_frame, text="0%", font=global_font, bg="#AAAAAA", anchor="e",
                              justify="right")
        }

        # 결과 표시
        results_labels = [
            ("쓰인 글자수:", self.results["typed_chars"]),
            ("정확한 글자수:", self.results["correct_chars"]),
            ("연습 시간:", self.results["practice_time"]),
            ("현재 속도:", self.results["current_speed"]),
            ("정확도:", self.results["accuracy"]),
        ]

        for row, (label_text, result_label) in enumerate(results_labels):
            Label(result_frame, text=label_text, font=global_font, bg="#AAAAAA", anchor="w", justify="left").grid(
                row=row, column=0, sticky="w", padx=20, pady=5)
            result_label.grid(row=row, column=1, sticky="e", padx=20, pady=5)

        # 입력 및 타이머 설정
        bottom_frame = Frame(self.master, relief=RAISED, bd=2, bg="#AAAAAA")
        bottom_frame.pack(side="bottom", fill="x", padx=10, pady=5)

        input_label = TKLabel(master=bottom_frame, text="한글-2").create_label(
            anchor="w", fg_color="#AAAAAA")
        input_label.pack(side="left", padx=5, pady=5)

        self.input_entry = Entry(bottom_frame, textvariable=self.input_text_var, font=global_font, relief="flat", bd=0,
                                 bg="white",
                                 insertbackground="black", selectbackground="black", selectforeground="white")
        self.input_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.input_entry.bind("<Return>", self.on_enter)

        self.timer_label = Timer(master=bottom_frame, text="00:00", font=global_font, bg="#AAAAAA", anchor="e")
        self.timer_label.pack(side="right", padx=5, pady=5)
        self.timer_label.start()

        self.measure_manager.startTest(self.texts[self.current_sentence_index])

    # 엔터 키 입력 이벤트 처리
    def on_enter(self, event):
        text = self.input_entry.get()
        self.check_accuracy_and_move_to_next_line(text)

    # 텍스트 변경 이벤트 처리
    def on_text_changed(self, *args):
        text = self.input_text_var.get()
        self.measure_manager.onTextChanged(text)
        self.update_speed_and_accuracy()

    # 속도 및 정확도 업데이트
    def update_speed_and_accuracy(self):
        cpm, max_cpm = self.measure_manager.updateSpeed()
        self.current_speed_label.update_value(cpm, unit="타/분")
        self.max_speed_label.update_value(max_cpm, unit="타/분")
        self.results["current_speed"].configure(text=f"{cpm:.0f}타/분")
        self.results["typed_chars"].configure(text=f"{len(self.input_entry.get())}타")

        accuracy = self.measure_manager.calculate_overall_accuracy([self.input_entry],
                                                                   [self.texts[self.current_sentence_index]])
        self.accuracy_label.update_value(accuracy, unit="%")
        self.results["accuracy"].configure(text=f"{accuracy:.2f}%")

    # 다음 줄로 이동 가능 여부 판단
    def can_move_to_next_line(self, text):
        print(text, self.current_sentence_index, self.texts)
        if self.current_sentence_index < len(self.texts):
            typing_text_length = len(text.rstrip())
            current_sentence_length = len(self.texts[self.current_sentence_index])

            print('can_move_to_next_line', typing_text_length >= current_sentence_length)
            return typing_text_length >= current_sentence_length
        return False

    # 다음 줄로 이동
    def move_to_next_line(self):
        self.current_sentence_index += 1
        if self.current_sentence_index < len(self.texts):
            self.short_text_label.configure(text=self.texts[self.current_sentence_index])
            self.input_entry.delete(0, 'end')
            self.measure_manager.startTest(self.texts[self.current_sentence_index])
            self.update_speed_and_accuracy()
        else:
            self.input_entry.configure(state='disabled')
            self.short_text_label.configure(text="연습 완료!")

    # 정확도 체크 및 다음 줄로 이동 처리
    def check_accuracy_and_move_to_next_line(self, text):
        print(text)
        if self.can_move_to_next_line(text):
            self.move_to_next_line()


if __name__ == "__main__":
    font_family, font_size = GlobalFont.get_font()
    tk_font = (font_family, font_size)

    root = ctk.CTk()
    root.title("메인 윈도우")
    root.geometry("1024x768")
    root.configure(fg_color="#AAAAAA")
    short_practice = ShortTextWindow(master=root)
    root.mainloop()
