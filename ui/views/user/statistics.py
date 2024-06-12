import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.font_manager as fm
import random
import os.path
from config import FONT_LOCATION
from utils.user import User
from utils.manager_json import read_json
from utils.center_window import center_window

COMBO_DATA_VARIABLE={
    "평균타수": "avg_typist",
    "최고타수": "best_typist",
    "정확도": "accuracy"
}


class StatisticsWindow:
    def __init__(self, master):
        # 기본 창 설정
        self.master = master
        self.master.title("통계")
        self.master.geometry("1024x768")
        self.master.configure(bg="#AAAAAA")

        # 윈도우 위치를 화면 중앙으로 설정
        center_window(self.master)

        self.data = self.get_date()
        self.canvas_frame = None
        self.create_dialog()

    def create_dialog(self):
        self.list_combobox = None
        self.measure_combobox = None
        def show_graph(data, frame):
            combobox_frame = ttk.Frame(frame)
            combobox_frame.pack(pady=10)

            # 글별 콤보박스
            self.list_combobox = ttk.Combobox(combobox_frame, values=list(map(str, data.keys())))
            self.list_combobox.pack(side=tk.LEFT, pady=10)
            self.list_combobox.bind("<<ComboboxSelected>>", lambda event: on_select())
            on_select()

            if len(list(map(str, data.keys()))) > 0:
                # 측정된 데이터별 콤보박스
                self.measure_combobox = ttk.Combobox(combobox_frame, values=list(map(str, COMBO_DATA_VARIABLE.keys())))
                self.measure_combobox.pack(side=tk.LEFT, pady=10)
                self.measure_combobox.bind("<<ComboboxSelected>>", lambda event: on_select())
                on_select()

        def on_select():
            if self.canvas_frame is not None:
                self.canvas_frame.destroy()

            # 두 개의 콤보박스가 모두 선택 시, 알맞는 그래프 노출
            if (self.list_combobox is not None and self.measure_combobox is not None
                    and self.list_combobox.get() and self.measure_combobox.get()):
                list_name = self.list_combobox.get()
                measure = self.measure_combobox.get()
                self.canvas_frame = PlotCanvas(self.master, self.data, list_name, measure)

        show_graph(self.data, self.master)

    def get_date(self): # user 데이터 그래프로 표현하기 쉽게 보정
        data = read_json(User().get_nickname()) # 저장된 데이터 읽어오기
        result = {}

        for item in data.keys():
            avg_typist = [] # 평균 타수
            best_typist = [] # 최고 타수
            accuracy = [] # 정확도
            times = [] # 시간
            for v in data[item]:
                avg_typist.append(v["평균타수"])
                best_typist.append(v["최고타수"])
                accuracy.append(v["정확도"])
                times.append(v["날짜"])
            result[item] = {
                "avg_typist": avg_typist,
                "best_typist": best_typist,
                "accuracy": accuracy,
                "times": times
            }

        return result


class PlotCanvas(FigureCanvasTkAgg):
    def __init__(self, master, data, list_key, measure_key):
        super().__init__()
        self.canvas_frame = ttk.Frame(master)
        self.canvas_frame.pack(pady=20)

        self.master = master
        self.data = data
        self.list_key = list_key
        self.measure_key = measure_key

        self.plot(self.data, self.list_key, self.measure_key)

    def plot(self, data, list_key, measure_key):
        DEFAULT_FONT_PATH = os.path.join(FONT_LOCATION, 'DOSMyungjo.ttf')
        font_prop = fm.FontProperties(fname=DEFAULT_FONT_PATH)

        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.figure.patch.set_facecolor('#aaaaaa')
        self.ax = self.figure.add_subplot()
        self.ax.set_facecolor('#aaaaaa')

        self.ax.plot(data[list_key]['times'], data[list_key][COMBO_DATA_VARIABLE[measure_key]], marker='o', linestyle='-', color=self.get_random_color())
        self.ax.set_xlabel('시간', fontproperties=font_prop, fontsize=12)
        self.ax.set_ylabel(measure_key, fontproperties=font_prop, fontsize=12)
        self.ax.set_title('통계', fontproperties=font_prop, fontsize=17)
        self.ax.grid(True)
        self.ax.tick_params(axis='x', rotation=20)
        self.figure.tight_layout()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def get_random_color(self):
        return random.random(), random.random(), random.random()

    def destroy(self):
        self.canvas_frame.destroy()
