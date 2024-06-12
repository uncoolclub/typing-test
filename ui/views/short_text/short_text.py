import os.path
import threading
import customtkinter as ctk
from tkinter import Frame, RAISED, SUNKEN, LabelFrame, Label, END
from PIL import Image, ImageTk

from config import IMG_LOCATION
from ui.widgets.tkinputframe import TKInputFrame
# from utils.text_file import TextFile
from utils.proverb import Proverb
from ui.global_font import GlobalFont
from ui.widgets.tkprogressbar import TKProgressbar
from logic.measure.measure_manager import MeasureManager
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

        # self.text_file = TextFile('default1.txt')
        # self.texts = self.text_file.get_text()

        self.proverb = Proverb()
        self.texts = self.proverb.getRandomProverb(20)

        # 사용자 인터페이스 생성
        self.create_window()
        self.max_length = 0

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
        self.max_speed_label = TKProgressbar(master=inner_frame, text="최고 속도: ", default_font=global_font, value=0,
                                           max_value=500, progress_color="#A80000")
        self.max_speed_label_frame = self.max_speed_label.create_widgets()
        self.max_speed_label_frame.pack(padx=20, pady=10, fill="x")

        self.current_speed_label = TKProgressbar(master=inner_frame, text="현재 속도: ", default_font=global_font, value=0,
                                               max_value=500, progress_color="#0000A8")
        self.current_speed_label_frame = self.current_speed_label.create_widgets()
        self.current_speed_label_frame.pack(padx=20, pady=10, fill="x")

        # 정확도 진행률 표시
        self.accuracy_label = TKProgressbar(master=inner_frame, text="정확도: ", default_font=global_font, value=0,
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
            ("총 글자수:", self.results["typed_chars"]),
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
        self.input_frame = TKInputFrame(self.master, self.on_keyrelease, self.on_text_changed, label_text="한글-2",
                                        font=global_font)
        self.input_frame.frame.pack(side="bottom", pady=(0, 10))

        self.measure_manager.startTest()
        # self.input_frame.input_entry.bind('<KeyRelease>', self.on_keyrelease)

        threading.Timer(0.5, self.refresh).start()

    def refresh(self):
        self.on_text_changed()
        threading.Timer(0.5, self.refresh).start()

    def on_text_changed(self, *args):
        text = self.input_frame.input_entry.get()
        max_length = len(self.texts[self.current_sentence_index])
        if len(text) > max_length + 1:
            self.input_frame.input_entry.delete(max_length, END)
            return

        self.update_calculate()

    # 속도 및 정확도 업데이트
    def update_calculate(self):
        original_text = self.texts[self.current_sentence_index]
        input_text = self.input_frame.input_entry.get()
        accuracy, matches, mismatches, typing_speed = self.measure_manager.calculate(original_text, input_text)

        if accuracy == None:
            return

        self.current_speed_label.update_value(typing_speed, unit="타/분")
        self.max_speed_label.update_value(self.measure_manager.max_typing_speed, unit="타/분")

        self.results["typed_chars"].configure(text=f"{matches+mismatches}타")
        self.results["correct_chars"].configure(text=f"{matches}타")
        self.results["practice_time"].configure(text=f"{int(self.measure_manager.elapsed_time)}초")
        self.results["current_speed"].configure(text=f"{typing_speed:.0f}타/분")
        self.accuracy_label.update_value(accuracy, unit="%")
        self.results["accuracy"].configure(text=f"{accuracy:.0f}%")

    # 다음 줄로 이동 가능 여부 판단
    def can_move_to_next_line(self, text):
        if self.current_sentence_index <= len(self.texts):
            typing_text_length = len(text)
            current_sentence_length = len(self.texts[self.current_sentence_index])

            print('can_move_to_next_line', typing_text_length >= current_sentence_length)
            return typing_text_length >= current_sentence_length
        return False

    # 다음 줄로 이동
    def move_to_next_line(self):
        self.current_sentence_index += 1
        if self.current_sentence_index < len(self.texts):
            # self.update_calculate()
            self.short_text_label.configure(text=self.texts[self.current_sentence_index])
            self.measure_manager.resetTest()
            self.input_frame.input_entry.delete(0, 'end')
            self.measure_manager.startTest()
        else:
            self.input_frame.input_entry.configure(state='disabled')
            self.short_text_label.configure(text="연습 완료!")

    # 정확도 체크 및 다음 줄로 이동 처리
    def check_accuracy_and_move_to_next_line(self, text):
        if self.can_move_to_next_line(text):
            self.move_to_next_line()
            return True

        return False

    def on_keyrelease(self, text, event):
        max_length = len(self.texts[self.current_sentence_index])
        if event.keysym == 'Return':
            if len(text) > max_length - 1:
                self.move_to_next_line()
                self.input_frame.input_entry.delete(self.max_length, END)

        else:
            if len(text) > max_length:
                self.move_to_next_line()
                self.input_frame.input_entry.delete(self.max_length, END)


if __name__ == "__main__":
    font_family, font_size = GlobalFont.get_font()
    tk_font = (font_family, font_size)

    root = ctk.CTk()
    root.geometry("1024x768")
    root.configure(fg_color="#AAAAAA")
    short_practice = ShortTextWindow(master=root)
    root.mainloop()
