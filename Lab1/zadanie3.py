from functools import reduce

def zadanie3(zadania):
    posortowane_zadania = sorted(zadania, key=lambda x: x[0])

    czas_bieżący = 0
    całkowity_czas_oczekiwania = 0

    for czas_wykonania, nagroda in zadania:
        czas_bieżący += czas_wykonania
        całkowity_czas_oczekiwania += czas_bieżący

    return posortowane_zadania, całkowity_czas_oczekiwania


zadania = [(3, 50), (1, 30), (2, 40)] # (jedn.czasu, jedn. nagrody)
posortowane_zadania, czas_oczekiwania = zadanie3(zadania)
print("Proceduralnie:")
print("Optymalna kolejność zadań:", posortowane_zadania)
print("Całkowity czas oczekiwania:", czas_oczekiwania)