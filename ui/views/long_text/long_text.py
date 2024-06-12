from ui.views.results.results import ResultsWindow
from utils.text_file import TextFile
import customtkinter as ctk
from tkinter import Label
from ui.global_font import GlobalFont
from ui.window.default_window import DefaultWindow
from ui.widgets.tkinputframe import TKInputFrame
from logic.measure.measure_manager import MeasureManager
from utils.user import User
from utils.manager_json import save_json


class LongTextWindow:
    def __init__(self, master, label, file_name):
        self.master = master
        self.label = label
        self.file_name = file_name
        self.current_page = 0  # 현재 페이지를 추적하기 위한 변수
        self.lines_per_page = 5  # 한 페이지에 표시할 텍스트 줄 수
        self.current_label_index = 0  # 현재 레이블 인덱스를 추적하기 위한 변수
        self.results_window_open = False
        self.text_file = TextFile(self.file_name)  # 텍스트 파일 로드
        self.text_content = self.text_file.get_text()  # 텍스트 파일에서 내용 가져오기
        self.measure_manager = MeasureManager()
        self.create_window()

        # 쓰인글자 self.measure_manager.num_chars = 0
        # 정확한 글자 self.measure_manager.correct_characters = 0
        # 연습 시간 self.measure_manager.elapsed_time
        # 정확도 self.measure_manager.overall_accuracy
        # 최고속도 self.measure_manager.max_cpm

    def create_window(self):
        # 기본 창 설정
        title = f"긴글 연습 - 『{self.label}』"
        custom_window = DefaultWindow(root=self.master, master=self.master, title=title, window_size="1024x900")
        self.frame = custom_window.get_frame()
        self.font = GlobalFont.get_global_font(font_size=18, use_type="ctk")  # 전역 폰트 설정

        self.labels = []  # 레이블 저장을 위한 리스트 초기화
        self.display_text_with_labels()  # 텍스트와 레이블 표시

        self.input_frame = TKInputFrame(self.master, self.on_keyrelease, self.on_text_changed, label_text="한글-2",
                                        font=self.font)
        self.input_frame.frame.pack(side="bottom", pady=(0, 10))

    def display_text_with_labels(self):
        # 현재 페이지에 표시할 텍스트 계산
        start_index = self.current_page * self.lines_per_page
        end_index = start_index + self.lines_per_page
        self.page_text = self.text_content[start_index:end_index]

        if not self.labels:
            # 레이블을 한 번만 생성
            self.content_frame = ctk.CTkFrame(self.frame, fg_color="#AAAAAA")
            self.content_frame.pack(pady=10, padx=10, fill='both', expand=True)

            for _ in range(self.lines_per_page):
                # 텍스트 내용 표시
                text_label = Label(self.content_frame, text="", bg="#AAAAAA", font=self.font, justify='left',
                                   anchor='w')
                text_label.pack(pady=5, padx=10, fill='x')

                # 사용자 입력 레이블 자리 표시자
                user_input_label = Label(self.content_frame, text="", bg="#AAAAAA", font=self.font, justify='left',
                                         anchor='w')
                user_input_label.pack(pady=(0, 10), padx=10, fill='x')
                self.labels.append((text_label, user_input_label))

        for i, (text_label, user_input_label) in enumerate(self.labels):
            if i < len(self.page_text):
                text_label.config(text=self.page_text[i])
                user_input_label.config(text="", fg="black")  # 기본 글자색으로 초기화
            else:
                text_label.config(text="")
                user_input_label.config(text="", fg="black")  # 기본 글자색으로 초기화

        if self.current_page == 0:
            self.measure_manager.startTest(self.labels[self.current_label_index][0].cget("text"))
        else:
            self.measure_manager.nextTest(self.labels[self.current_label_index][0].cget("text"))

    def next_page(self):
        if self.current_page + 1 < len(self.text_content) // self.lines_per_page:
            self.current_page += 1
            self.current_label_index = 0  # 새 페이지 시작 전 레이블 인덱스 초기화
            self.display_text_with_labels()
        else:
            self.display_results()

    def display_results(self):
        if not self.results_window_open:
            self.results_window_open = True
            self.input_frame.disable_input()
            self.input_frame.stop_timer()

            # 결과 저장
            save_json(User().get_nickname(), self.label, self.measure_manager)

            self.results_window = ResultsWindow(self.master, measure=self.measure_manager)

    def on_results_window_closed(self):
        self.results_window_open = False

    def on_keyrelease(self, text, event):
        # 현재 페이지에 더 이상 텍스트가 없으면 다음 페이지로 이동
        if len(self.page_text) <= self.current_label_index or self.current_label_index >= self.lines_per_page:
            self.next_page()
            return True

        if len(text) < len(self.page_text[self.current_label_index]):
            # 입력된 텍스트가 부족할 때는 기본 동작을 중단
            return False

        if self.current_label_index < len(self.page_text):
            # 텍스트와 글자색을 한 번에 설정
            self.labels[self.current_label_index][1].config(text=text, fg="#666666")
            self.current_label_index += 1

            if self.current_label_index >= self.lines_per_page:
                # 현재 페이지의 모든 텍스트가 입력되면 다음 페이지로 이동
                self.next_page()
                return True

            # 다음 텍스트의 범위 확인
            if self.current_label_index < len(self.page_text):  
                self.measure_manager.nextTest(self.labels[self.current_label_index][0].cget("text"))

        return True

    def on_text_changed(self, text):
        # 입력 텍스트가 변경될 때 호출
        print(self.labels[self.current_label_index][0].cget("text"))
        print(self.labels[self.current_label_index][1].cget("text"))

        if len(self.page_text) <= self.current_label_index:
            self.next_page()
            return True
            # 텍스트와 글자색을 한 번에 설정

        if self.current_label_index < len(self.page_text):
            self.labels[self.current_label_index][1].config(text=text)

        self.measure_manager.onTextChanged(text)
        cpm, max_cpm = self.measure_manager.updateSpeed()
        print(cpm, max_cpm)
        self.measure_manager.calculate_overall_accuracy([self.input_frame.input_entry],
                                                            [self.labels[self.current_label_index][1].cget("text")])
