import tkinter as tk
from tkinter import messagebox


class aplikacja:
    def __init__(self, root):
        self.root = root
        self.root.title("Harmonogram prania")

        self.osoba = 0
        self.zadanie = []
        self.osoba2 = 0

        #interfeis
        self.root.geometry("500x400")
        self.label = tk.Label(root,text="Ilość osób chętnych:")
        self.label.pack(pady=50)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=20)
        self.next_button = tk.Button(root,text="ok",command=self.ok,width=10,height=3,font=(12))
        self.next_button.pack(pady=10)

    def ok(self):
        if self.osoba == 0:
            try:
                self.osoba = int(self.entry.get()) #pobieranie wartości
                if self.osoba <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Niepoprawna ilość.")
                return

root = tk.Tk()
app = aplikacja(root)
root.mainloop()
