import logging
import asyncio
import os
import telebot
bot = telebot.TeleBot("1691371768:AAE1T-ieS89l1JKAi6dNOutknH_It7aMDWc")
from bot import bot
from rest import RestBridge
from database import prepare_index
bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
rest = RestBridge(bot)

async def start():
    await prepare_index()
    await rest.start()
    await bot.loop()

username("SuabruMBot")
sync def stop():
    await rest.stop()


if __name__ == '__main__':
    loglevel = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
    logging.basicConfig(level=loglevel)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(stop())
