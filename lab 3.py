# Zadanie 1 - Z wykorzystaniem OOP zaproponuj implementację Employees System Project

class Employee:
    def __init__(self, imie, nazwisko, wiek, wynagrodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = int(wiek)
        self.wynagrodzenie = float(wynagrodzenie)
    def __str__(self):
        return f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, Wiek: {self.wiek}, Wynagrodzenie: {self.wynagrodzenie}"

class EmployeesManager:
    def __init__(self):
        self.pracownicy = []
    def dodaj(self, pracownik):
        self.pracownicy.append(pracownik)
    def wyswietl(self):
        for pracownik in self.pracownicy:
            print(pracownik)
    def znalez(self, nazwisko):
        for pracownik in self.pracownicy:
            if pracownik.nazwisko == nazwisko:
                return pracownik
        return None
    def aktualizacja(self, nazwisko, nowe_wynagrodzenie):
        pracownik = self.znalez(nazwisko)
        if pracownik:
            pracownik.wynagrodzenie = float(nowe_wynagrodzenie)
            print(f"Wynagrodzenie dla {nazwisko} zaktualizowane do {nowe_wynagrodzenie}.")
        else:
            print(f"Pracownik {nazwisko} nie znaleziony.")
    def delete(self, min_wiek, max_wiek):
        self.pracownicy = [pracownik for pracownik in self.pracownicy if not (min_wiek <= pracownik.wiek <= max_wiek)]

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()
    def interfejs(self):
        while True:
            print("\nWybierz opcję:")
            print("1: Dodawanie nowych pracowników")
            print("2: Wyświetlenie listy istniejących pracowników")
            print("3: Usuwanie pracowników na podstawie przedziału wiekowego")
            print("4: Aktualizacja wynagrodzeń pracowników według nazwiska")
            print("5: Zamknięcie")
            wybor = input("Wybór: ")

            if wybor == "1":
                imie = input("Imię: ")
                nazwisko = input("Nazwisko: ")
                wiek = input("Wiek: ")
                wynagrodzenie = input("Wynagrodzenie: ")
                nowy_pracownik = Employee(imie, nazwisko, wiek, wynagrodzenie)
                self.manager.dodaj(nowy_pracownik)
            elif wybor == "2":
                self.manager.wyswietl()
            elif wybor == "3":
                min_wiek = int(input("Podaj minimalny wiek: "))
                max_wiek = int(input("Podaj maksymalny wiek: "))
                self.manager.delete(min_wiek, max_wiek)
            elif wybor == "4":
                nazwisko = input("Podaj nazwisko pracownika: ")
                nowe_wynagrodzenie = input("Podaj nowe wynagrodzenie: ")
                self.manager.aktualizacja(nazwisko, nowe_wynagrodzenie)
            elif wybor == "5":
                print("Zamknięcie programu.")
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")
frontend = FrontendManager()
frontend.interfejs()
