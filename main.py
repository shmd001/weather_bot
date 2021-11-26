import telebot
import config
from weather import Weather

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, config.start_message)
    

@bot.message_handler(content_types=['text'])
def weather_message(message):
    bot.send_message(message.from_user.id, Weather().get_temperature(message.text))

if __name__ == '__main__':
    bot.polling(none_stop=True)
