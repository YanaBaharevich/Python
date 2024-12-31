import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


class aplikacja:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Harmonogram prania")
        self.current_step = 0
        self.tasks = []

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = aplikacja()
    app.run()
