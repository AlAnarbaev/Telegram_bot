# Импортируем необходимые классы из aiogramm

from aiogram import Bot, Dispatcher, executor, types

# Импортируем библиотеку random
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pytube import YouTube

import os

import random

import keyboards

import logging

import config

# import sqlite3

# Создаем переменную, содержащую токен бота, полученный из BotFather в Telegram

token = config.token

# Создаем экземпляр класса Бот, указываем переменную в качестве аргумента

my_bot = Bot(token)

# Создаем экземпляр класса Диспетчер, указываем объект my_bot в качестве аргумента

dp = Dispatcher(my_bot, storage=MemoryStorage())
storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)



# connect = sqlite3.connect('users.db')
# cursor = connect.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS users(
#     username VARCHAR(255),
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     id_user INTEGER,
#     chat_id INTEGER
#     );
#     """)
# connect.commit()

# Добавляем обработчик для команды старт

@dp.message_handler(commands='start')
async def start(message: types.Message):
    # cursor = connect.cursor()
    # cursor.execute(f"SELECT id_user FROM users WHERE id_user = {message.from_user.id};")
    # res = cursor.fetchall()
    # if res == []:
    #     cursor.execute(f"""INSERT INTO users VALUES ('{message.from_user.username}',
    #         '{message.from_user.first_name}', '{message.from_user.last_name}',
    #         {message.from_user.id}, {message.chat.id})""")
    # connect.commit()

    await message.answer(f'Здравствуйте {message.from_user.full_name}!\n'
                         f'Тут вы можете получить информацию о курсах программирования в Geektech.\n\n'
                         f'Чтобы посмотреть список курсов, введите команду /help\nили команды /audio или /video, чтобы скачать аудио или видео по ссылке с Youtube\n'
                         f'А еще я загадал число от 1 до 3, попробуйте отгадать')#, reply_markup = keyboards.greet_kb)

def downloader(url, type):
    yt = YouTube(url)
    if type == "video":
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            "video", f"{yt.title}.mp4")
        return f"{yt.title}.mp4"
    elif type == "audio":
        yt.streams.filter(only_audio=True).first().download("audio", f"{yt.title}.mp3")
        return f"{yt.title}.mp3"

class DownloadVideo(StatesGroup):
            download = State()

class DownloadAudio(StatesGroup):
            download = State()

@dp.message_handler(commands='video')
async def video(msg:types.Message):
    await msg.answer(f"Отправьте ссылку и я вам его скачаю")
    await DownloadVideo.download.set()

@dp.message_handler(commands='audio')
async def audio(msg:types.Message):
    await msg.answer(f"Отправьте ссылку и я вам скачаю его в mp3")
    await DownloadAudio.download.set()

@dp.message_handler(state=DownloadVideo.download)
async def download_video_state(msg:types.Message, state:FSMContext):
    try:
        await msg.answer("Скачиваем видео, ожидайте...")
        title = downloader(msg.text, "video")
        video = open(f'video/{title}', 'rb')
        try:
            await msg.answer("Все скачалось, вот видео")
            await my_bot.send_video(msg.chat.id, video)
        except Exception as error:
            await msg.answer(f"Произошла ошибка, повторите еще раз. {error}")
            await state.finish()
    except:
        await msg.answer("Ссылка не верна!")
        await state.finish()
    os.remove(f'video/{title}')

@dp.message_handler(state=DownloadAudio.download)
async def download_audio_state(msg:types.Message, state:FSMContext):
    try:
        await msg.answer("Скачиваем аудио, ожидайте...")
        title = downloader(msg.text, "audio")
        audio = open(f'audio/{title}', 'rb')
        try:
            await msg.answer("Все скачалось, вот аудио")
            await my_bot.send_audio(msg.chat.id, audio)
        except Exception as error:
            await msg.answer(f"Произошла ошибка, повторите еще раз. {error}")
        await state.finish()
    except:
        await msg.answer("Ссылка не верна!")
        await state.finish()
    os.remove(f'audio/{title}')


# Добавляем обработчик для команды help

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply(f"<b>Список курсов програмирования в Geektech</b> :\n\n"
                        f"<b>/backend</b>   - Backend-разработчик\n"
                        f"<b>/frontend</b>   - Frontend-разработчик\n"
                        f"<b>/uxui</b>           - UX/UI-дизайнер\n"
                        f"<b>/android</b>     - Android-разработчик\n"
                        f"<b>/ios</b>             - iOS-разработчик", parse_mode='HTML')
    await message.delete()
# Добавляем обработчик для команды старт

@dp.message_handler(text=range(1,4))
async def number_check(message: types.Message):

    # Создаем переменную number со случайным значением из диапазона 1-3

    number = random.randrange(1, 4)

    if int(message.text) == number:
            await message.reply('Правильно, вы отгадали')
    else:
            await message.reply(f'Неправильно, я загадывал число {number}')

# ДЗ3

# Добавляем обработчик для команды backend

@dp.message_handler(commands='backend')
async def backend(message: types.Message):
    await message.reply(f"<b>Backend-разработчик</b>\n\n"
                         f"Станьте Backend-разработчиком на языке программирования Python с нуля.\n"
                         f"<b>Cтоимость курса:</b>\n10000 сом/мес\n"
                         f"<b>Продолжительность курса:</b>\n5 месяцев", parse_mode='HTML')
    await message.delete()

# Добавляем обработчик для команды frontend

@dp.message_handler(commands='frontend')
async def backend(message: types.Message):
    await message.reply(f"<b>Frontend-разработчик</b>\n\n"
                         f"Научитесь с нуля создавать сайты любой сложности и веб-приложения, с помощью языка программирования JavaScript.\n"
                         f"<b>Cтоимость курса:</b>\n10000 сом/мес\n"
                         f"<b>Продолжительность курса:</b>\n5 месяцев", parse_mode='HTML')
    await message.delete()

# Добавляем обработчик для команды uxui

@dp.message_handler(commands='uxui')
async def backend(message: types.Message):
    await message.reply(f"<b>UX/UI-дизайнер</b>\n\n"
                         f"Вы научитесь создавать дизайн веб-сайтов и мобильных приложений. Освоите сервис Figma и сможете закрепить полученные знания на практике.\n"
                         f"<b>Cтоимость курса:</b>\n10000 сом/мес\n"
                         f"<b>Продолжительность курса:</b>\n3 месяца", parse_mode='HTML')
    await message.delete()

# Добавляем обработчик для команды android

@dp.message_handler(commands='android')
async def backend(message: types.Message):
    await message.reply(f"<b>Android-разработчик</b>\n\n"
                         f"Научитесь с нуля создавать мобильные приложения под операционную систему Android на языках программирования Java и Kotlin.\n"
                         f"<b>Cтоимость курса:</b>\n10000 сом/мес\n"
                         f"<b>Продолжительность курса:</b>\n7 месяцев", parse_mode='HTML')
    await message.delete()

# Добавляем обработчик для команды ios

@dp.message_handler(commands='ios')
async def backend(message: types.Message):
    await message.reply(f"<b>iOS-разработчик</b>\n\n"
                         f"Научитесь с нуля создавать мобильные приложения под операционную систему iOS на языке программирования Swift.\n"
                         f"<b>Cтоимость курса:</b>\n10000 сом/мес\n"
                         f"<b>Продолжительность курса:</b>\n7 месяцев", parse_mode='HTML')
    await message.delete()




if __name__ == '__main__':
    executor.start_polling(dp)



