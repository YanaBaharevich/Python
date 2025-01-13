# Zadanie 1 - Z wykorzystaniem OOP zaproponuj implementację Employees System Project + Zadanie 2

import json

class Employee:
    def __init__(self, imie, nazwisko, wiek, wynagrodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = int(wiek)
        self.wynagrodzenie = float(wynagrodzenie)
    def __str__(self):
        return f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, Wiek: {self.wiek}, Wynagrodzenie: {self.wynagrodzenie}"
    def to_dict(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "wiek": self.wiek,
            "wynagrodzenie": self.wynagrodzenie
        }

class EmployeesManager:
    def __init__(self,plik="pracownicy.json"):
        self.plik = plik
        self.pracownicy = self.wczytaj_z_pliku()
    def wczytaj_z_pliku(self):
        try:
            with open(self.plik,"r") as f:
                dane = json.load(f)
                return [self.utworz_pracownika(p) for p in dane]
        except FileNotFoundError:
            return []

    def zapisz_do_pliku(self):
        with open(self.plik, "w") as f:
            json.dump([p.to_dict() for p in self.pracownicy], f, indent=4)
    def dodaj(self, pracownik):
        self.pracownicy.append(pracownik)
        self.zapisz_do_pliku()
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
            self.zapisz_do_pliku()
            print(f"Wynagrodzenie dla {nazwisko} zaktualizowane do {nowe_wynagrodzenie}.")
        else:
            print(f"Pracownik {nazwisko} nie znaleziony.")

    def delete(self, min_wiek, max_wiek):
        self.pracownicy = [p for p in self.pracownicy if not (min_wiek <= p.wiek <= max_wiek)]
        self.zapisz_do_pliku()
    def utworz_pracownika(self, dane):
        return Employee(dane["imie"], dane["nazwisko"], dane["wiek"], dane["wynagrodzenie"])

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def logowanie(self):
        print("Logowanie do systemu:")
        for _ in range(3):
            login = input("Login: ")
            haslo = input("Hasło: ")
            if login == "admin" and haslo == "admin":
                print("Zalogowano pomyślnie.")
                return True
            else:
                print("Niepoprawne dane logowania. Spróbuj ponownie.")
        print("Przekroczono liczbę prób logowania.")
        return False

    def walidacja_danych(self, imie, nazwisko, wiek, wynagrodzenie):
        if not imie.isalpha():
            print("Imię musi zawierać tylko litery.")
            return False
        if not nazwisko.isalpha():
            print("Nazwisko musi zawierać tylko litery.")
            return False
        if not wiek.isdigit() or int(wiek) <= 0:
            print("Wiek musi być liczbą dodatnią.")
            return False
        try:
            float(wynagrodzenie)
        except ValueError:
            print("Wynagrodzenie musi być liczbą.")
            return False
        return True
    def interfejs(self):
        if not self.logowanie():
            return
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
                if self.walidacja_danych(imie, nazwisko, wiek, wynagrodzenie):
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
                if nowe_wynagrodzenie.replace('.', '', 1).isdigit():
                    self.manager.aktualizacja(nazwisko, nowe_wynagrodzenie)
                else:
                    print("Wynagrodzenie musi być liczbą.")
            elif wybor == "5":
                print("Zamknięcie programu.")
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

frontend = FrontendManager()
frontend.interfejs()
