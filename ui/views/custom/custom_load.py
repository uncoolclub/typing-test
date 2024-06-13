import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, filedialog

from utils.center_window import center_window
from utils.text_file import TextFile


class FileLoadWindow:
    def __init__(self, master):
        # 기본 창 설정
        self.master = master
        self.master.title("파일 불러오기")
        self.master.geometry("300x300")
        self.master.configure(bg="#AAAAAA")

        # 윈도우 위치를 화면 중앙으로 설정
        center_window(self.master)

        self.canvas_frame = None
        self.create_dialog()

    def create_dialog(self):
        # 파일 다이얼로그 버튼과 긴글 연습 라벨 프레임 생성
        self.dialog_frame = ttk.Frame(self.master)
        self.dialog_frame.pack(pady=10)

        # 긴글 연습 라벨 추가
        self.long_text_label = ttk.Label(self.dialog_frame, text="긴글 연습 추가하기")
        self.long_text_label.pack(side=tk.LEFT, padx=5)

        # 파일 다이얼로그 버튼 추가
        self.file_dialog_button = ttk.Button(self.dialog_frame, text="파일 열기", command=self.open_file_dialog)
        self.file_dialog_button.pack(side=tk.LEFT, padx=5)

        # 파일 목록을 표시할 리스트박스
        self.file_listbox = tk.Listbox(self.master)
        self.file_listbox.pack(pady=10, padx=5, fill=tk.BOTH, expand=True)

        # 돌아가는 버튼 추가
        self.back_button = ttk.Button(self.master, text="돌아가기", command=self.go_back)
        self.back_button.pack(pady=10)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="파일 선택",
            filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            file_name = file_path.split("/")[-1]  # 파일 경로에서 파일 이름 추출
            print(f"Selected file: {file_name} \n path : {file_path}")  # 선택된 파일명 출력
            self.save_custom_file(file_path, file_name)

    def save_custom_file(self, file_path, file_name):
        path_arr = file_path.split("/")
        remove_file_name = "/".join(path_arr[:-1])
        text_file = TextFile(file_name, remove_file_name)
        text_content = text_file.get_text()
        text_file.save_text_file("\n".join(text_content))

    def go_back(self):
        self.master.destroy()
        new_window = ctk.CTk()
        from ui.views.main.main import Main
        Main(new_window)
