# Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.

# Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec. Done

# Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników. Done
# Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami. Done
# Polecenie "koniec" - Kończy działanie aplikacji. Done

# Proces tworzenia użytkowników: Done 

# Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie. Done
# Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C") Done
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii. Done
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy. Done
# Polecenie "koniec" - Wraca do pierwszego menu. Done

# Proces zarządzania użytkownikami:

# Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy. DONE
# Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą. DONE
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel. DONE
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca. DONE
# Polecenie "koniec" - Wraca do pierwszego menu.

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy
        
class Wychowawca:  
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
        
Baza_szkoły = {
    "Uczniowie": [Uczen("Jan", "Kowalski", "3C"), Uczen("Ewa", "Nowak", "2A"), Uczen("Piotr", "Wiśniewski", "2B")], 
    
    "Nauczyciele": [Nauczyciel("Anna", "Nowak", "Matematyka", ["3C", "2A"]), Nauczyciel("Paweł", "Zieliński", "Fizyka", ["3C","2B"]), Nauczyciel("Jan", "Gil", "Polski", ["2B","3C"]), Nauczyciel("Jan", "Porta", "Polski", ["2B"])], 
    
    "Wychowawcy": [Wychowawca("Marta", "Wiśniewska", "3C"), Wychowawca("Krzysztof", "Kowalski", "2A")],
    }
    
def wyszukaj_osób_z_klasy(klasa):
    uczniowie_w_klasie = [uczen for uczen in Baza_szkoły["Uczniowie"] if uczen.klasa == klasa]
    wychowawcy_w_klasie = [wychowawca for wychowawca in Baza_szkoły["Wychowawcy"] if wychowawca.klasa == klasa]
    return uczniowie_w_klasie, wychowawcy_w_klasie

def wyszukaj_lekcje_i_nauczycieli_ucznia(imie, nazwisko):
    uczniowie = [uczen for uczen in Baza_szkoły["Uczniowie"] if uczen.imie == imie and uczen.nazwisko == nazwisko]
    if not uczniowie:
        print(f'Nie znaleziono ucznia o imieniu {imie} i nazwisku {nazwisko}.')
        return
    uczen = uczniowie[0]
    print(f'Uczeń {uczen.imie} {uczen.nazwisko} z klasy {uczen.klasa} ma następujące lekcje i nauczycieli:')
    
    for nauczyciel in Baza_szkoły["Nauczyciele"]:
        if uczen.klasa in nauczyciel.klasy:
            print(f'- Przedmiot: {nauczyciel.przedmiot}, Nauczyciel: {nauczyciel.imie} {nauczyciel.nazwisko}')

def wyszukaj_klays_nuczyicela(imie, nazwisko):
    nauczyciele = [nauczyciel for nauczyciel in Baza_szkoły["Nauczyciele"] if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko]
    if not nauczyciele:
        print(f'Nie znaleziono nauczyciela o imieniu {imie} i nazwisku {nazwisko}.')
        return
    nauczyciel = nauczyciele[0]
    print(f'Nauczyciel {nauczyciel.imie} {nauczyciel.nazwisko} prowadzi następujące klasy:')
    for klasa in nauczyciel.klasy:
        print(f'- {klasa}')

def wyszukaj_uczniow_wychowawcy(imie, nazwisko):
    wychowawcy = [wychowawca for wychowawca in Baza_szkoły["Wychowawcy"] if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko]
    if not wychowawcy:
        print(f'Nie znaleziono wychowawcy o imieniu {imie} i nazwisku {nazwisko}.')
        return
    wychowawca = wychowawcy[0]
    print(f'Wychowawca {wychowawca.imie} {wychowawca.nazwisko} prowadzi klasę {wychowawca.klasa}. Uczniowie tej klasy to:')
    for uczen in Baza_szkoły["Uczniowie"]:
        if uczen.klasa == wychowawca.klasa:
            print(f'- {uczen.imie} {uczen.nazwisko}')


print("Witaj w systemie zarządzania bazą szkolną!")

while True: 
    komenda = input("""Dostępne komendy: 
    1. Utwórz 
    2. Zarządzaj 
    3. Koniec
    Podaj komendę: """)
    
    match komenda:
        case "Utwórz"|"1":  
            print("Wybrałeś opcję tworzenia użytkowników.")
            while True:
                tworzenie_opcja = input("""Wybierz typ użytkownika do utworzenia:
             1. Uczeń
             2. Nauczyciel
             3. Wychowawca
             4. Koniec
             Podaj komendę: """)
                match tworzenie_opcja: 
                    case "Uczeń"|"1":
                        imie = input("Podaj imię:")
                        nazwisko = input("Podaj nazwisko:")
                        klasa = input("Podaj nazwę klasy (np. 3C): ")
                        uczen = Uczen(imie, nazwisko, klasa)
                        Baza_szkoły["Uczniowie"].append(uczen)                       
                        print(f'Utworzono ucznia: {uczen.imie} {uczen.nazwisko}, klasa: {uczen.klasa}')
                    case "Nauczyciel"|"2":
                        imie = input("Podaj imię:")
                        nazwisko = input("Podaj nazwisko:")
                        przedmiot = input("Podaj nazwę przedmiotu prowadzonego:")
                        klasy = []
                        print("Podaj nazwy klas, które prowadzi nauczyciel (wpisz pustą linię, aby zakończyć):")
                        while True:
                            klasa = input()
                            if klasa == "":
                                break
                            klasy.append(klasa)
                        nauczyciel = Nauczyciel(imie, nazwisko, przedmiot, klasy)
                        Baza_szkoły["Nauczyciele"].append(nauczyciel)
                        print(f'Utworzono nauczyciela: {nauczyciel.imie} {nauczyciel.nazwisko}, przedmiot: {nauczyciel.przedmiot}, klasy: {", ".join(nauczyciel.klasy)}')
                    case "Wychowawca"|"3":
                        imie = input("Podaj imię:")
                        nazwisko = input("Podaj nazwisko:") 
                        klasa = input("Podaj nazwę prowadzonej klasy:")
                        wychowawca = Wychowawca(imie, nazwisko, klasa)
                        Baza_szkoły["Wychowawcy"].append(wychowawca)
                        print(f'Utworzono wychowawcę: {wychowawca.imie} {wychowawca.nazwisko}, klasa: {wychowawca.klasa}')
                    case "Koniec"|"4":
                        print("Powrót do głównego menu.")
                        break
        case "Zarządzaj"|"2":
            print("Wybrałeś opcję zarządzania użytkownikami.") 
            while True:
                zarzadzanie_opcja = input("""Wybierz opcję zarządzania użytkownikami:
                1. Klasa
                2. Uczeń
                3. Nauczyciel
                4. Wychowawca 
                5. Wyświelt bazę danych
                6. Koniec 
                Podaj komendę: """)
                
                match zarzadzanie_opcja:
                    case "Klasa"|"1":
                        
                        klasa = input("Podaj nazwę klasy (np. 3C): ")
                        print(f"Wypisuję uczniów i wychowawcę klasy {klasa}:")
                        uczniowie, wychowawcy = wyszukaj_osób_z_klasy(klasa)
                        print("Uczniowie:")
                        for uczen in uczniowie:
                            print(f'- {uczen.imie} {uczen.nazwisko}')
                        print("Wychowawcy:")
                        for wychowawca in wychowawcy:
                            print(f'- {wychowawca.imie} {wychowawca.nazwisko}')
                            
                    case "Uczeń"|"2":
                        
                        imie_ucznia= input("Podaj imię: ")
                        nazwisko_ucznia = input("Podaj nazwisko: ")
                        wyszukaj_lekcje_i_nauczycieli_ucznia(imie = imie_ucznia, nazwisko = nazwisko_ucznia)
                        
                    case "Nauczyciel"|"3":
                        
                        imie_nauczyciela = input("Podaj imię nauczyciela: ")
                        nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela: ")
                        wyszukaj_klays_nuczyicela(imie = imie_nauczyciela, nazwisko = nazwisko_nauczyciela)
                        
                    case "Wychowawca"|"4":
                        
                        imie_wychowawcy = input("Podaj imię wychowawcy: ")
                        nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy: ")
                        wyszukaj_uczniow_wychowawcy(imie = imie_wychowawcy, nazwisko = nazwisko_wychowawcy)
                        
                    case "Koniec"|"5":
                        
                        baza_wybór = input("Podaj nazwę bazy danych do wyświetlenia (uczniowie, nauczyciele, wychowawcy): ")
                    
                        if baza_wybór == "uczniowie":
                            print("Wyświetlam bazę danych uczniów:")
                            for uczen in Baza_szkoły["Uczniowie"]:
                              print(f'Uczeń: {uczen.imie} {uczen.nazwisko}, klasa: {uczen.klasa}')
                        elif baza_wybór == "nauczyciele":
                            
                            print("Wyświetlam bazę danych nauczycieli:")
                            for nauczyciel in Baza_szkoły["Nauczyciele"]:
                              print(f'Nauczyciel: {nauczyciel.imie} {nauczyciel.nazwisko}, przedmiot: {nauczyciel.przedmiot}')
                              print(f'Prowadzone klasy:')
                              for klasa in nauczyciel.klasy:
                                    print(f'- {klasa}')
                           
                        elif baza_wybór == "wychowawcy":
                            print("Wyświetlam bazę danych wychowawców:")
                            for wychowawca in Baza_szkoły["Wychowawcy"]:
                              print(f'Wychowawca: {wychowawca.imie} {wychowawca.nazwisko}, klasa: {wychowawca.klasa}') 
                              
                    case "Koniec"|"6":
                        print("Powrót do głównego menu.")
                        break
        case "Koniec"|"3":
            print("Koniec działania programu. Do zobaczenia!")
            break