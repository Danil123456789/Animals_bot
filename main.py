import telebot

API_TOKEN = '769315655:AAHVPC5zj8hNKDWOASNQMSRvfUgFbsxLXhA'  # TODO: Вставьте сюда API_TOKEN вашего бота

START_STICKER = 'CAACAgIAAxkBAAEBaLlfeFX9DYLP1SI5ft08oNiWUqkv6QACGAADwDZPE9b6J7-cahj4GwQ'  # @Stiker_id_bot поможет
WIN_STICKER = 'CAACAgIAAxkBAAEBaLdfeFXjjIqK3cCUSgABSJOKYkTLmfUAAhUAA8A2TxPNVqY7YZ5k5xsE'
RIGHT_ANSWER = 5

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, START_STICKER)
    bot.send_message(message.from_user.id, "Привет! Введи название любого животного")

list_stickers = []

list_animals = ['Бизон', 'Дельфин', 'Орёл', 'Пони', 'Человек', 'Омар', 'Обезьяны', 'Носорог', 'Олени',
                'Утка', 'Тигр', 'Паук', 'Волк', 'Индейка', 'Лев', 'Свинья', 'Змея', 'Акула', 'Птица', 'Медведь',
                'Рыба', 'Горилла', 'Лошадь', 'Кот', 'Собака', 'Еж', 'Жираф', 'Хамелион', 'Цапля']


@bot.message_handler(content_types=['text'])
def start(message):
    text = message.text
    for i in list_animals:
        if i.lower() == text.lower():
            bot.send_sticker(message.chat.id, WIN_STICKER)
            break

@bot.message_handler(content_types=['voice'])
def start_message(message):
    bot.send_message(message.from_user.id, "Не слышуууу. Ничего не слышу. Глуховат я :(")


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.from_user.id, "Картинки какие-то шлют. Ничего не понимаю...")


@bot.message_handler(content_types=['document'])
def start_message(message):
    bot.send_message(message.from_user.id, "Ой, вот только файлы мне тут не надо слать!")


bot.polling()
