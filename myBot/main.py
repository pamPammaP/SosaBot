from aiogram import Bot, Dispatcher, executor
import asyncio
import time
from aiogram import types
from datetime import datetime

import handlers
import gettime
import get_comm
import bd
 
API_TOKEN = '8079636146:AAGihQJ-Vfzse59rGP6TnOj3BiPo1q_eOFo'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

bd.db_create()

dp.register_message_handler(handlers.help, commands=["help"])
dp.register_message_handler(get_comm.get_com, content_types=['photo'])
dp.register_message_handler(get_comm.get_com, commands=["sosal"])

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 
                           '@all Готовы сосать, господа? ')
    global time_sos
    time_sos = gettime.get_time()
    bd.write_chat(time_sos, chat_id)
    while True:
        await asyncio.sleep(60)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        time_sos1 = bd.get_time(chat_id)
        if current_time == time_sos1: 
            time_sos = gettime.get_time()
            bd.write_time(time_sos, chat_id)
            await bot.send_message(message.chat.id, 
                                   '@all Время сосать, господа!!! ') 
            
@dp.message_handler(commands=['check'])
async def check(message: types.Message):
    chat_id = message.chat.id

    await message.answer(f" Время следующего сосания: " + bd.get_time(chat_id)[0])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
