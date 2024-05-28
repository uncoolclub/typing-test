import time

class MeasureManager:
    def __init__(self):
        self.start_time = None
        self.is_finished = False
        self.max_cpm = 0

    def resetMeasure(self):
        self.start_time = None
        self.is_finished = False

    def updateSpeed(self):
        if self.start_time is not None and not self.is_finished:
            elapsed_time = time.time() - self.start_time

            if elapsed_time > 1:  # 최소 1초 이상 지나야 타이핑 속도를 계산
                num_chars = len(self.input_field.text())
                cpm = (num_chars / elapsed_time) * 60

                # self.speed_label.setText(f"타이핑 속도: {cpm:.0f} 타/분 (CPM)")

                if cpm < 1000:  # 비정상적으로 높은 속도를 필터링
                    if self.max_cpm < cpm:
                        self.max_cpm = cpm

                # self.max_speed_label.setText(f"최대 타이핑 속도 : {self.max_cpm:.0f} 타/분 (CPM)")

            return { 'cpm': self.cpm, 'max_cpm': self.max_cpm }
