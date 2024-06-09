import tkinter as tk
from tkinter import ttk
from ui.widgets.tkdialog import TKDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.font_manager as fm
import random
import os.path
from config import FONT_LOCATION


class StatisticsDialog:
    def __init__(self, master, user):
        self.master = master
        self.user = user
        self.data = self.get_date()
        self.create_dialog(master)

    def create_dialog(self, master):
        def show_graph(data, frame, dialog):
            self.canvas = None

            def on_select(event):
                # 캔버스 그리기 전에 기존 캔버스 지우기
                if self.canvas is not None:
                    self.canvas.destroy()
                value = combobox.get()
                self.canvas = PlotCanvas(frame, data, value)

            combobox = ttk.Combobox(frame, values=list(map(str, data.keys())))
            combobox.pack(pady=10)
            combobox.bind("<<ComboboxSelected>>", on_select)

        dialog = TKDialog(master, master, title="통계", content_frame_builder=lambda frame, dialog: show_graph(data=self.data, frame=frame, dialog=dialog))
        # lamda로
        dialog.wait_window()

    def get_date(self): # user 데이터 그래프로 표현하기 쉽게 보정
        data = self.user.getRecord()
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
    def __init__(self, master, data, key):
        super().__init__()
        self.canvas_frame = ttk.Frame(master)
        self.canvas_frame.pack(pady=20)

        self.master = master
        self.data = data
        self.key = key

        self.plot(self.data, self.key)

    def plot(self, data, key):
        DEFAULT_FONT_PATH = os.path.join(FONT_LOCATION, 'DOSMyungjo.ttf')
        font_prop = fm.FontProperties(fname=DEFAULT_FONT_PATH)

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.figure.patch.set_facecolor('#aaaaaa')
        self.ax = self.figure.add_subplot()
        self.ax.set_facecolor('#aaaaaa')

        self.ax.plot(data[key]['times'], data[key]['avg_typist'], marker='o', linestyle='-', color=self.get_random_color())
        self.ax.set_xlabel('시간', fontproperties=font_prop, fontsize=12)
        self.ax.set_ylabel('평균 타수', fontproperties=font_prop, fontsize=12)
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

