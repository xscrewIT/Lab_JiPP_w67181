from collections import Counter
import string

stop_words = {
    "i", "w", "się", "na", "jest", "z", "do", "to", "że", "nie",
    "o", "a", "jak", "po", "ale", "za", "dla", "od", "przez", "aby"
}


def analiza_tekstu(tekst):
    tekst = tekst.translate(str.maketrans("", "", string.punctuation))

    akapity = tekst.strip().split("\n")
    zdania = [zdanie for akapit in akapity for zdanie in akapit.split(".") if zdanie]
    słowa = [słowo.lower() for zdanie in zdania for słowo in zdanie.split()]

    liczba_słów = len(słowa)
    liczba_zdań = len(zdania)
    liczba_akapitów = len(akapity)

    print(f"Liczba słów: {liczba_słów}")
    print(f"Liczba zdań: {liczba_zdań}")
    print(f"Liczba akapitów: {liczba_akapitów}")

    słowa_bez_stop_words = list(filter(lambda x: x not in stop_words, słowa))

    licznik_słów = Counter(słowa_bez_stop_words)
    najczęstsze_słowa = licznik_słów.most_common(10)

    print("\nNajczęściej występujące słowa (bez stop words):")
    for słowo, liczba in najczęstsze_słowa:
        print(f"{słowo}: {liczba}")


    def odwroc_slowo(słowo):
        return słowo[::-1] if słowo.lower().startswith('a') else słowo

    przekształcone_słowa = list(map(odwroc_slowo, słowa))

    przekształcony_tekst = ' '.join(przekształcone_słowa)

    print("\nPrzykład przekształconego tekstu (pierwsze 100 znaków):")
    print(przekształcony_tekst[:100], "...")


tekst = """
Anna i Adam aktywnie angażują się w analizę aplikacji. Analiza aktywności jest ambitnym aspektem projektu. 
Adam często aktualizuje archiwum, aby aplikacja działała automatycznie. Ania akceptuje nowe algorytmy, 
ale alarmy i awarie aplikacji są aktualnie analizowane. Awaria automatycznego systemu autoryzacji anulowała akcję Anny.
"""

analiza_tekstu(tekst)
