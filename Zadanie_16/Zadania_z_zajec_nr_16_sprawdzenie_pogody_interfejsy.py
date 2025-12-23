# Zoptymalizuj kod z poprzedniego zadania z pogodą.

# Utwórz klasę WeatherForecast, która będzie służyła do odczytywania i zapisywania pliku, a także odpytywania API. DONE

# Obiekt klasy WeatherForecast dodatkowo musi poprawnie implementować cztery metody:

#  __setitem__ DONE
#  __getitem__
#  __iter__ DONE
#  items DONE

# Wykorzystaj w kodzie poniższe zapytania:

# weather_forecast[date] da odpowiedź na temat pogody dla podanej daty DONE
# weather_forecast.items() zwróci generator tupli w formacie (data, pogoda) dla już zapisanych rezultatów przy wywołaniu DONE
# weather_forecast to iterator zwracający wszystkie daty, dla których znana jest pogoda

import sys
import datetime
from Weather_Forecast import WeatherForecast
sys.stdout.reconfigure(encoding="utf-8")

#Wczytanie danych pogodowych z pliku
Baza_prognozy_pogody = WeatherForecast.Wczytanie_danych_pogody("Prognoza_pogody.txt")

#Wyświetlenie wczytanej prognozy pogody
for (miasto, data, szer, dlug), prognoza in Baza_prognozy_pogody.items():
    print(miasto, data, prognoza)


while True:
 komenda = input("""Lista dostępnych komend w programnie prognozy pogody (wybierz numer komendy): 
    1. Sprawdź pogodę dla danego dnia i miasta 
    2. Wyświetl zapisaną prognozę pogody w bazie danych
    3. Wyświetl wszystkie daty i prognozy pogody z bazy danych, dla których znana jest pogoda
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
      Pobranie_danych_pogodowych_z_API = WeatherForecast()
      Godziny, Opady, lat, lon = Pobranie_danych_pogodowych_z_API.Zapytanie_o_pogode_do_API(miasto)
    #   Baza_prognozy_pogody = WeatherForecast.Wczytanie_danych_pogody("Prognoza_pogody.txt")

      #Sprawdzenie czy prognoza dla danej daty i miasta jest już w pliku
      Bedzie_padac = False

      for wpis in Baza_prognozy_pogody.items():  
        if miasto == wpis[0][0] and data == wpis[0][1]:
              print("Prognoza pogody dla miasta", miasto, "i daty", data, "jest już w bazie danych:")
              print("Prognoza:", wpis[1])
              Bedzie_padac = True
              break
            
     #Pozyskanie prognozy z API i zapisa do pliku
      for godzina, opad in zip(Godziny, Opady):
            if godzina.startswith(data) and opad > 0:
                prognoza = f"Będzie padać ({opad} mm) – {godzina}" 
                print(prognoza)
                Bedzie_padac = True
                Baza_prognozy_pogody[miasto, data, lat, lon] = prognoza
                break
            elif godzina.startswith(data) and opad == 0:
                prognoza = f"Nie będzie padać – {godzina}"
                print(prognoza)
                Bedzie_padac = True
                Baza_prognozy_pogody[miasto, data, lat, lon] = prognoza
                break

      if not Bedzie_padac:
            print("Brak danych o opadach dla tej daty lub wartość jest ujemna.")
            prognoza = "Brak danych o opadach dla tej daty lub wartość jest ujemna."
            Baza_prognozy_pogody[miasto, data, lat, lon] = prognoza
            
    case "2":
        print("Wyświetlanie zapisanej prognozy pogody w bazie danych:")
        for (miasto, data, szer, dlug), prognoza in Baza_prognozy_pogody.items():
            print(miasto, data, prognoza)

    case "3":
       #tUTAJ PORAWKA MA ZWRAĆ DATY DLA ZNANEJ PROGNOZY POGODY PLUS GET ITEM
       #weather_forecast to iterator zwracający wszystkie daty, dla których znana jest pogoda
      for (miasto, data, szer, dlug), prognoza in Baza_prognozy_pogody.items():
          if prognoza != "Brak danych o opadach dla tej daty lub wartość jest ujemna.":
             print(f"Dla miasta: {miasto} i daty: {data} prognoza pogody to: {prognoza}")
    
    case "4":
     print("Koniec programu prognozy pogody. Dane zostały zapisane do pliku txt.")
     Zapis = WeatherForecast()
     Zapis.Zapisanie_danych_pogodowych_do_pliku(Baza_prognozy_pogody)
     exit()