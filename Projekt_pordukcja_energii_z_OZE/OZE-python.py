from flask import Flask, json, render_template, request
import sys
import pandas as pd
import os

# Inicjalizacja Flask i podlinkowanie do danych z CSV Open Power System Data
app = Flask(__name__)
sys.stdout.reconfigure(encoding="utf-8")
URL = "https://data.open-power-system-data.org/time_series/latest/time_series_60min_singleindex.csv"

# Funkcja do wczytania danych z CSV do lokalnej bazy danych 
def get_data_from_csv(url):
    try:
        # Wczytanie nagłówków kolumn z CSV, aby wybrać tylko te związane z produkcją energii z OZE
        cols = pd.read_csv(url, nrows=0).columns

        # Technolgie OZE, które mają zostać wczytane z CSV i są dostępne w bazie
        tech_keys = [
            "solar_generation_actual",
            "wind_onshore_generation_actual",
            "wind_offshore_generation_actual"
        ]

        # Pozostawnie tylko kolumn z datami oraz te związane z produkcją energii 
        selected_cols = [cols[0]]  

        for c in cols:
            for key in tech_keys:
                if key in c:
                    selected_cols.append(c)

        # Wczytanie danych z CSV z wybranymi kolumnami
        data = pd.read_csv(
            url,
            usecols=selected_cols,
            parse_dates=[0],
            index_col=0
        )

        data.index = data.index.tz_localize(None)

        print(f"Wczytano {len(data.columns)} kolumn OZE")
        return data

    # Wskazanie błędu w przpadku porlbmeów z wczytaniem CSV
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None
    
# Lładowanie danych z CSV do lokalnej bazy danych 
Baza_danych_OZE = get_data_from_csv(URL)

# Sprawdzenie czy dane zostały poprawnie wczytane i wyświetlenie pierwszych kilku wierszy danych z CSV
print("Dane z CSV:")
if Baza_danych_OZE is not None:
    print(Baza_danych_OZE.head())

# Funkcja pobierająca dane OZE
def get_oze_data(country, source, start_date, end_date, freq):

    data = Baza_danych_OZE.copy()

    data.index = data.index.tz_localize(None)

    # Ograniczenie do zakresu dat
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    start_date = max(start_date, data.index.min())
    end_date = min(end_date, data.index.max())

    data = data.loc[start_date:end_date]

    # Mapowanie nazw źródeł OZE z lokalnej bazy danych i powiązanie z wartościami z formularza
    source_map = {
        "solar": "solar_generation_actual",
        "wind_onshore": "wind_onshore_generation_actual",
        "wind_offshore": "wind_offshore_generation_actual"
    }

    if source not in source_map:
        raise ValueError("Nieznany typ OZE")

    # Szukanie odpowiedniej kolumny w danych z klucza
    key = source_map[source]

    cols = [c for c in data.columns if c.startswith(country) and key in c]

    if not cols:
        return pd.DataFrame()
    
    # Zwracanie zadanego źródła OZE z agregacją
    series = (
        data[cols[0]]
        .resample(freq)
        .sum()
        .rename(source)
    )

    return series.to_frame()

# Pobieranie i przetwarzanie danych po przesłaniu formularza za pomocą flask
@app.route("/", methods=["GET", "POST"])
def index():
    country = "None"
    source = "None"
    
    if request.method == "POST":
        freq = request.form.get("Agregacja")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        country = request.form.getlist("country")
        source = request.form.getlist("oze")
        
        # Sprawdzanie poprawności danych wejściowych
        print(freq) 
        print(start_date)
        print(end_date)
        print(country)
        print(source)
        
        # Przetwarzanie danych dla każdego zaznaczonego źródła OZE
        result_data = None
        
        for src in source:   
            print("Akutalnie przetwarzane źródło OZE:", src)
            
            # Tymczasowe przechowywanie danych OZE
            data_temp = get_oze_data(country[0], src, start_date, end_date, freq)

            # Sprawdzenie czy dane są w CSV i poprawnie pobrane i kontynyacja przetwarzania jeśli ich nie ma aby uniknąć komunikatu o błędize w pandas
            if data_temp is None:
                print(f"Brak danych (None) dla {src}")
                continue

            if data_temp.empty:
                print(f"Pusty DataFrame dla {src}")
                continue

            # Restowanie indexkowania dannych oraz zmiania koluny z datami na date
            data_temp = data_temp.reset_index()

            if "utc_timestamp" in data_temp.columns:
                data_temp = data_temp.rename(columns={"utc_timestamp": "date"})

            # Zmiana nazwy kolumny z wynikami na wybrane technologie OZE
            value_columns = [c for c in data_temp.columns if c not in ["date"]]
            if len(value_columns) != 1:
                print("Nieoczekiwane kolumny:", data_temp.columns)
                continue

            data_temp = data_temp.rename(columns={value_columns[0]: src})
            
            # Łączenie danych o produkcji OZE z wybranych OZE do jedenej tabeli 
            if result_data is None:
                result_data = data_temp
            else:
                result_data = pd.merge(result_data, data_temp, on="date", how="outer")

        # W przypadku braku danych dla wybranego kraju / zakresu dat zostanie zwrócony komunikat o błędzie (pandas nie wywali błędu, co może mylić użytkownika)
        if result_data is None:
            print("Error: result_data dalej puste, dane nie zostały znalezione w bazie danych dla wybranych parametrów w OPSD")
            result_data = pd.DataFrame()
            print("Brak danych w bazie dla wybranego kraju / zakresu dat")
       
            return render_template(
                "Dane_oze.html",
                error_msg="Brak danych w bazie dla wybranego kraju, technologii OZE lub zakresu dat!! Wybierz inne parametry.",
            )

        # Wyświetlanie końcowych danych w konsoli dla sprawdzenia porawności wczytywania danych przez html/flask
        print("Ostateczne result_data:")
        print(result_data.head())
        print(result_data.columns)

        # Zamiania daty na stringi, uzupełnianie brakujących danych zerami oraz zapisanie do pliku JSON w folderze static/data
        result_data["date"] = result_data["date"].astype(str)
        result_data = result_data.fillna(0)
        json_path = os.path.join(app.static_folder, "data", "Dane_energetyczne.json")

        # Zmiania nazw kolmun na bardziej przyjazne dla użytkownika oraz sortowanie danych po dacie
        result_data = result_data.sort_values("date")
        result_data = result_data.rename(columns={"date": "Data"})
        result_data = result_data.rename(columns={"solar": "Energia słoneczna, MWh"})
        result_data = result_data.rename(columns={"wind_offshore": "Energia wiatrowa morska, MWh"})
        result_data = result_data.rename(columns={"wind_onshore": "Energia wiatrowa lądowa, MWh"})

        result_data.to_json(
            json_path,
            orient="records",
            date_format="iso",
            force_ascii=False
        )
        print("Zapisano Dane_energetyczne.json")


    return render_template("Dane_oze.html", Kraj=country[0])

if __name__ == "__main__":
    app.run(debug=True)
    

