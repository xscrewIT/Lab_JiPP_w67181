#from multiprocessing.managers import Value

def zadanie1(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"Paczka o wadze {waga} przekracza maksymalną wagę kursu - {max_waga}")

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

liczba_kursow, kursy = zadanie1([10, 15, 7, 8, 5, 20, 10], 20)
for i, kurs in enumerate(kursy, 1):
    print(f"Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg")