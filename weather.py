import config
import requests

class Weather():
    """Отвечает за работу с погодой"""
    
    def __init__(self):
        pass
        
    def get_temperature(self, city):
        """Возвращает погоду в указанном месте

        Args:
            city (str): Место, в котором необходимо узнать погоду

        Returns:
            str: Погода в нужном месте
        """
        
        # Получение ответа от API
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={config.API_KEY}'
        )
        
        # Обработка JSON ответа
        data = r.json()
        if data['cod'] != 200:
            return 'Город не найден'
        
        # Получение температуры
        temperature = round(data['main']['temp'])
        
        return f'В городе {city} сейчас {temperature}˚C'
