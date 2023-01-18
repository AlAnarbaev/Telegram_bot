# Импортируем необходимые классы из aiogramm

from aiogram import Bot, Dispatcher, executor, types

# Импортируем библиотеку random

import random

import keyboards

# import sqlite3

# Создаем переменную, содержащую токен бота, полученный из BotFather в Telegram

token = "5555418010:AAHYAkV6ZPt5ZKqAovArDYUJ9nMn7jFfum8"

# Создаем экземпляр класса Бот, указываем переменную в качестве аргумента

my_bot = Bot(token)

# Создаем экземпляр класса Диспетчер, указываем объект my_bot в качестве аргумента

dp = Dispatcher(my_bot)

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
                         f'Чтобы посмотреть список курсов, введите команду /help или выберите кнопку с интересующим курсом ниже\n'
                         f'А еще я загадал число от 1 до 3, попробуйте отгадать', reply_markup = keyboards.greet_kb)
    await message.delete()

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



