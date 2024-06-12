import tkinter as tk

from ui.widgets.tkdialog import TKDialog
from ui.widgets.tklabel import TKLabel


class ResultsWindow:
    def __init__(self, master, measure):
        self.master = master
        self.measure = measure
        self.create_dialog(master)  # 다이얼로그 생성 함수 호출

    def create_dialog(self, master):
        def build_results_content(frame, dialog):
            # padding 조정을 위한 컨테이너 프레임 사용
            container = tk.Frame(frame, bg='#AAAAAA')
            container.pack(fill='x', expand=True, padx=10, pady=10)  # x축으로 채우고 확장

            # 측정된 시간을 분과 초로 변환
            minutes, seconds = divmod(int(self.measure.elapsed_time), 60)

            # 라벨에 표시될 정보들
            labels_info = {
                "쓰인 글자 수:": f"{self.measure.num_chars} 개",
                "정확한 글자 수:": f"{self.measure.correct_characters} 개",
                "연습 시간:": f"{minutes:02}:{seconds:02} 초",  # MM:SS 형태로 표시
                "최고 속도:": f"{self.measure.max_cpm} 타",
                "정확도:": f"{self.measure.overall_accuracy} %",
            }

            # 정보를 표시할 라벨들을 컨테이너 안에 생성
            for label, value in labels_info.items():
                label_container = tk.Frame(container, bg='#AAAAAA')
                label_container.pack(fill='x', expand=True, pady=10)  # 각 라벨 컨테이너를 x축으로 채움 및 확장

                # 제목과 값에 대해 별도의 라벨 생성하여 더 나은 정렬 제어
                label_text = TKLabel(label_container, text=label, font_size=20).create_label()
                value_text = TKLabel(label_container, text=value, font_size=20).create_label()
                label_text.pack(side="left")
                value_text.pack(side="right")

        # 다이얼로그 설정 및 표시
        dialog = TKDialog(master, master, title="결과", window_size="480x480",
                          content_frame_builder=build_results_content)
        dialog.wait_window()  # 다이얼로그가 닫힐 때까지 대기
