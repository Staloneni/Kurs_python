# Na podstawie zadania z lekcji 5 (operacje na koncie, sprzedaż/zakup itp.) należy zaimplementować poniższą część:

# Saldo konta oraz magazyn mają zostać zapisane do pliku tekstowego, a przy kolejnym uruchomieniu programu ma zostać odczytany. 
# Zapisać należy również historię operacji (przegląd), która powinna być rozszerzana przy każdym kolejnym uruchomieniu programu.

Saldo_pliku = open("Saldo.txt", "r")
Slado = float(Saldo_pliku.read())
Saldo_pliku.close()

Historia_operacji = []

Hisotria_wczytaj_plik = open("Historia_operacji.txt", "r")
for linia in Hisotria_wczytaj_plik:
    Historia_operacji.append(linia.strip())
Hisotria_wczytaj_plik.close()

Stan_magazynu = [
    # {
    #     "Nazwa_produktu": "Odkurzacz",
    #     "Cena_jednostkowa": 1500,
    #     "Ilosc": 4,
    #     "Kod_produktu_LPN": "LPNOD1488",
    # }, 
    # {
    #     "Nazwa_produktu": "Klocki",
    #     "Cena_jednostkowa": 200,
    #     "Ilosc": 10,
    #     "Kod_produktu_LPN": "LPNKL2001",
    #     }, 
    # {
    #     "Nazwa_produktu": "Piła",
    #     "Cena_jednostkowa": 800,
    #     "Ilosc": 2,
    #     "Kod_produktu_LPN": "LPNPI8002",
    #     },
]

Magazyn_wczytaj_plik = open("Stan_magazynu.txt", "r")
for linia in Magazyn_wczytaj_plik:
    nazwa_produktu, cena_jednostkowa, ilosc, kod_produktu_LPN = linia.strip().split(",")
    produkt = {
        "Nazwa_produktu": nazwa_produktu,
        "Cena_jednostkowa": float(cena_jednostkowa),
        "Ilosc": int(ilosc),
        "Kod_produktu_LPN": kod_produktu_LPN,
    }
    Stan_magazynu.append(produkt)
Magazyn_wczytaj_plik.close()

while True:
 komenda = input("""Witaj w systemie zarządzania firmą! Oto dostępne komendy, podaj nazwę lub liczbę (wielkość liter ma znaczenia):
 1. Saldo
 2. Sprzedaż
 3. Zakup
 4. Konto - wyświetla stan konta firmy   
 5. Lista - wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością
 6. Magazyn - wyświetla stan magazynu dla konkretnego produktu
 7. Przegląd
 8. Koniec
 Wprowadź komendę: """)

 match komenda:
    case "Saldo"|"1":
        print("Akutlanie saldo firmy wynosi:", Slado, "zł.")
        kwota = float(input("Podaj kwotę do dodania lub odjęcia w złotówkach (jeśli chcesz odjąć, wpisz wartość ujemną): "))
        Slado += kwota  
        if Slado < 0:
            print("Operacja niemożliwa do wykonania. Saldo nie może być ujemne.")
            Slado -= kwota
        print("Nowe saldo firmy wynosi:", Slado, "zł.")
        operacja = "Komenda: Saldo, Kwota: " + str(kwota) + "zł"
        Historia_operacji.append(operacja)
    case "Sprzedaż"|"2":
        print("Wybrałeś komendę sprzedaż.")
        Nazwa_produktu = input("Podaj nazwę produktu, który sprzedałeś:")
        Ilość = int(input("Podaj ilość sprzedanego produktu: "))
        
        for produkt in Stan_magazynu:
            if produkt["Nazwa_produktu"] == Nazwa_produktu:
                if produkt["Ilosc"] >= Ilość:
                    przychod = produkt["Cena_jednostkowa"] * Ilość
                    Slado += przychod
                    produkt["Ilosc"] -= Ilość
                    print(f"Sprzedano {Ilość} sztuk produktu {Nazwa_produktu}. Przychód: {przychod} zł. Nowe saldo firmy wynosi: {Slado} zł.")
                else:
                    print("Operacja niemożliwa do wykonania. Brak wystarczającej ilości produktu w magazynie.")
                break
        operacja = "Komenda: Sprzedaż, Nazwa_produktu: " + Nazwa_produktu + ", Ilość: " + str(Ilość)
        Historia_operacji.append(operacja)
    case "Zakup"|"3":
        print("Wybrałeś komendę zakup.")
        Nazwa_produktu = input("Podaj nazwę produktu, który zakupiłeś:")
        Cena_jednostkowa = float(input("Podaj cenę jednostkową produktu w złotówkach: "))
        Ilość = int(input("Podaj ilość zakupionego produktu: "))
        Kod_produktu_LPN = input("Podaj kod produktu LPN: ")  
        koszt = Cena_jednostkowa * Ilość
        if Slado >= koszt:
            Slado -= koszt
            for produkt in Stan_magazynu:
                if produkt["Nazwa_produktu"] == Nazwa_produktu:
                    produkt["Ilosc"] += Ilość
                    print(f"Dodano {Ilość} sztuk produktu {Nazwa_produktu} do magazynu.")
                    break
            else:
                nowy_produkt = {
                    "Nazwa_produktu": Nazwa_produktu,
                    "Cena_jednostkowa": Cena_jednostkowa,
                    "Ilosc": Ilość,
                    "Kod_produktu_LPN": Kod_produktu_LPN,
                }
                Stan_magazynu.append(nowy_produkt)
                print(f"Dodano nowy produkt {Nazwa_produktu} do magazynu.")
            print(f"Koszt zakupu: {koszt} zł. Nowe saldo firmy wynosi: {Slado} zł.")
        else:
            print("Operacja niemożliwa do wykonania. Saldo nie może być ujemne.")
        
        operacja = "Komenda: Zakup, Nazwa produktu: " + Nazwa_produktu + ", Ilość: " + str(Ilość) + ", Cena jednostkowa: " + str(Cena_jednostkowa) + "zł"
        Historia_operacji.append(operacja)
    case "Konto"|"4":
        print("Wybrałeś komendę konto.")
        print("Aktualne saldo firmy wynosi:", Slado, "zł.")
        operacja = "Komenda: Konto"
        Historia_operacji.append(operacja)
    case "Lista"|"5":
        print("Wybrałeś komendę lista.")
        print("Stan magazynu:")
        for produkt in Stan_magazynu:
            print(f"Nazwa produktu: {produkt['Nazwa_produktu']}, Cena jednostkowa: {produkt['Cena_jednostkowa']} zł, Ilość: {produkt['Ilosc']}, Kod produktu LPN: {produkt['Kod_produktu_LPN']}")
        operacja = "Komenda: Lista"
        Historia_operacji.append(operacja)
    case "Magazyn"|"6":
        print("Wybrałeś komendę magazyn.")
        nazwa_produktu = input("Podaj nazwę produktu, którego stan magazynu chcesz sprawdzić: ")
        
        for produkt in Stan_magazynu:
            if produkt["Nazwa_produktu"] == nazwa_produktu:
                print(f"Nazwa produktu: {produkt['Nazwa_produktu']}, Cena jednostkowa: {produkt['Cena_jednostkowa']} zł, Ilość: {produkt['Ilosc']}, Kod produktu LPN: {produkt['Kod_produktu_LPN']}")
                break
        else:
            print("Produkt nie znajduje się w magazynie.") 
        operacja = "Komenda: Magazyn, Nazwa produktu: " + nazwa_produktu
        Historia_operacji.append(operacja)
    case "Przegląd"|"7":
        print("Wybrałeś komendę przegląd.")
        Indesk_od = int(input("Podaj indeks 'od' (lub pozostaw puste, aby zacząć od początku): "))-1
        Indesk_do = int(input("Podaj indeks 'do' (lub pozostaw puste, aby zakończyć na końcu): "))-1
        
        for i in range(len(Historia_operacji)):
            if (Indesk_od == -1 or i >= Indesk_od) and (Indesk_do == -1 or i <= Indesk_do):
                print(f"Indeks {i + 1}: {Historia_operacji[i]}")
        
        operacja = "Komenda: Przegląd, Indesk_od: " + str(Indesk_od) + ", Indesk_do: " + str(Indesk_do)
        Historia_operacji.append(operacja)
        
    case "Koniec"|"8":
        print("Kończysz działanie programu.")
        Saldo_pliku = open("Saldo.txt", "w")
        Saldo_pliku.write(Slado.__str__())
        Saldo_pliku.close()
        
        
        Historia_operacji_plik = open("Historia_operacji.txt", "a")
        for operacja in Historia_operacji:
            Historia_operacji_plik.write(operacja.__str__() + "\n")
        Historia_operacji_plik.close()
        
        Magazyn_zapis_stanu = open("Stan_magazynu.txt", "w")
        for produkt in Stan_magazynu:
            Magazyn_zapis_stanu.write(f"{produkt['Nazwa_produktu']},{produkt['Cena_jednostkowa']},{produkt['Ilosc']},{produkt['Kod_produktu_LPN']}\n")
        Magazyn_zapis_stanu.close()
        
        break
    case _:
        print("Nieznana komenda. Proszę spróbować ponownie.")

