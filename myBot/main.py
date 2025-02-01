from aiogram import Bot, Dispatcher, executor
import asyncio
import time
from aiogram import types
from datetime import datetime

import handlers
import gettime
import get_comm
 
API_TOKEN = '8079636146:AAGihQJ-Vfzse59rGP6TnOj3BiPo1q_eOFo'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(handlers.help, commands=["help"])
dp.register_message_handler(get_comm.get_com, content_types=['photo'])
dp.register_message_handler(get_comm.get_com, commands=["sosal"])

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await bot.send_message(message.chat.id, 
                           '@all Готовы сосать, господа? ')
    global time_sos
    time_sos = gettime.get_time()
    while True:
        await asyncio.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == time_sos: 
            time_sos = gettime.get_time()
            await bot.send_message(message.chat.id, 
                                   '@all Время сосать, господа!!! ') 
            
@dp.message_handler(commands=['check'])
async def check(message: types.Message):
    await message.answer(f" Время следующего сосания: " + time_sos)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
