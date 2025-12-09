# Napisz program do gry w kółko i krzyżyk z przeciwnikiem komputerowym. Główne założenia:
# 1. Gracz komputerowy rozpoczyna grę.
# 2. Gracz komputerowy jest reprezentowany przez krzyżyk.
# 3. Użytkownik programu jest reprezentowany przez kółko.
# 4. Przeciwnik komputerowy gra optymalnie, tzn. zawsze wybiera najlepszy możliwy ruch. W połączeniu z pkt 1 oznacza to, że gracz komputerowy nigdy nie przegra.
# 5.Identyfikatory pól na tablicy są rozmieszczone następująco:
#    1 2 3
#    4 5 6
#    7 8 9 .

# Przebieg gry (działanie programu):
# 1. Przeciwnik komputerowy wykonuje ruch. Jeśli komputer wygrał, wyświetla komunikat "Przegrana". Jeśli ostatnie pole zostało wypełnione, wyświetla komunikat "Remis" i kończy działanie.
# 2. Program zaczyna działanie od wyświetlenia tablicy jako trzech linii w terminalu. Minus "-" symbolizuje pole jeszcze nie wypełnione.
# ---
# -X-
# ---
# 3. Program pobiera od użytkownika identyfikator pola, które ma być wypełnione kółkiem i oczekuje naciśnięcia <Enter>.
# 4. Jeśli identyfikator pola jest nieprawidłowy (zły identyfikator lub pole jest już zajęte), program wyświetla napis "Błąd", i wraca do punktu 4.
# 5. Program wraca do punktu 1.

#na razie gra na 2 osoby bez komputera

#Definicje funkcji
def sprawdzenie_poprwnosci_wyboru_pola(pole):
  while True:
      if not pole.isdigit() or int(pole) < 1 or int(pole) > 9:
           print("Błąd niewłaściwy numer pola lub nierozpoznany znak.")
           pole = input("Wybierz ponownie pole do wypełnienia kółkiem (1-9): ")
      else:
         break    
  return pole
    
def przypisanie_kolumny_i_wiersza(pole):
    if pole in {1,2,3}:
        wiersz = 0
        kolumna = pole - 1
    elif pole in {4,5,6}:
        wiersz = 1
        kolumna = pole - 4
    elif pole in {7,8,9}:
        wiersz = 2
        kolumna = pole - 7
    return wiersz, kolumna       

def wyswietl_tablice(tablica):
    for wiersz in tablica:
        linia = ""
        for pole in wiersz:
            linia += pole
        print(linia)

def sprawdzenie_zajetosci_pola(tablica, wiersz, kolumna):
    if tablica[wiersz][kolumna] != '-':
        print("Błąd pole zajęte.")
        return False
    else:
     return True

def sprawdzenie_wygranej(tablica):
    #sprawdzenie wierszy
    for wiersz in tablica:
        if wiersz[0] == wiersz[1] == wiersz[2] and wiersz[0] != '-':
            if wiersz[0] == wiersz[1] == wiersz[2] == 'O':
                print("Gratulacje! Gracz wygrał grę!")
            else:
                print("Niestety, komputer wygrał. Przegrana!")
            return True
    #sprawdzenie kolumn
    for kolumna in range(3):
        if tablica[0][kolumna] == tablica[1][kolumna] == tablica[2][kolumna] and tablica[0][kolumna] != '-':
            if tablica[0][kolumna] == tablica[1][kolumna] == tablica[2][kolumna] == 'O':
                print("Gratulacje! Gracz wygrał grę!")
            else:
                print("Niestety, komputer wygrał. Przegrana!")
            return True
    #sprawdzenie przekątnych
    if tablica[0][0] == tablica[1][1] == tablica[2][2] and tablica[0][0] != '-':
        if tablica[0][0] == tablica[1][1] == tablica[2][2] == 'O':
          print("Gratulacje! Gracz wygrał grę!")
        else:
         print("Niestety, komputer wygrał. Przegrana!")
        return True
    if tablica[0][2] == tablica[1][1] == tablica[2][0] and tablica[0][2] != '-':
        if tablica[0][2] == tablica[1][1] == tablica[2][0] == 'O':
          print("Gratulacje! Gracz wygrał grę!")
        else:
         print("Niestety, komputer wygrał. Przegrana!")
        return True
    return False

def sprawdzenie_remisu(tablica):
    for wiersz in tablica:
        for pole in wiersz:
            if pole == '-':
                return False
    return True

def ruch_komputera(tablica):
    for i in range(3):
        for j in range(3):
            if tablica[i][j] == '-':
                tablica[i][j] = 'X'
                if sprawdzenie_wygranej(tablica):
                    return
                tablica[i][j] = '-'
    for i in range(3):
        for j in range(3):
            if tablica[i][j] == '-':
                tablica[i][j] = 'O'
                if sprawdzenie_wygranej(tablica):
                    tablica[i][j] = 'X'
                    return
                tablica[i][j] = '-'
    for i in range(3):
        for j in range(3):
            if tablica[i][j] == '-':
                tablica[i][j] = 'X'
                return

# Główna część programu
tablica_oznaczen_pol = [{1,2,3}, {4,5,6}, {7,8,9}]
tablica_gry = [['-','-','-'], ['-','-','-'], ['-','-','-']]

print("Witaj w grze Kółko i Krzyżyk!")
print("Onaczenia pól gry:")

for wiersz in tablica_oznaczen_pol:
    linia = " "
    for pole in wiersz:
        linia += str(pole)
    print(linia)

print("Gra się rozpoczęła! Plansza wygląda następująco:")
wyswietl_tablice(tablica_gry)

while True: #pętla gry
 #Ruch komputera krzyżyk
 print("Grę rozpoczyna komputer (krzyżyk)!")
 ruch_komputera(tablica_gry)
 wyswietl_tablice(tablica_gry)
 if sprawdzenie_wygranej(tablica_gry):
     break
 
 if sprawdzenie_remisu(tablica_gry):
      print("Remis!")
      break 
    
 #Ruch gracza kółko
 pole_O = input("Wybierz pole do wypełnienia kółkiem (1-9): ")

 #Sprawdzenie poprawności wyboru pola dla gracza kółko
 while True:
      pole_O = int(sprawdzenie_poprwnosci_wyboru_pola(pole_O))
      wiersz, kolumna = przypisanie_kolumny_i_wiersza(pole_O)
      if sprawdzenie_zajetosci_pola(tablica_gry, wiersz, kolumna) == False:
          pole_O = input("Wybierz ponownie pole do wypełnienia (1-9): ")
          continue
      else:
          break
 
 tablica_gry[wiersz][kolumna] = 'O'
 
 wyswietl_tablice(tablica_gry)
 
 if sprawdzenie_wygranej(tablica_gry):
     break

 if sprawdzenie_remisu(tablica_gry):
      print("Remis!")
      break 