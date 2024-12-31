import tkinter as tk
from tkinter import messagebox


class Aplikacja:
    def __init__(self, root):
        self.root = root
        self.root.title("Harmonogram prania")

        self.osoba = 0
        self.zadania = []
        self.indeks_osoba = 0

        # Interfejs
        self.root.geometry("500x400")
        self.label = tk.Label(root, text="Ilość osób chętnych:")
        self.label.pack(pady=20)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)
        self.next_button = tk.Button(root, text="OK", command=self.ok, width=10, height=2, font=("Arial", 12))
        self.next_button.pack(pady=10)

    def ok(self):
        if self.osoba == 0:
            try:
                self.osoba = int(self.entry.get())
                if self.osoba <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Błąd", "Niepoprawna ilość. Wprowadź liczbę całkowitą większą od zera.")
                return
            self.label.config(text=f"Imię {self.indeks_osoba + 1} osoby:")
            self.entry.delete(0, tk.END)
            self.zadania = []

        elif len(self.zadania) < self.osoba:
            imie = self.entry.get().strip()
            if not imie:
                messagebox.showerror("Błąd", "Niepoprawne imię. Wprowadź imię.")
                return

            self.zadania.append({'imie': imie, 'czas': None})
            self.indeks_osoba += 1

            if self.indeks_osoba < self.osoba:
                self.label.config(text=f"Imię {self.indeks_osoba + 1} osoby:")
                self.entry.delete(0, tk.END)
            else:
                self.label.config(text=f"Czas prania dla {self.zadania[0]['imie']} (min):")
                self.entry.delete(0, tk.END)
                self.indeks_osoba = 0  # Resetujemy
                self.next_button.config(command=self.czas_prania)

    def czas_prania(self):
        try:
            czas = int(self.entry.get())
            if czas <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny czas. Wprowadź liczbę całkowitą większą od zera.")
            return

        self.zadania[self.indeks_osoba]['czas'] = czas
        self.entry.delete(0, tk.END)
        self.indeks_osoba += 1

        if self.indeks_osoba < self.osoba:
            self.label.config(text=f"Czas prania dla {self.zadania[self.indeks_osoba]['imie']} (min):")
        else:
            self.sjf()


root = tk.Tk()
app = Aplikacja(root)
root.mainloop()
