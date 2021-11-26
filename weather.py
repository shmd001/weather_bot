import pyowm
import config

class Weather():
    def __init__(self):
        owm = pyowm.OWM(config.api_key)
        mgr = owm.weather_manager()
        
    def get_weather(self, city):
        observation = self.mgr.weather_at_place(city)
        w = observation.weather
        
        temperature = w.temperature('celcius')['temp']
        
        return temperature