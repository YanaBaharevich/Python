"""ZAD 1"""


def podzialpaczki(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"Pacza o wadze {waga} przekraca maksymalną wagę tj. {max_waga}")

    wagi_sorted = sorted(wagi, reverse=True)
    kursy = []

    for waga in wagi_sorted:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break
        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy


wagi = [10, 15, 7, 20, 5, 8, 10]
max_waga = 25

print(podzialpaczki(wagi, max_waga))
liczba_kursow, kursy = podzialpaczki(wagi, max_waga)
for i, kurs in enumerate(kursy, 1):
    print(F"Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg")

'''ZAD 2'''

from collections import deque


def bfs_task(graph, start, end):
    queue = deque([start])  # kolekcja dla przechowywania sciezek
    visited = set()  # wierzcholki odwidzone

    while queue:
        path = queue.popleft()
        node = path[-1]  # ostatni wierzcholek w sciezce
        # jezeli wierzcholek jest celem zwroc scezke
        if node == end:
            return path
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)

    return None  # jezeli nie znaleziono sciezki


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_task(graph, 'A', 'F'))


