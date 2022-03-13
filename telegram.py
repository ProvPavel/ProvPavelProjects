import telebot
from requests import request
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5244170384:AAFC6tWiMobzeiOGTg-e6zAApAvfvv8MKnE')
LOGS = {}


@bot.message_handler(commands=['logs'])
def logs(message):
    if message.from_user.id == 1963745858:
        for user in LOGS.keys():
            info = '\n'.join(LOGS[user])
            bot.send_message(message.chat.id, f'{user}\n{info}')


@bot.message_handler(commands=['clear'])
def clear(message):
    if message.from_user.id == 1963745858:
        global LOGS
        LOGS = {}


@bot.message_handler(commands=['start'])
def start(message):
    info = f'Привет, {message.from_user.first_name} {message.from_user.last_name}!' \
           f'Доступные команды:\n/news\n/travel'
    bot.send_message(message.chat.id, info)
    if message.from_user.id not in LOGS.keys():
        LOGS[message.from_user.id] = []
    LOGS[message.from_user.id].append('start')


@bot.message_handler(commands=['news'])
def news(message):
    url = 'https://yandex.ru/news?msid=1645874415555541-10935585541354775902-sas5-9946-38a-sas-l7-balancer-8080-BAL-8146&mlid=1645873938.glob_225&utm_source=morda_desktop&utm_medium=topnews_news'
    html = request(method='GET', url=url).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.find_all('div', class_='mg-card__annotation')[:5:]:
        bot.send_message(message.chat.id, i.text)
    if message.from_user.id not in LOGS.keys():
        LOGS[message.from_user.id] = []
    LOGS[message.from_user.id].append('news')


@bot.message_handler(commands=['travel'])
def travel(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Yandex', url='https://yandex.ru'))
    markup.add(telebot.types.InlineKeyboardButton('Google', url='https://google.com'))
    markup.add(telebot.types.InlineKeyboardButton('VK', url='https://vk.com'))
    bot.send_message(message.chat.id, 'Доступные пути:', reply_markup=markup)
    if message.from_user.id not in LOGS.keys():
        LOGS[message.from_user.id] = []
    LOGS[message.from_user.id].append('travel')


bot.polling(non_stop=True)
