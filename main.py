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
