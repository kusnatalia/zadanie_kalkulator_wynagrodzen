import csv

def zapisz_do_csv(nazwa_pliku, lista_pracownikow):
    with open(nazwa_pliku, 'w', newline='') as plik:
        pole_imie = 'imię'
        pole_nazwisko = 'nazwisko'
        pole_wynagrodzenie = 'wynagrodzenie_brutto'

        writer = csv.DictWriter(plik, fieldnames=[pole_imie, pole_nazwisko, pole_wynagrodzenie])
        writer.writeheader()

        for pracownik in lista_pracownikow:
            writer.writerow({pole_imie: pracownik['imię'], pole_nazwisko: pracownik['nazwisko'], pole_wynagrodzenie: pracownik['wynagrodzenie_brutto']})

lista_pracownikow = [
    {'imię': 'Jan', 'nazwisko': 'Kowalski', 'wynagrodzenie_brutto': 5000},
    {'imię': 'Zofia', 'nazwisko': 'Nowak', 'wynagrodzenie_brutto': 7000},
    {'imię': 'Wojtek', 'nazwisko': 'Inny', 'wynagrodzenie_brutto': 6500}
]

nazwa_pliku = 'pracownicy.csv'
zapisz_do_csv(nazwa_pliku, lista_pracownikow)

import csv


class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)

    def oblicz_wynagrodzenie_netto(self):


        skladki  = self.wynagrodzenie_brutto * 0.1371
        skladka_zdrowotna= (self.wynagrodzenie_brutto-skladki)*0.09
        dochod=self.wynagrodzenie_brutto-skladki-250
        zaliczka =dochod*0.12 - 300

        wynagrodzenie_netto = self.wynagrodzenie_brutto - skladki - skladka_zdrowotna-dochod
        return wynagrodzenie_netto

    def oblicz_calkowity_koszt(self):
        wynagrodzenie_netto = self.oblicz_wynagrodzenie_netto()
        koszt_pracodawcy = self.wynagrodzenie_brutto + (self.wynagrodzenie_brutto * 0.1) + (
                    self.wynagrodzenie_brutto * 0.3)  # Przykładowe dodatkowe koszty pracodawcy
        return koszt_pracodawcy


def oblicz_calkowity_koszt_pracodawcy():
    lista_pracownikow = []

    with open('pracownicy.csv', 'r') as plik_csv:
        czytnik = csv.reader(plik_csv)

        next(czytnik)
        for wiersz in czytnik:
            imie, nazwisko, wynagrodzenie_brutto = wiersz
            pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
            lista_pracownikow.append(pracownik)

    calkowity_koszt = 0.0
    for pracownik in lista_pracownikow:
        calkowity_koszt += pracownik.oblicz_calkowity_koszt()

    return calkowity_koszt


calkowity_koszt = oblicz_calkowity_koszt_pracodawcy()
print(f'Całkowity koszt pracodawcy: {calkowity_koszt}')
