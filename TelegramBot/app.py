import telebot
from config import token, keys
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = '\n'.join((
        f'Привет, {message.chat.username}!',
        'Я бот, который конвертирует валюту. Чтобы начать мною пользоваться, введите: ',
        '<имя валюты> <имя валюты, в какую хотите перевести> <количество переводимой валюты>',
        ' ',
        'ВАЖНО!!! Название валюты вводится с маленькой буквы!',
        'Узнать мои возможности: /help'
))
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать пользоваться ботом, введите: /start или \n' \
           '<имя валюты> <имя валюты, в какую хотите перевести> <количество переводимой валюты> \n' \
           'Чтобы узнать, какие валюты я могу конвертировать: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n' + '\n'.join(keys.keys())
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком мало или много параметров (должно быть 3).')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}.')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()