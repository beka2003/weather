import requests

city = "Moscow,RU"
appid = "bde816a9134cfdfb0d91449aba12c8f8"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

for i in data['list']:
    print(
        "--------------------------------",
        "\r\nДата <", i['dt_txt'],
          "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),"°C",
          "> \r\nПогодные условия <", i['weather'][0]['description'],
          "> \r\nСкорость ветра <", i['wind']['speed'], "м/c",
          "> \r\nВидимость <", i['visibility'] / 1000,"км >"
          )