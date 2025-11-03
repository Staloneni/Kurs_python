# Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać, a następnie wymaga podania wagi dla każdej z nich.

# Na koniec działania program powinien wyświetlić w podsumowaniu:

# Liczbę paczek wysłanych
# Liczbę kilogramów wysłanych
# Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
# Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik

# Restrykcje:

# Waga elementów musi być z przedziału od 1 do 10 kg.
# Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
# W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
# W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.

# Przykład 1:

# Ilość elementów: 2
# Wagi elementów: 7, 9
# Podsumowanie:

# Wysłano 1 paczkę (7+9)
# Wysłano 16 kg
# Suma pustych kilogramów: 4kg
# Najwięcej pustych kilogramów ma paczka 1 (4kg)

# Przykład 2:

#  Ilość elementów: 6
# Wagi elementów: 3, 6, 5, 8, 2, 3
# Podsumowanie:

# Wysłano 2 paczki (3+6+5, 8+2+3)
# Wysłano 27 kg
# Suma pustych kilogramów: 13kg
# Najwięcej pustych kilogramów ma paczka 2 (7kg)

# Przykład 3:
#  Ilość elementów: 8

# Wagi elementów: 7, 14
#  Podsumowanie:
# Wysłano 1 paczkę (7)
# Wysłano 7 kg
# Suma pustych kilogramów: 13kg
# Najwięcej pustych kilogramów ma paczka 13

maks_waga_paczki = int(20)
min_waga_elementu = int(1)
max_waga_elementu = int(10)

macierz_paczek = []
aktulana_paczka = []
waga_akutlanej_paczki = float(0)


liczba_elemnetów = int(input("Podaj liczbę elementów do wysłania:"))

for i in range(liczba_elemnetów):
    waga_elementu = float(input("Podaj wagę elementu w kg (dopuszczlany zakres wagowy od 1 kg do 10 kg):"))
        
    if waga_elementu < min_waga_elementu or waga_elementu > max_waga_elementu:
        print("Waga elementu spoza zakresu, kończę wczytywanie. Wczytane paczki zostaną wysłane.")
        break
      
    # sprawdzenie czy element zmieści się do paczki
    if waga_akutlanej_paczki + waga_elementu <= maks_waga_paczki:
        aktulana_paczka.append(waga_elementu)
        waga_akutlanej_paczki += waga_elementu
    else:
        macierz_paczek.append(aktulana_paczka)
        aktulana_paczka = [waga_elementu]
        waga_akutlanej_paczki = waga_elementu
        
# dorzucenie ostatniej paczki jeśli coś w niej zostało    
if aktulana_paczka:
   macierz_paczek.append(aktulana_paczka)
        
liczba_paczek = len(macierz_paczek)
całkowita_waga_zamówienia = sum(sum(paczka) for paczka in macierz_paczek)
suma_pustych_kg = liczba_paczek * maks_waga_paczki - całkowita_waga_zamówienia
        
puste_kg = [maks_waga_paczki - sum(paczka) for paczka in macierz_paczek]
puste_kg_najwiecej = max(puste_kg)
nr_paczki_z_najwiecej_pustymi = puste_kg.index(puste_kg_najwiecej) + 1        
        
print("Wysłano liczbę paczek:", liczba_paczek)
print("Wysłano:", całkowita_waga_zamówienia, "kg")
print("Suma pustych kilogarmów", suma_pustych_kg, "kg")
print("Najwięcej pustych kilogramów ma paczka nr", nr_paczki_z_najwiecej_pustymi,"(", puste_kg_najwiecej, "kg)")
print("Struktura zamówenia (każdy wiersz to paczka):")
for wiersz in macierz_paczek:
    print(wiersz)