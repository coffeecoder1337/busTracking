import os
import telebot
from bus_getter import BusGetter
from dotenv import load_dotenv
from parser import Parser
from telebot import types


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
to_home_url = 'https://tagiltram.ru/bus-58-2'
from_home_url = 'https://tagiltram.ru/bus-58-1'

bot = telebot.TeleBot(BOT_TOKEN)

to_home = Parser(to_home_url)
from_home = Parser(from_home_url)


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('От вокзала')
    button2 = types.KeyboardButton('От северного')
    button3 = types.KeyboardButton('Ближайшее')
    keyboard.add(button1, button2, button3)

    bot.reply_to(message, 'Привет, Дашулик! Я тебя лублу <3', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'От вокзала':
        to_home_times = to_home.parse_time()
        to_home_times_str = '\n'.join([t for t in to_home_times])

        response = f'От вокзала:\n{to_home_times_str}'

        bot.reply_to(message, response)

    elif message.text == 'От северного':
        from_home_times = from_home.parse_time()
        from_home_times_str = '\n'.join([t for t in from_home_times])

        response = f'От северного:\n{from_home_times_str}'

        bot.reply_to(message, response)

    elif message.text == 'Ближайшее':
        to_home_times = BusGetter.get_next_three_bus(to_home.parse_time())
        from_home_times = BusGetter.get_next_three_bus(from_home.parse_time())

        to_home_times_str = '\n'.join([t for t in to_home_times])
        from_home_times_str = '\n'.join([t for t in from_home_times])

        response = f'От вокзала:\n{to_home_times_str}\n\nОт северного:\n{from_home_times_str}'

        bot.reply_to(message, response)


