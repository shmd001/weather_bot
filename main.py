import telebot
import config
from weather import Weather

# Инициализация бота
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    """Отвечает на /start

    Args:
        message : Сообщение пользователя
    """
    bot.send_message(message.from_user.id, config.start_message)
    

@bot.message_handler(content_types=['text'])
def weather_message(message):
    """Сообщает погоду в указанном месте

    Args:
        message : Сообщение пользователя
    """
    bot.send_message(message.from_user.id, Weather().get_temperature(message.text))

if __name__ == '__main__':
    bot.polling(none_stop=True)
