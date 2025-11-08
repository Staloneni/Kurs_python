# Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

# Program po uruchomieniu wyświetla informację o dostępnych komendach:

# saldo
# sprzedaż
# zakup
# konto
# lista
# magazyn
# przegląd
# koniec

# Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

# saldo - Program pobiera kwotę do dodania lub odjęcia z konta. Done
# sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
# zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
# konto - Program wyświetla stan konta.
# lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
# magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
# przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
# koniec - Aplikacja kończy działanie.

# Dodatkowe wymagania:

# Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec". Done
# Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
# Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
# Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.

Slado = 10000
Historia_operacji = []

Stan_magazynu = [
    {
        "Nazwa_produktu": "Odkurzacz",
        "Cena_jednostkowa": 1500,
        "Ilosc": 4,
        "Kod_produktu_LPN": "LPNOD1488",
    }, 
    {
        "Nazwa_produktu": "Klocki",
        "Cena_jednostkowa": 200,
        "Ilosc": 10,
        "Kod_produktu_LPN": "LPNKL2001",
        }, 
    {
        "Nazwa_produktu": "Piła",
        "Cena_jednostkowa": 800,
        "Ilosc": 2,
        "Kod_produktu_LPN": "LPNPI8002",
        },
]

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
        Historia_operacji.append({ "Komenda": "Saldo", "Kwota": kwota})
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
      
        Historia_operacji.append({ "Komenda": "Sprzedaż", "Nazwa_produktu": Nazwa_produktu, "Ilość": Ilość })
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
        Historia_operacji.append({ "Komenda": "Zakup", "Nazwa_produktu": Nazwa_produktu, "Ilość": Ilość, "Cena_jednostkowa": Cena_jednostkowa })
    case "Konto"|"4":
        print("Wybrałeś komendę konto.")
        print("Aktualne saldo firmy wynosi:", Slado, "zł.")
        Historia_operacji.append({ "Komenda": "Konto" })
    case "Lista"|"5":
        print("Wybrałeś komendę lista.")
        print("Stan magazynu:")
        for produkt in Stan_magazynu:
            print(f"Nazwa produktu: {produkt['Nazwa_produktu']}, Cena jednostkowa: {produkt['Cena_jednostkowa']} zł, Ilość: {produkt['Ilosc']}, Kod produktu LPN: {produkt['Kod_produktu_LPN']}")
        Historia_operacji.append({ "Komenda": "Lista" })
    case "Magazyn"|"6":
        print("Wybrałeś komendę magazyn.")
        nazwa_produktu = input("Podaj nazwę produktu, którego stan magazynu chcesz sprawdzić: ")
        
        for produkt in Stan_magazynu:
            if produkt["Nazwa_produktu"] == nazwa_produktu:
                print(f"Nazwa produktu: {produkt['Nazwa_produktu']}, Cena jednostkowa: {produkt['Cena_jednostkowa']} zł, Ilość: {produkt['Ilosc']}, Kod produktu LPN: {produkt['Kod_produktu_LPN']}")
                break
        else:
            print("Produkt nie znajduje się w magazynie.") 
        Historia_operacji.append({ "Komenda": "Magazyn", "Nazwa_produktu": nazwa_produktu })
    case "Przegląd"|"7":
        print("Wybrałeś komendę przegląd.")
        Indesk_od = int(input("Podaj indeks 'od' (lub pozostaw puste, aby zacząć od początku): "))-1
        Indesk_do = int(input("Podaj indeks 'do' (lub pozostaw puste, aby zakończyć na końcu): "))-1
        
        for i in range(len(Historia_operacji)):
            if (Indesk_od == -1 or i >= Indesk_od) and (Indesk_do == -1 or i <= Indesk_do):
                print(f"Indeks {i + 1}: {Historia_operacji[i]}")
        
        Historia_operacji.append({ "Komenda": "Przegląd", "Indesk_od": Indesk_od, "Indesk_do": Indesk_do })
    case "Koniec"|"8":
        print("Kończysz działanie programu.")
        break
    case _:
        print("Nieznana komenda. Proszę spróbować ponownie.")

