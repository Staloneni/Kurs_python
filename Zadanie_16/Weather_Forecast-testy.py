import requests
from geopy.geocoders import Nominatim

class WeatherForecast:
    def __init__(self, filename):
       self.filename = filename
       self._data = {}
    
    def __iter__(self):
        return iter(self._data)
    
    def items(self):
        for miasto, data, lat, lon, prognoza in self._data.items():
            yield miasto, data, lat, lon, prognoza
    
def Wczytanie_danych_pogody(self):
        try:
            with open(self.filename, "r",encoding="utf-8") as Prognoza_pogody_plik:
                Prognoza_pogody = [{
                "Miasto":"",
                "Data":"",
                "Szerokosc":"",
                "Dlugosc":"",
                "Prognoza":""
               }]
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
                return Prognoza_pogody
        except FileNotFoundError:
            print(f"Błąd: Plik {self.filename} nie został znaleziony.")
            return Prognoza_pogody

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
    
def Zapisanie_danych_pogodowych_do_pliku(self, miasto, data, lat, lon, prognoza):
        with open("Prognoza_pogody.txt", mode="a",encoding="utf-8") as plik_wynikowy:
            plik_wynikowy.write(f"{miasto},{data},{lat},{lon},{prognoza}\n")
        plik_wynikowy.close()


