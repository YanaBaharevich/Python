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





