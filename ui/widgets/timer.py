import tkinter as tk


class Timer(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.time_elapsed = 0
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.time_elapsed = 0
        self.config(text="00:00")

    def update_timer(self):
        if self.running:
            self.time_elapsed += 1
            minutes, seconds = divmod(self.time_elapsed, 60)
            self.config(text=f"{minutes:02}:{seconds:02}")
            self.after(1000, self.update_timer)
