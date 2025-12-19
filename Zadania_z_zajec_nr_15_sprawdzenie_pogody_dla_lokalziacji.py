# Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:

# Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03. W przypadku nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
# Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
# Istnieją trzy możliwe informacje dla opadów deszczu:
# Będzie padać (dla wyniku większego niż 0.0)
# Nie będzie padać (dla wyniku równego 0.0)
# Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
# Będzie padać
# Nie będzie padać
# Nie wiem
# Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.

# URL do API:
# https://api.open-meteo.com/v1/forecast?latitude={51° 6′ 0″}&longitude={17° 1′ 59″}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={2025-12-12}&end_date={2025-12-12}

# W URL należy uzupełnić parametry: latitude, longitude oraz searched_date

import datetime
import requests
import sys
from geopy.geocoders import Nominatim
sys.stdout.reconfigure(encoding="utf-8")

Prognoza_pogody = [
    {
        "Miasto":"",
        "Data":"",
        "Szerokosc":"",
        "Dlugosc":"",
        "Prognoza":""  
    }  
]

#Wczytanie pliku z prognozą pogody
Prognoza_pogody_plik = open("Prognoza_pogody.txt", "r",encoding="utf-8")
for linia in Prognoza_pogody_plik:
    miasto, data, szerokosc, dlugosc, prognoza = linia.strip().split(",")
    wpis = {
        "Miasto": miasto,
        "Data": data,
        "Szerokosc": szerokosc,
        "Dlugosc": dlugosc,
        "Prognoza": prognoza  
    }
    Prognoza_pogody.append(wpis)
Prognoza_pogody_plik.close()

for wpis in Prognoza_pogody:
    print(f"Miasto: {wpis['Miasto']}, Data: {wpis['Data']}, Szerokość: {wpis['Szerokosc']}, Długość: {wpis['Dlugosc']}, Prognoza: {wpis['Prognoza']}")

#Zapytanie o miasto i datę
print("Sprawdzanie pogody dla danego dnia!")
miasto = input("Podaj miasto dla którego chcesz sprawdzić pogodę dla danej daty (program obsługuje polskie znaki):")

while True:
    if miasto.strip() == "":
        print("Nazwa miasta nie może być pusta. Podaj poprawną nazwę miasta.")
        miasto = input("Podaj miasto dla którego chcesz sprawdzić pogodę dla danej daty:")
    else:
        break

geolocator = Nominatim(user_agent="moja_aplikacja")
lokalizacja = geolocator.geocode(miasto)
lat = lokalizacja.latitude
lon = lokalizacja.longitude
data = input("Podaj datę w formacie RRRR-MM-DD (jeśli pole będzie puste program przyjmnie jutrzeszą datę):")

if data == "":
    jutrszesza_data = datetime.date.today() + datetime.timedelta(days=1)
    data = str(jutrszesza_data)
    print("Program sprawdza pogodę dla jutrzejszej daty:", data)
else:
    print("Program sprawdza pogodę dla dzisiejszej daty:", data)
    
if lokalizacja:
    print("Miasto:", lokalizacja.address)
    print("Szerokość:", lokalizacja.latitude)
    print("Długość:", lokalizacja.longitude)
else:
    print("Nie znaleziono miasta")

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    "&hourly=precipitation"
    "&timezone=Europe/Warsaw"
)

Dane_pogodowe = requests.get(url).json()
Godziny = Dane_pogodowe["hourly"]["time"]
Opady = Dane_pogodowe["hourly"]["precipitation"]
Bedzie_padac = False

#Sprawdzenie czy prognoza dla danej daty i miasta jest już w pliku
for wpis in Prognoza_pogody:
    if wpis["Miasto"].lower() == miasto.lower() and wpis["Data"] == data:
        print(f"Prognoza dla miasta {miasto} na dzień {data} jest już w pliku:")
        print(wpis["Prognoza"])
        Bedzie_padac = True
        exit()
        break
    
#Pozyskanie prognozy z API i zapisa do pliku
for godzina, opad in zip(Godziny, Opady):
    if godzina.startswith(data) and opad > 0:
        print(f"Będzie padać ({opad} mm) – {godzina}")
        Bedzie_padac = True
        with open("Prognoza_pogody.txt", mode="a",encoding="utf-8") as plik_wynikowy:
            plik_wynikowy.write(f"{miasto},{data},{lat},{lon},Będzie padać ({opad} mm) – {godzina}\n")
        plik_wynikowy.close()
        break
    elif godzina.startswith(data) and opad == 0:
        print(f"Nie będzie padać – {godzina}")
        Bedzie_padac = True
        with open("Prognoza_pogody.txt", mode="a",encoding="utf-8") as plik_wynikowy:
            plik_wynikowy.write(f"{miasto},{data},{lat},{lon},Nie będzie padać – {godzina}\n")
        plik_wynikowy.close()
        break

if not Bedzie_padac:
    print("Brak danych o opadach dla tej daty lub wartość jest ujemna.")
    with open("Prognoza_pogody.txt", mode="a",encoding="utf-8") as plik_wynikowy:
        plik_wynikowy.write(f"{miasto},{data},{lat},{lon},Brak danych o opadach dla tej daty lub wartość jest ujemna.\n")
    plik_wynikowy.close()