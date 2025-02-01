import random as rd
from aiogram import types

f = open("C:/My/SosaBot/myBot/commentSos.txt", "+r", encoding="utf-8")
comment = f.readlines()
f.close()
flag_sosaniy = True

async def get_com(message: types.Message):
    if message.content_type == 'photo' and (message.text == '/sosal' or message.caption =='/sosal'):
        await message.answer(rd.choice(comment))
    elif message.content_type != 'photo' and message.text == '/sosal':
        await message.answer(' Видимо ты орально фиксируешься недостаточно!\nБыстро прислал фото! ')

async def get_comSOS(message: types.Message):
    if message.content_type == 'photo' and (message.text == '/sosal' or message.caption =='/sosal'):
        global flag_sosaniy 
        flag_sosaniy = False
        await message.answer(rd.choice(comment))
    else:
        await message.answer(' Видимо ты орально фиксируешься недостаточно!\nБыстро прислал фото! '), True
