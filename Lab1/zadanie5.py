from functools import reduce

def optymalny_harmonogram(zadania):
    posortowane_zadania = sorted(zadania, key=lambda x: x[1])

    maksymalna_nagroda = 0
    harmonogram = []

    def wybierz_zadanie(acc, zadanie):
        ostatnie_zadanie = acc[-1] if acc else None

        if ostatnie_zadanie is None or zadanie[0] >= ostatnie_zadanie[1]:
            acc.append(zadanie)
        return acc

    harmonogram = reduce(wybierz_zadanie, posortowane_zadania, [])

    maksymalna_nagroda = sum(map(lambda x: x[2], harmonogram))

    return maksymalna_nagroda, harmonogram


zadania = [
    (1, 3, 50),  # (czas rozpoczęcia, czas zakończenia, nagroda)
    (2, 5, 20),
    (3, 9, 100),
    (6, 8, 70),
    (5, 7, 60),
]

maks_nagroda, optymalny_harmonogram = optymalny_harmonogram(zadania)
print("Maksymalna nagroda:", maks_nagroda)
print("Optymalny harmonogram:", optymalny_harmonogram)
