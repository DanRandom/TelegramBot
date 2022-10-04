import telebot
from flask import Flask, request
import os


TOKEN = '' #TOKEN is removed for privacy
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello')

@bot.message_handler(commands=['info'])
def get_info(message):
    chid = message.chat.id
    bot.send_message(chid, updates)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    chid = message.chat.id
    mid = message.message_id
    if message.text:
        bot.send_message(chid, message.text)

def photoMessage(message):
    chid = message.chat.id;
    bot.send_message(chid, "IMAGE WAS SENT!!!!")

@bot.message_handler(content_types=['photo'])
def photo(message):
    photoMessage(message)


@bot.message_handler(commands=['chatid'])
def show_id(message):
    cid = message.chat.id
    bot.reply_to(message, cid)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://serene-falls-89714.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
