from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import hug
import requests
import config
import json
import os

TOKEN = os.getenv('TOKEN', config.telegram_token)
APP_NAME = os.getenv('HEROKU_APP_NAME')
bot = Bot(TOKEN)
URL = 'https://{herokuapp}.herokuapp.com/{token}'.format(herokuapp=APP_NAME, token=TOKEN)
payload = {'url': URL}
requests.get('https://api.telegram.org/bot{token}/setWebhook'.format(token=TOKEN), params=payload)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola :v")


def chatid(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_chat.id)


def setup():
    setup_dispatcher = Dispatcher(bot, None, workers=0)
    start_handler = CommandHandler('start', start)
    setup_dispatcher.add_handler(start_handler)
    chatid_handler = CommandHandler('getchatid', chatid)
    setup_dispatcher.add_handler(chatid_handler)
    return setup_dispatcher


dispatcher = setup()


def setwebhook(body):
    update = Update.de_json(json.loads(json.dumps(body)), bot)
    dispatcher.process_update(update)


@hug.get('/ruok')
def ruok():
    return "Yes I am!"


@hug.post('/{token}'.format(token=TOKEN))
def webhook(body):
    setwebhook(body)
    return "Hola!"


@hug.get('/{chat_id}')
def getmensaje(chat_id: hug.types.number, message):
    bot.send_message(chat_id=chat_id, text=message)
    return "Mensaje enviado"


@hug.post('/message')
def post(body):
    chat_id = body.get('chat_id')
    message = body.get('message')
    bot.send_message(chat_id=chat_id, text=message)
    return "Mensaje enviado"
