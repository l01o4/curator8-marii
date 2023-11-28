import telebot

bot = telebot.TeleBot('6609721607:AAFwAC6LaZz_UAZutdqGGCDgKHeu9h6K2bM')


@bot.message_hendler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_hendler(commands=['fact1'])
def main(message):
    bot.send_message(message.chat.id,
                     'Только 19% людей отправляют смайлики, которые реально характеризуют их настроение')


@bot.message_hendler(commands=['fact2'])
def main(message):
    bot.send_message(message.chat.id, 'Вы не можете дышать через нос, если ваш язык высунут')


@bot.message_hendler(commands=['Further'])
def main(message):
    bot.send_message(message.chat.id,
                     'Вы только что это попробовали и поняли, что можете дышать, но при этом похожи на собаку')


@bot.message_hendler(commands=['Now'])
def main(message):
    bot.send_message(message.chat.id,
                     'А теперь вы улыбаетесь \n*Улыбайтесь чаще ведь улыбка причина хорошего настроения*',
                     parse_mode='Markdown')


bot.infinity_polling()