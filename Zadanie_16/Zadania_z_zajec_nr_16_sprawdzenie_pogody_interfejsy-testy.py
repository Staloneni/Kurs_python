# Zoptymalizuj kod z poprzedniego zadania z pogodą.

# Utwórz klasę WeatherForecast, która będzie służyła do odczytywania i zapisywania pliku, a także odpytywania API. DONE

# Obiekt klasy WeatherForecast dodatkowo musi poprawnie implementować cztery metody:

#  __setitem__
#  __getitem__
#  __iter__ DONE
#  items

# Wykorzystaj w kodzie poniższe zapytania:

# weather_forecast[date] da odpowiedź na temat pogody dla podanej daty
# weather_forecast.items() zwróci generator tupli w formacie (data, pogoda) dla już zapisanych rezultatów przy wywołaniu
# weather_forecast to iterator zwracający wszystkie daty, dla których znana jest pogoda

import sys
import datetime
from Weather_Forecast import WeatherForecast
sys.stdout.reconfigure(encoding="utf-8")

#Wczytanie danych pogodowych z pliku
Wczytywanie_danych_pogodowych = WeatherForecast("Prognoza_pogody.txt")
Dane_pogodowe = Wczytywanie_danych_pogodowych.Wczytanie_danych_pogody()

#Wyświetlenie wczytanej prognozy pogody
Prognoza_pogody = Dane_pogodowe[1:]  # Pomijamy pierwszy pusty wpis
print("Wczytana prognoza pogody z pliku:")
for wpis in Prognoza_pogody:
    print(f"Miasto: {wpis['Miasto']}, Data: {wpis['Data']}, Szerokość: {wpis['Szerokosc']}, Długość: {wpis['Dlugosc']}, Prognoza: {wpis['Prognoza']}")


while True:
 komenda = input("""Lista dostępnych komend w programnie prognozy pogody (wybierz numer komendy): 
    1. Sprawdź pogodę dla danego dnia i miasta 
    2. Wyświetl zapisaną prognozę pogody w bazie danych
    3. Wyświetl prognozę pogody dla danej daty 
    4. Koniec
    Podaj komendę: """)
 
 match komenda:
    case "1":
     #Zapytanie o miasto i datę
      print("Sprawdzanie pogody dla danego dnia!")
      miasto = input("Podaj miasto dla którego chcesz sprawdzić pogodę dla danej daty (program obsługuje polskie znaki):")

      while True:
            if miasto.strip() == "":
                print("Nazwa miasta nie może być pusta. Podaj poprawną nazwę miasta.")
                miasto = input("Podaj miasto dla którego chcesz sprawdzić pogodę dla danej daty:")
            else:
                break

      data = input("Podaj datę w formacie RRRR-MM-DD (jeśli pole będzie puste program przyjmnie jutrzeszą datę):")

      if data == "":
            jutrszesza_data = datetime.date.today() + datetime.timedelta(days=1)
            data = str(jutrszesza_data)
            print("Program sprawdza pogodę dla jutrzejszej daty:", data)
      else:
            print("Program sprawdza pogodę dla dzisiejszej daty:", data)

      #Zapytanie do API o współrzędne geograficzne miasta i pobranie danych pogodowych
      Pobranie_danych_pogodowych_z_API = WeatherForecast(miasto)
      Godziny, Opady, lat, lon = Pobranie_danych_pogodowych_z_API.Zapytanie_o_pogode_do_API(miasto)

      #Sprawdzenie czy prognoza dla danej daty i miasta jest już w pliku
      Bedzie_padac = False

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
                prognoza = f"Będzie padać ({opad} mm) – {godzina}" 
                print(prognoza)
                Bedzie_padac = True
                Zapis_danych = WeatherForecast("")
                Zapis_danych.Zapisanie_danych_pogodowych_do_pliku(miasto, data, lat, lon, prognoza)
                Prognoza_pogody.append({
                    "Miasto": miasto,   
                    "Data": data,
                    "Szerokosc": lat,
                    "Dlugosc": lon,
                    "Prognoza": prognoza
                })
                break
            elif godzina.startswith(data) and opad == 0:
                prognoza = f"Nie będzie padać – {godzina}"
                print(prognoza)
                Bedzie_padac = True
                Zapis_danych = WeatherForecast("")
                Zapis_danych.Zapisanie_danych_pogodowych_do_pliku(miasto, data, lat, lon, prognoza)
                Prognoza_pogody.append({
                    "Miasto": miasto,   
                    "Data": data,
                    "Szerokosc": lat,
                    "Dlugosc": lon,
                    "Prognoza": prognoza
                })
                break

      if not Bedzie_padac:
            print("Brak danych o opadach dla tej daty lub wartość jest ujemna.")
            prognoza = "Brak danych o opadach dla tej daty lub wartość jest ujemna."
            Zapis_danych = WeatherForecast("")
            Zapis_danych.Zapisanie_danych_pogodowych_do_pliku(miasto, data, lat, lon, prognoza)
            
    case "2":
        print("Wyświetlanie zapisanej prognozy pogody w bazie danych:")
        # for wpis in Prognoza_pogody:
        #     print(f"Miasto: {wpis['Miasto']}, Data: {wpis['Data']}, Szerokość: {wpis['Szerokosc']}, Długość: {wpis['Dlugosc']}, Prognoza: {wpis['Prognoza']}")
        # for date, forecast in Wczytywanie_danych_pogodowych.items():
        #     print(f"Data: {date}, Prognoza: {forecast}")
        print(type(Prognoza_pogody))
        for data, prognoza in Prognoza_pogody.items():
         print(f"Key: {data}, Value: {prognoza}")
        # for miasto, data, lat, lon, prognoza in gen:
        #  print(f"Miasto: {miasto}, Data: {data}, Szerokość: {lat}, Długość: {lon}, Prognoza: {prognoza}")
        


    case "3":
        print("Wyświetlanie prognozy pogody dla danej daty:")
        data_query = input("Podaj datę w formacie RRRR-MM-DD:")
        found = False
        for date, forecast in Wczytywanie_danych_pogodowych.items():
            if date == data_query:
                print(f"Data: {date}, Prognoza: {forecast}")
                found = True
        if not found:
            print(f"Brak prognozy dla daty: {data_query}")
    case "4":
        print("Koniec programu prognozy pogody.")
        break