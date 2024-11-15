from functools import lru_cache


def knapsack(przedmioty, pojemność):
    wagi = list(map(lambda x: x[0], przedmioty))
    wartości = list(map(lambda x: x[1], przedmioty))
    n = len(przedmioty)

    @lru_cache(maxsize=None)
    def knapsack(i, w):
        if i == 0 or w == 0:
            return 0

        if wagi[i - 1] > w:
            return knapsack(i - 1, w)

        return max(knapsack(i - 1, w), wartości[i - 1] + knapsack(i - 1, w - wagi[i - 1]))

    def wybrane_przedmioty():
        wynik = []
        w = pojemność
        for i in range(n, 0, -1):
            if knapsack(i, w) != knapsack(i - 1, w):
                wynik.append(przedmioty[i - 1])
                w -= wagi[i - 1]
        return wynik

    maksymalna_wartość = knapsack(n, pojemność)
    przedmioty_do_zabrania = wybrane_przedmioty()

    return maksymalna_wartość, przedmioty_do_zabrania


przedmioty = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (waga, wartość)
pojemność = 5

maks_wartość, wybrane_przedmioty = knapsack(przedmioty, pojemność)
print("Maksymalna wartość:", maks_wartość)
print("Wybrane przedmioty:", wybrane_przedmioty)
