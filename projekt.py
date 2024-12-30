import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Aplikacja:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Harmonogram prania")
        self.current_step = 0
        self.tasks = []