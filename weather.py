import config
import requests

class Weather():
    def __init__(self):
        pass
        
    def get_temperature(self, city):
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={config.api_key}')
        data = r.json()
        
        if data['cod'] != 200:
            return 'Город не найден'
        
        temperature = round(data['main']['temp'])
        
        return f'В городе {city} сейчас {temperature}˚C'
