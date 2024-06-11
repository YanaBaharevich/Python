import pandas as pd
import datetime
import random
import os
import matplotlib.pyplot as plt


#Dane podróży
data = {
    'ID': list(range(1, 48)),
    'Data_rezerwacji': ['2024-01-15', '2024-02-10', '2024-03-20', '2024-04-01', '2024-05-05',
                        '2024-06-10', '2024-07-20', '2024-08-02', '2024-09-14', '2024-10-10',
                        '2024-11-01', '2024-12-05', '2024-01-10', '2024-02-15', '2024-03-20',
                        '2024-04-05', '2024-05-10', '2024-06-15', '2024-07-20', '2024-08-05',
                        '2024-09-14', '2024-10-10', '2024-11-05', '2024-12-10', '2024-01-15',
                        '2024-02-20', '2024-03-25', '2024-04-30', '2024-05-05', '2024-06-10',
                        '2024-07-15', '2024-08-20', '2024-09-01', '2024-10-05', '2024-11-11',
                        '2024-12-20', '2024-01-02', '2024-02-14', '2024-03-10', '2024-04-01',
                        '2024-05-05', '2024-06-10', '2024-07-15', '2024-08-20', '2024-09-01',
                        '2024-10-05', '2024-11-11'],
    'Data_wylotu': ['2024-02-01', '2024-03-05', '2024-04-10', '2024-04-15', '2024-05-20',
                    '2024-06-25', '2024-08-05', '2024-08-20', '2024-09-30', '2024-10-25',
                    '2024-11-15', '2024-12-20', '2024-01-25', '2024-03-01', '2024-04-05',
                    '2024-04-20', '2024-05-25', '2024-06-30', '2024-08-05', '2024-08-20',
                    '2024-09-30', '2024-10-25', '2024-11-20', '2024-12-25', '2025-01-30',
                    '2025-03-05', '2025-04-10', '2025-05-15', '2025-06-25', '2025-07-30',
                    '2025-09-05', '2025-09-20', '2025-10-20', '2025-11-25', '2025-12-25',
                    '2026-01-05', '2026-01-20', '2026-02-25', '2026-03-25', '2026-04-30',
                    '2026-05-20', '2026-06-25', '2026-07-30', '2026-08-25', '2026-09-30',
                    '2026-10-25', '2026-11-20'],
    'Data_powrotu': ['2024-02-10', '2024-03-15', '2024-04-15', '2024-04-20', '2024-06-01',
                     '2024-07-05', '2024-08-15', '2024-08-30', '2024-10-10', '2024-11-05',
                     '2024-11-25', '2025-01-05', '2024-02-05', '2024-03-10', '2024-04-15',
                     '2024-04-30', '2024-06-05', '2024-07-10', '2024-08-15', '2024-08-30',
                     '2024-10-10', '2024-11-05', '2024-11-30', '2025-01-05', '2025-02-10',
                     '2025-03-15', '2025-04-20', '2025-05-25', '2025-07-05', '2025-08-10',
                     '2025-09-15', '2025-09-30', '2025-11-01', '2025-12-05', '2026-01-05',
                     '2026-01-30', '2026-03-10', '2026-03-30', '2026-05-05', '2026-05-30',
                     '2026-06-25', '2026-08-05', '2026-08-30', '2026-10-05', '2026-10-30',
                     '2026-11-25', '2026-12-30'],
    'Trasa': ['Warszawa - Paryż', 'Berlin - Nowy Jork', 'Londyn - Barcelona', 'Rzym - Ateny', 'Kraków - Dubaj',
              'Gdańsk - Oslo', 'Szczecin - Lizbona', 'Katowice - Mediolan', 'Poznań - Madryt', 'Łódź - Pekin',
              'Kraków - Rzym', 'Warszawa - Tokio', 'Gdańsk - Lizbona', 'Wrocław - Nowy Jork', 'Szczecin - Barcelona',
              'Poznań - Mediolan', 'Katowice - Paryż', 'Łódź - Berlin', 'Kraków - Londyn', 'Warszawa - Dubaj',
              'Gdańsk - Rzym', 'Poznań - Barcelona', 'Kraków - Paryż', 'Warszawa - Nowy Jork', 'Gdańsk - Madryt',
              'Szczecin - Pekin', 'Katowice - Londyn', 'Łódź - Dubaj', 'Warszawa - Barcelona', 'Gdańsk - Paryż',
              'Berlin - Mediolan', 'Oslo - Pekin', 'Londyn - Paryż', 'Ateny - Dubaj', 'Mediolan - Barcelona',
              'Nowy Jork - Tokio', 'Madryt - Rzym', 'Barcelona - Paryż', 'Paryż - Dubaj', 'Berlin - Barcelona',
              'Nowy Jork - Barcelona', 'Madryt - Dubaj', 'Pekin - Tokio', 'Paryż - Rzym', 'Mediolan - Lizbona',
              'Dubaj - Barcelona', 'Barcelona - Mediolan'],
    'Linia_lotnicza': ['LOT', 'Lufthansa', 'British Airways', 'Ryanair', 'Emirates',
                        'SAS', 'TAP Portugal', 'Ryanair', 'Iberia', 'Air China',
                        'Alitalia', 'LOT', 'TAP Portugal', 'Lufthansa', 'Ryanair',
                        'LOT', 'Lufthansa', 'Ryanair', 'British Airways', 'Emirates',
                        'Ryanair', 'LOT', 'Air France', 'LOT', 'Iberia',
                        'Air China', 'British Airways', 'Emirates', 'Ryanair', 'LOT',
                        'Ryanair', 'British Airways', 'Air China', 'British Airways', 'Emirates',
                        'British Airways', 'Emirates', 'Lufthansa', 'Ryanair', 'Emirates',
                        'Lufthansa', 'Ryanair', 'Emirates', 'British Airways', 'Ryanair',
                        'Emirates', 'British Airways'],
    'Klasa_biletu': ['Ekonomiczna', 'Premium', 'Biznesowa', 'Ekonomiczna', 'Premium',
                      'Ekonomiczna', 'Biznesowa', 'Ekonomiczna', 'Premium', 'Ekonomiczna',
                      'Biznesowa', 'Premium', 'Ekonomiczna', 'Biznesowa', 'Premium',
                      'Ekonomiczna', 'Premium', 'Ekonomiczna', 'Biznesowa', 'Ekonomiczna',
                      'Premium', 'Ekonomiczna', 'Biznesowa', 'Premium', 'Premium',
                      'Ekonomiczna', 'Premium', 'Biznesowa', 'Biznesowa', 'Ekonomiczna',
                      'Premium', 'Ekonomiczna', 'Biznesowa', 'Ekonomiczna', 'Biznesowa',
                      'Ekonomiczna', 'Biznesowa', 'Premium', 'Biznesowa', 'Ekonomiczna',
                      'Premium', 'Ekonomiczna', 'Premium', 'Biznesowa', 'Ekonomiczna',
                      'Premium', 'Biznesowa'],
    'Cena_biletu': [500, 1200, 800, 300, 2500,
                     600, 1400, 400, 1800, 900,
                     1000, 3000, 700, 2500, 1200,
                     500, 1500, 300, 2000, 1800,
                     1000, 700, 1800, 3500, 900,
                     2500, 2000, 1200, 800, 700,
                     1500, 2500, 2000, 1800, 500,
                     1000, 1400, 1200, 300, 600,
                     1500, 1000, 1800, 2500, 2000,
                     1200, 2500],
    'Hotel': ['Hotel ABC', 'Hotel XYZ', 'Hotel QWE', 'Hotel 123', 'Hotel EFG',
               'Hotel ASD', 'Hotel ZXC', 'Hotel POI', 'Hotel MNB', 'Hotel QAZ',
               'Hotel WER', 'Hotel RTY', 'Hotel UIO', 'Hotel PLK', 'Hotel ASX',
               'Hotel WQA', 'Hotel BVC', 'Hotel DFG', 'Hotel FGH', 'Hotel JKL',
               'Hotel MNB', 'Hotel QWE', 'Hotel ASD', 'Hotel QAZ', 'Hotel PLK',
               'Hotel POI', 'Hotel MNB', 'Hotel RTY', 'Hotel UIO', 'Hotel ABC',
               'Hotel XYZ', 'Hotel QWE', 'Hotel 123', 'Hotel EFG', 'Hotel ASD',
               'Hotel ZXC', 'Hotel POI', 'Hotel MNB', 'Hotel QAZ', 'Hotel WER',
               'Hotel RTY', 'Hotel UIO', 'Hotel PLK', 'Hotel ASX', 'Hotel WQA',
               'Hotel BVC', 'Hotel DFG'],
    'Koszt_noclegu': [600, 1500, 900, 400, 3000,
                       700, 1600, 450, 2000, 1000,
                       1200, 3500, 800, 3000, 1500,
                       600, 1800, 350, 2300, 2000,
                       1200, 800, 2000, 4000, 1000,
                       3000, 2500, 800, 600, 700,
                       1800, 3000, 2500, 2000, 600,
                       1200, 1400, 1500, 400, 700,
                       1800, 900, 2000, 3000, 1500,
                       1000, 2500],
    'Miasto': ['Paryż', 'Nowy Jork', 'Barcelona', 'Ateny', 'Dubaj',
                'Oslo', 'Lizbona', 'Mediolan', 'Madryt', 'Pekin',
                'Rzym', 'Tokio', 'Lizbona', 'Nowy Jork', 'Barcelona',
                'Mediolan', 'Paryż', 'Berlin', 'Londyn', 'Dubaj',
                'Rzym', 'Barcelona', 'Paryż', 'Nowy Jork', 'Madryt',
                'Pekin', 'Londyn', 'Dubaj', 'Barcelona', 'Paryż',
                'Mediolan', 'Pekin', 'Paryż', 'Dubaj', 'Barcelona',
                'Nowy Jork', 'Rzym', 'Paryż', 'Dubaj', 'Barcelona',
                'Nowy Jork', 'Dubaj', 'Pekin', 'Rzym', 'Lizbona',
                'Barcelona', 'Mediolan'],
    'Typ_podrozy': ['Wakacje', 'Służbowe', 'Wakacje', 'Wakacje', 'Wakacje',
                     'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje',
                     'Wakacje', 'Służbowe', 'Służbowe', 'Służbowe', 'Wakacje',
                     'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje',
                     'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje',
                     'Wakacje', 'Służbowe', 'Służbowe', 'Wakacje', 'Wakacje',
                     'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje',
                     'Służbowe', 'Wakacje', 'Służbowe', 'Wakacje', 'Wakacje',
                     'Wakacje', 'Wakacje', 'Wakacje', 'Wakacje', 'Służbowe',
                     'Służbowe', 'Wakacje']
}

df = pd.DataFrame(data)
df.to_excel('dane_podrozy.xlsx', index=False)

sciezka_do_pliku_excel = 'D:\\Python\\dane_podrozy.xlsx'

licznik_biletow = 1

while True:
    nazwa_pliku = f"bilet_podrozy_{licznik_biletow}.txt"
    if not os.path.exists(nazwa_pliku):
        try:
            losowy_indeks = random.choice(df.index)
            losowa_podroz = df.loc[losowy_indeks]

            with open(nazwa_pliku, 'w', encoding='utf-8') as file:
                file.write("*" * 50 + "\n")
                file.write("Bilet podróży\n")
                file.write("*" * 50 + "\n")
                file.write("Data rezerwacji: {}\n".format(losowa_podroz['Data_rezerwacji']))
                file.write("_" * 50 + "\n")
                file.write("Data wylotu: {}\n".format(losowa_podroz['Data_wylotu']))
                file.write("_" * 50 + "\n")
                file.write("Trasa: {}\n".format(losowa_podroz['Trasa']))
                file.write("_" * 50 + "\n")
                file.write("Linia lotnicza: {}\n".format(losowa_podroz['Linia_lotnicza']))
                file.write("_" * 50 + "\n")
                file.write("Klasa biletu: {}\n".format(losowa_podroz['Klasa_biletu']))
                file.write("_" * 50 + "\n")
                file.write("Cena biletu: {}\n".format(losowa_podroz['Cena_biletu']))
                file.write("_" * 50 + "\n")

            print(f"Bilet podróży został utworzony w pliku '{nazwa_pliku}'.")
            licznik_biletow += 1
            break
        except Exception as e:
            print("Wystąpił błąd:", e)
    else:
        licznik_biletow += 1


df=pd.read_excel('D:\\Python\\dane_podrozy.xlsx')
stat=df.copy()
stat.drop("Trasa",axis=1,inplace=True)
stat.drop("Hotel",axis=1,inplace=True)
stat.drop("Data_rezerwacji",axis=1,inplace=True)

#1 wykres

dane_miasto= df["Typ_podrozy"].value_counts()
mst = dane_miasto.index
lsc = dane_miasto.values
def prepare_label(pct, allvals):
    absolute = int(pct / 100. * sum(allvals))
    return "{:.1f}%)".format(pct, absolute)
wedges, _, autotexts = plt.pie(lsc, labels=mst, autopct=lambda pct: prepare_label(pct, lsc), textprops=dict(color="black"))
plt.setp(autotexts, size=14, weight="bold")
plt.legend(title='Miasta')
plt.show()

#2 wykres








