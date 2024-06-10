import os
import time
import threading
import tkinter

import customtkinter as ctk
from tkinter import Toplevel, Frame, RAISED, SUNKEN, LabelFrame, Label, Entry, StringVar
from PIL import Image, ImageTk

from logic.file.textFile import TextFile
from ui.font_loader import FontLoader
from ui.widgets.label import Label as CustomLabel
from ui.widgets.progressbar import Progressbar
from logic.measure.measure_manager import MeasureManager
from ui.widgets.timer import Timer


class ShortTextWindow:
    def __init__(self, master, default_font):
        self.master = master
        self.default_font = default_font
        self.measure_manager = MeasureManager()
        self.current_sentence_index = 0
        self.text_file = TextFile('default1.txt')
        self.texts = self.text_file.getText()
        self.input_text_var = StringVar()
        self.input_text_var.trace_add("write", self.on_text_changed)
        self.create_window()
        self.max_length = 0

    def create_window(self):
        new_window = Toplevel(self.master)
        new_window.title("짧은글 연습")
        new_window.geometry("1024x768")
        new_window.configure(bg="#AAAAAA")

        frame = Frame(new_window, relief=RAISED, bd=2, bg="#AAAAAA")
        frame.pack(side="top", fill="both", padx=30, pady=20)

        icon_path = "../../../resource/images/ic_keyboard.png"
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)

        title_label = CustomLabel(master=frame, text="짧은글 연습", default_font=self.default_font).create_label(
            height=30, fg_color="#000088", anchor="w", text_color="white", image=icon_photo, compound="left", padx=10)
        title_label.pack(side="top", fill='x', padx=10, pady=10)

        short_text_frame = Frame(frame, relief=SUNKEN, bd=2, bg="#AAAAAA")
        short_text_frame.pack(side="top", fill="both", padx=10)
        self.short_text_label = CustomLabel(master=short_text_frame, text=self.texts[self.current_sentence_index],
                                            default_font=self.default_font).create_label(height=60, anchor="w")
        self.short_text_label.pack(side="top", fill="x", padx=15, pady=20)

        progress_frame = LabelFrame(frame, text="  빠르기·정확도  ", relief=SUNKEN, bd=2, bg="#AAAAAA",
                                    fg="black", font=self.default_font, background="#AAAAAA", labelanchor="n")
        progress_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        inner_frame = Frame(progress_frame, bg="#AAAAAA")
        inner_frame.pack(fill="both", pady=30)

        self.max_speed_label = Progressbar(master=inner_frame, text="최고 속도: ", default_font=self.default_font, value=0,
                                           max_value=500, progress_color="#A80000")
        self.max_speed_label_frame = self.max_speed_label.create_widgets()
        self.max_speed_label_frame.pack(padx=20, pady=10, fill="x")

        self.current_speed_label = Progressbar(master=inner_frame, text="현재 속도: ", default_font=self.default_font, value=0,
                                               max_value=500, progress_color="#0000A8")
        self.current_speed_label_frame = self.current_speed_label.create_widgets()
        self.current_speed_label_frame.pack(padx=20, pady=10, fill="x")

        self.accuracy_label = Progressbar(master=inner_frame, text="정확도: ", default_font=self.default_font, value=0,
                                          max_value=100, progress_color="#00A8A8")
        self.accuracy_label_frame = self.accuracy_label.create_widgets()
        self.accuracy_label_frame.pack(padx=20, pady=10, fill="x")

        result_frame = LabelFrame(frame, text="  결과  ", relief=SUNKEN, bd=2, bg="#AAAAAA", fg="black",
                                  font=self.default_font, background="#AAAAAA", labelanchor="n")
        result_frame.pack(side="right", fill="both", padx=10, pady=10)

        self.results = {
            "typed_chars": Label(result_frame, text="0타", font=self.default_font, bg="#AAAAAA", anchor="e",
                                 justify="right"),
            "correct_chars": Label(result_frame, text="0타", font=self.default_font, bg="#AAAAAA", anchor="e",
                                   justify="right"),
            "practice_time": Label(result_frame, text="0.0초", font=self.default_font, bg="#AAAAAA", anchor="e",
                                   justify="right"),
            "current_speed": Label(result_frame, text="0타/분", font=self.default_font, bg="#AAAAAA", anchor="e",
                                   justify="right"),
            "accuracy": Label(result_frame, text="0%", font=self.default_font, bg="#AAAAAA", anchor="e",
                              justify="right")
        }

        results_labels = [
            ("쓰인 글자수:", self.results["typed_chars"]),
            ("정확한 글자수:", self.results["correct_chars"]),
            ("연습 시간:", self.results["practice_time"]),
            ("현재 속도:", self.results["current_speed"]),
            ("정확도:", self.results["accuracy"]),
        ]

        for row, (label_text, result_label) in enumerate(results_labels):
            Label(result_frame, text=label_text, font=self.default_font, bg="#AAAAAA", anchor="w", justify="left").grid(
                row=row, column=0, sticky="w", padx=20, pady=5)
            result_label.grid(row=row, column=1, sticky="e", padx=20, pady=5)

        bottom_frame = Frame(new_window, relief=RAISED, bd=2, bg="#AAAAAA")
        bottom_frame.pack(side="bottom", fill="x", padx=10, pady=5)

        input_label = CustomLabel(master=bottom_frame, text="한글-2", default_font=self.default_font).create_label(
            anchor="w", fg_color="#AAAAAA")
        input_label.pack(side="left", padx=5, pady=5)

        self.input_entry = Entry(bottom_frame, textvariable=self.input_text_var, font=self.default_font, relief="flat", bd=0, bg="white",
                                 insertbackground="black", selectbackground="black", selectforeground="white")
        self.input_entry.pack(side="left", fill="x", expand=True, padx=5)
        # self.input_entry.bind("<Return>", self.on_enter)

        self.timer_label = Timer(master=bottom_frame, text="00:00", font=self.default_font, bg="#AAAAAA", anchor="e")
        self.timer_label.pack(side="right", padx=5, pady=5)
        self.timer_label.start()

        self.measure_manager.startTest(self.texts[self.current_sentence_index])
        self.input_entry.bind('<KeyRelease>', self.limit_text_length)

        threading.Timer(0.5, self.refresh).start()

    def refresh(self):
        self.update_speed_and_accuracy()
        threading.Timer(0.5, self.refresh).start()

    def on_enter(self, event):
        text = self.input_entry.get()
        self.check_accuracy_and_move_to_next_line(text)
        return "break"

    def on_text_changed(self, *args):
        text = self.input_entry.get()
        max_length = len(self.measure_manager.sentence)
        if len(text) > max_length + 1:
            self.input_entry.delete(max_length, tkinter.END)

        self.measure_manager.onTextChanged(text)
        self.update_speed_and_accuracy()

    def update_speed_and_accuracy(self):
        cpm, max_cpm = self.measure_manager.updateSpeed()
        self.current_speed_label.update_value(cpm, unit="타/분")
        self.max_speed_label.update_value(max_cpm, unit="타/분")

        self.results["typed_chars"].configure(text=f"{self.measure_manager.num_chars}타")
        mismatched_characters = self.measure_manager.total_mismatched_characters + self.measure_manager.mismatched_characters
        if(mismatched_characters < 0):
            mismatched_characters = 0

        self.results["correct_chars"].configure(text=f"{self.measure_manager.num_chars - mismatched_characters}타")
        self.results["practice_time"].configure(text=f"{int(self.measure_manager.elapsed_time)}초")
        self.results["current_speed"].configure(text=f"{cpm:.0f}타/분")
        # self.results["typed_chars"].configure(text=f"{len(self.input_entry.get())}타")

        accuracy = self.measure_manager.calculate_overall_accuracy([self.input_entry], [self.texts[self.current_sentence_index]])
        self.accuracy_label.update_value(accuracy, unit="%")
        self.results["accuracy"].configure(text=f"{accuracy:.2f}%")

    def can_move_to_next_line(self, text):
        if self.current_sentence_index <= len(self.texts):
            typing_text_length = len(text)
            current_sentence_length = len(self.texts[self.current_sentence_index])

            print('can_move_to_next_line', typing_text_length >= current_sentence_length)
            return typing_text_length >= current_sentence_length
        return False

    def move_to_next_line(self):
        self.current_sentence_index += 1
        if self.current_sentence_index < len(self.texts):
            # self.update_speed_and_accuracy()
            self.short_text_label.configure(text=self.texts[self.current_sentence_index])

            self.measure_manager.nextTest(self.texts[self.current_sentence_index])
            self.input_entry.delete(0, 'end')
        else:
            self.input_entry.configure(state='disabled')
            self.short_text_label.configure(text="연습 완료!")

    def check_accuracy_and_move_to_next_line(self, text):
        if self.can_move_to_next_line(text):
            self.move_to_next_line()

    def limit_text_length(self, event):
        current_text = self.input_entry.get()
        max_length = len(self.measure_manager.sentence)
        if event.keysym == 'Return':
            if len(current_text)> max_length - 1:
                self.move_to_next_line()
                self.input_entry.delete(self.max_length, tkinter.END)

        else:
            if len(current_text) > max_length:
                self.move_to_next_line()
                self.input_entry.delete(self.max_length, tkinter.END)

if __name__ == "__main__":
    font_path = os.path.abspath("../../../resource/fonts/DOSMyungjo.ttf")
    font_family, font_size = FontLoader.load_custom_font(font_path, size=22)
    tk_font = (font_family, font_size)

    root = ctk.CTk()
    root.title("메인 윈도우")
    root.geometry("1024x768")
    short_practice = ShortTextWindow(master=root, default_font=tk_font)
    root.mainloop()
