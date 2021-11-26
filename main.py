import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, config.start_message)
    
@bot.message_handler(commands=['weather'])
def weather_message(message):
    pass

if __name__ == '__main__':
    bot.polling(none_stop=True)
