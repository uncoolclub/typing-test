class Measure:
    def accuracy(self, origin_text, input_text):
        if len(origin_text) != len(input_text):
            raise ValueError("The lengths of the original text and input text must be the same.")
        
        correct_count = 0
        for index, origin in enumerate(origin_text):
            if origin == input_text[index]:
                correct_count += 1
        
        accuracy_percentage = (correct_count / len(origin_text)) * 100
        return accuracy_percentage

# 예시 사용
measure = Measure()
accuracy = measure.accuracy("aaaa", "aabb")

print(f"정확도: {accuracy:.2f}%")

import tkinter as tk
from tkinter import ttk
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.start_time = None
        self.total_characters = 0

        self.label = ttk.Label(root, text="Start typing:")
        self.label.pack()

        self.text_area = tk.Text(root, width=50, height=10)
        self.text_area.pack()
        self.text_area.bind("<KeyRelease>", self.on_key_release)

        self.cpm_label = ttk.Label(root, text="CPM: 0")
        self.cpm_label.pack()

        self.wpm_label = ttk.Label(root, text="WPM: 0")
        self.wpm_label.pack()

        self.start_button = ttk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack()

    def start_test(self):
        self.start_time = time.time()
        self.total_characters = 0
        self.text_area.delete(1.0, tk.END)
        self.cpm_label.config(text="CPM: 0")
        self.wpm_label.config(text="WPM: 0")
        self.text_area.focus()

    def on_key_release(self, event):
        if not self.start_time:
            return

        input_text = self.text_area.get(1.0, tk.END).strip()
        self.total_characters = len(input_text)

        elapsed_time = time.time() - self.start_time
        elapsed_minutes = elapsed_time / 60

        if elapsed_minutes > 0:
            cpm = self.total_characters / elapsed_minutes
            wpm = cpm / 5
        else:
            cpm = 0
            wpm = 0

        self.cpm_label.config(text=f"CPM: {cpm:.2f}")
        self.wpm_label.config(text=f"WPM: {wpm:.2f}")

# 애플리케이션 실행
root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()
