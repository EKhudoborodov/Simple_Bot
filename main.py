import telebot, random
from telebot import types
from random import randint

token = "5099243948:AAHSqJ6pYg-H3t72GutcgXL1tgbkqz1Sbvw"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу новости", "Покажи работы", "Погода", "Включи телевизор", "/help", "/calculate")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '/calculate - Я могу проводить простые операции с двумя числами.\n/print - Могу написать несколько случайных символов.\n/d1roll - Могу кинуть кубик.\n/d2roll - Могу кинуть два кубика.\n\nНапиши "Хочу новости", чтобы посмотреть новости о МТУСИ.\nНапиши "Покажи работы", чтобы посмотреть остальные работы.\nНапиши "Погода", чтобы посмотреть прогноз погоды.\nТакже можешь написать "Включи телевизор", чтобы посмотреть видео с сайта YouTube.')

@bot.message_handler(commands=['print'])
def start(message):
    letters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890'
    y = randint(4,25)
    result = ''
    for r in range(y):
        x = random.choice(letters)
        result += x
    bot.send_message(message.chat.id, f"Смотри, что получилось - {result}")

@bot.message_handler(commands=['d1roll'])
def start(message):
    numbers = '123456'
    x = random.choice(numbers)
    bot.send_message(message.chat.id, f"Выпало - {x}")

@bot.message_handler(commands=['d2roll'])
def start(message):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    x = random.choice(numbers)
    bot.send_message(message.chat.id, f"Выпало - {x}")

@bot.message_handler(commands=['calculate'])
def start_message(message):
    bot.send_message(message.chat.id, 'Что нужно посчитать?')
def convert_number(n, i):
    first = 0
    j = i - 1
    while n >= 1:
        first += (n % 10) * (10 ** j)
        j = j - 1
        n = int(n / 10)
    return first
def convert_message(text):
    i, n = 0, 0
    for char in text:
        if char == '1':
            n += 10 ** i
            i += 1
            continue
        if char == '2':
            n += 2 * (10 ** i)
            i += 1
            continue
        if char == '3':
            n += 3 * (10 ** i)
            i += 1
            continue
        if char == '4':
            n += 4 * (10 ** i)
            i += 1
            continue
        if char == '5':
            n += 5 * (10 ** i)
            i += 1
            continue
        if char == '6':
            n += 6 * (10 ** i)
            i += 1
            continue
        if char == '7':
            n += 7 * (10 ** i)
            i += 1
            continue
        if char == '8':
            n += 8 * (10 ** i)
            i += 1
            continue
        if char == '9':
            n += 9 * (10 ** i)
            i += 1
            continue
        if char == '+' or char == '-' or char == '*' or char == '/':
            first = convert_number(n, i)
            i, n = 0, 0
            sim = char
    second = convert_number(n, i)
    if sim == '+':
        res = first + second
    elif sim == '-':
        res = first - second
    elif sim == '*':
        res = first * second
    elif sim == '/':
        res = first / second
    return res
def answer(message):
    bot.send_message(message.chat.id, f"Результат - {convert_message(message.text)}")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу новости":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "покажи работы":
        bot.send_message(message.chat.id, 'Треугольник - https://github.com/EKhudoborodov/Triangle\nПереводчик - https://github.com/EKhudoborodov/Project1\nФласк БД - https://github.com/EKhudoborodov/MyWebApp')
    elif message.text.lower() == "включи телевизор":
        bot.send_message(message.chat.id, 'Включаю - https://www.youtube.com/')
    elif message.text.lower() == "спасибо":
        bot.send_message(message.chat.id, 'https://youtu.be/ZIYoUx8NZts')
    elif message.text.lower() == "погода" or message.text.lower() == "прогноз погоды":
        bot.send_message(message.chat.id, 'Прогноз погоды в Москве - https://yandex.ru/pogoda/?lat=55.75581741&lon=37.61764526')
    else:
        def convert_number(n, i):
            num = 0
            j = i - 1
            while n>=1:
                num += (n % 10) * (10 ** j)
                j = j - 1
                n = int(n / 10)
            return num
        def convert_message(text):
            i, n = 0, 0
            for char in text:
                if char == '1':
                    n += 10 ** i
                    i += 1
                    continue
                if char == '2':
                    n += 2 * (10 ** i)
                    i += 1
                    continue
                if char == '3':
                    n += 3 * (10 ** i)
                    i += 1
                    continue
                if char == '4':
                    n += 4 * (10 ** i)
                    i += 1
                    continue
                if char == '5':
                    n += 5 * (10 ** i)
                    i += 1
                    continue
                if char == '6':
                    n += 6 * (10 ** i)
                    i += 1
                    continue
                if char == '7':
                    n += 7 * (10 ** i)
                    i += 1
                    continue
                if char == '8':
                    n += 8 * (10 ** i)
                    i += 1
                    continue
                if char == '9':
                    n += 9 * (10 ** i)
                    i += 1
                    continue
                if char == '0':
                    i += 1
                    continue
                if char == '+' or char == '-' or char == '*' or char == '/':
                    first = convert_number(n, i)
                    i, n, zeroes = 0, 0, 0
                    sim = char
                    continue
                bot.send_message(message.chat.id, "Повторите, я не смог вас понять. =(")
                break
            second = convert_number(n, i)
            if sim == '+':
                res = first + second
            elif sim == '-':
                res = first - second
            elif sim == '*':
                res = first * second
            elif sim == '/':
                res = first / second
            return res
        bot.send_message(message.chat.id, f"Результат - {convert_message(message.text)}")

bot.polling(none_stop=True)