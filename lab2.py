# Zadanie 1. Analiza Tekstu i Transformacje Funkcyjne

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


response = requests.get('https://www.cs.put.poznan.pl/mkomosinski/p/dowcipy.html')
content=response.text
soup= BeautifulSoup(response.content, 'html.parser')

print(soup)

text=soup.get_text()
lista=text.split(" ")
ilosci=pd.Series(np.array(lista)).value_counts()
tablica_poszukiwanych=["nie", "i","co"]
licznik=0
a={}
for i in tablica_poszukiwanych:
    licznik = 0
    for word in lista:
        if word == i:
            licznik += 1
    a[i]=licznik
print(a)

znaki = 0
slowa = 0

for element in text:
    znaki = znaki + 1
print("Ilość znaków to: " + str(znaki))

slowa = len(lista)
print("Ilość słów to: " + str(slowa))

x = list(filter(lambda x: x.startswith('a') or x.startswith('A'), lista))
print(x)
y=[]
for i in x:
    y.append(i[::-1])
print('Odwrotna kolejność: ', y)

# Zadanie 3. Dynamiczne Wyznaczanie Ekstremów w Niejednorodnych

def analiza_danych(dane):
    liczby = list(filter(lambda x:isinstance(x, (int, float)), dane))
    max_liczba = max(liczby)
    napisy = list(filter(lambda x:isinstance(x, str), dane))
    najdluzszy_napis = max(napisy,key=len)
    krotki = list(filter(lambda x:isinstance(x, tuple), dane))
    najwieksza_krotka = max(krotki,key=len)
    return max_liczba, najdluzszy_napis, najwieksza_krotka

dane_wejsciowe=[
    42,"napis",(1, 2, 3),[10, 20],3.14,
    "najdluzszy napis w zestawie",{"klucz": "wartosc"},(1, 2, 3, 4),-15
]
najwieksza_liczba,najdluzszy_napis,najwieksza_krotka=analiza_danych(dane_wejsciowe)
print(f"Największa liczba: {najwieksza_liczba}")
print(f"Najdłuższy napis: {najdluzszy_napis}")
print(f"Krotka z największą liczbą elementów: {najwieksza_krotka}")

# Zadanie 2: Walidacja i Przekształcenia Operacji na Macierzach

def waliduj_operacje(macierz1,macierz2=None,operacja="dodawanie"):
    if operacja=="dodawanie" or operacja=="odejmowanie":
        if macierz1.shape !=macierz2.shape:
            raise ValueError("Macierze muszą mieć te same wymiary do dodawania lub odejmowania")
    elif operacja == "mnozenie":
        if macierz1.shape[1] !=macierz2.shape[0]:
            raise ValueError("Liczba kolumn macierzy pierwszej musi być równa liczbie wierszy macierzy drugiej")
    elif operacja =="transponowanie":
        pass
    else:
        raise ValueError(f"Nieznana operacja: {operacja}")

def wykonaj_operacje(macierz1,macierz2=None,operacja="dodawanie"):
    if operacja=="dodawanie":
        wynik=np.add(macierz1, macierz2)
    elif operacja=="odejmowanie":
        wynik=np.subtract(macierz1, macierz2)
    elif operacja=="mnozenie":
        wynik=np.dot(macierz1, macierz2)
    elif operacja=="transponowanie":
        wynik=np.transpose(macierz1)
    else:
        raise ValueError(f"Nieznana operacja:{operacja}")
    return wynik

def system_operacji_na_macierzach(operacja,macierz1,macierz2=None):
    try:
        waliduj_operacje(macierz1,macierz2,operacja)
        wynik = wykonaj_operacje(macierz1,macierz2,operacja)
        return wynik
    except ValueError as e:
        return f"Błąd:{e}"

macierz1 = np.array([[1, 2], [3, 4]])
macierz2 = np.array([[5, 6], [7, 8]])

print("Dodawanie macierzy:")
print(system_operacji_na_macierzach("dodawanie",macierz1,macierz2))
print("\nOdejmowanie macierzy:")
print(system_operacji_na_macierzach("odejmowanie",macierz1,macierz2))
print("\nMnożenie macierzy:")
print(system_operacji_na_macierzach("mnozenie",macierz1,macierz2))
print("\nTransponowanie macierzy:")
print(system_operacji_na_macierzach("transponowanie",macierz1))
