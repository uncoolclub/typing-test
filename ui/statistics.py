import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
import random


class Statistic(QMainWindow):
    def __init__(self, data = {}):
        super().__init__()
        print(data)
        self.data = data
        self.manufactureData()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('통계')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        m = PlotCanvas(self, width=5, height=4)
        layout.addWidget(m)

        self.show()

    def manufactureData(self):
        obj = {}
        for key in self.data.keys():
            scores = []
            times = []
            for item in self.data[key]:
                scores.append(item["평균타수"])
                times.append(item["날짜"])
            obj[key] = {
                'score': scores,
                'time': times
            }
        self.data = obj


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)
        self.data = parent.data
        self.plot()

    def plot(self):
        plt.rcParams['font.family'] = 'AppleGothic'
        plt.rc('font', family='AppleGothic')
        print(plt.rcParams['font.family'])

        # 그래프 그리기
        for key in self.data.keys():
            self.ax.plot(self.data[key]['time'], self.data[key]['score'], label=key, marker='o', linestyle='-', color=self.get_random_color())

        self.ax.set_xlabel('시간')
        self.ax.set_ylabel('평균 타수')
        self.ax.set_title('타수 통계')
        self.ax.grid(True)
        self.ax.legend()
        self.ax.tick_params(axis='x', rotation=45)
        self.figure.tight_layout()

    def get_random_color(self):
        return (random.random(), random.random(), random.random())
