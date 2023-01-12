import telebot
import requests
import json

from CryptoBot.extensions import APIException

exchanges = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}
TOKEN = "5777034290:AAGH_jhwcEOdziz_qVn1B_huidp_CCnxqbY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Введите 2 валюты и коливество через пробел в формате USD EUR RUB!"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):


    base, sym, amount = message.text.split()
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym}&from={base}&amount={amount}"
    headers = {
        "apikey": "RfeFJ3jLcVOYevESQOhw1cLMf4aaiGaJ"
    }

    r = requests.get(url, headers=headers)
    resp = json.loads(r.content)
    new_price = resp['result']
    bot.reply_to(message, f"Цена {amount} {base} в {sym} : {new_price}")


bot.polling()