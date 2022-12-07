import requests

city = "Moscow,RU"
appid = "bde816a9134cfdfb0d91449aba12c8f8"


res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()


print("Город:", data['name'])
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", '{0:+3.0f}'.format(data['main']['temp']),"°C")
print("Давление:", data['main']['pressure'])
print("Температура по ощущениям:", '{0:+3.0f}'.format(data['main']['feels_like']),"°C")
print("Минимальная температура:", '{0:+3.0f}'.format(data['main']['temp_min']),"°C")
print("Максимальная температура", '{0:+3.0f}'.format(data['main']['temp_max']),"°C")
print("Скор.ветра:", data['wind']['speed'],'м/c')
print("Видимость", data['visibility']/1000,'км')