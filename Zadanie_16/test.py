
class WeatherForecast:
 def __init__(self):
     self._data = {}

 def items(self):
     return self._data.items()
 
def load_from_txt(path):
     forecast = WeatherForecast()

     with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            miasto, data, szerokosc, dlugosc, prognoza = line.split(",")
            forecast._data[(miasto, data, szerokosc, dlugosc)] = prognoza

     return forecast

weather_forecast = load_from_txt("Prognoza_pogody.txt")

print(type(weather_forecast))
print(weather_forecast._data)

for data, prognoza in weather_forecast.items():
    print(data, prognoza)


