import requests
from geopy.geocoders import Nominatim

class WeatherForecast:
 def __init__(self):
     self._data = {}

 def items(self):
     return self._data.items()
 
 def iter(self):
     return iter(self._data.items())
 
 def __setitem__(self, key, value):
     self._data[key] = value

 def __getitem__(self, key):
     return self._data[key]
 
 def Wczytanie_danych_pogody(path):
    try: 
        Prognoza_pogody = WeatherForecast()
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                miasto, data, szerokosc, dlugosc, prognoza = line.split(",")
                Prognoza_pogody._data[(miasto, data, szerokosc, dlugosc)] = prognoza

        return Prognoza_pogody
    except FileNotFoundError:
     print(f"Błąd: Plik {path} nie został znaleziony.")
      
 def Zapytanie_o_pogode_do_API(self, miasto):
            geolocator = Nominatim(user_agent="moja_aplikacja")
            lokalizacja = geolocator.geocode(miasto)
            lat = lokalizacja.latitude
            lon = lokalizacja.longitude
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
            return Godziny, Opady, lat, lon  
    
 def Zapisanie_danych_pogodowych_do_pliku(self, baza_prognozy_pogody):
        with open("Prognoza_pogody.txt", mode="a",encoding="utf-8") as plik_wynikowy:
            for (miasto, data, szerokosc, dlugosc), prognoza in baza_prognozy_pogody.items():
                linia = f"{miasto},{data},{szerokosc},{dlugosc},{prognoza}\n"
                plik_wynikowy.write(linia)
        plik_wynikowy.close()