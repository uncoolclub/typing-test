import tkinter as tk
from tkinter import ttk, filedialog
from utils.center_window import center_window

CUSTOM_LIST_BOX = list()

class FileLoadWindow:
    def __init__(self, master):
        # 기본 창 설정
        self.master = master
        self.master.title("파일 불러오기")
        self.master.geometry("300x300")
        self.master.configure(bg="#AAAAAA")

        # 윈도우 위치를 화면 중앙으로 설정
        center_window(self.master)

        self.data = {}
        self.canvas_frame = None
        self.create_dialog()

    def create_dialog(self):
        self.list_combobox = None
        self.measure_combobox = None

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
            CUSTOM_LIST_BOX.append({"label": file_name, "file_name": file_name, "file_path": file_path})
            self.update_file_listbox()

    def update_file_listbox(self):
        self.file_listbox.delete(0, tk.END)  # 기존 목록 삭제
        for file_info in CUSTOM_LIST_BOX:
            self.file_listbox.insert(tk.END, file_info["label"])

    def go_back(self):
        # 메인 화면으로 돌아가는 기능 구현
        # 이 부분에 메인 화면을 호출하거나 메인 화면으로 돌아가는 로직을 추가하세요
        print("돌아가기 버튼 클릭")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileLoadWindow(master=root)
    root.mainloop()
