"""
1) Напишите телеграмм бот который загадывает случайное число с помощью
библиотеки random и вы должны угадать его.
Бот:
Я загадал число от 1 до 3 угадайте
Пользователь:
Вводит число 2, если число правильное то выводит “Правильно вы отгадали”
ДОП ЗАДАНИЕ:
2) Загрузить файлы в GitHub
"""

# Импортируем необходимые классы из aiogramm

from aiogram import Bot, Dispatcher, executor, types

# Импортируем библиотеку random

import random

# Создаем переменную, содержащую токен бота, полученный из BotFather в Telegram

token = "5555418010:AAHYAkV6ZPt5ZKqAovArDYUJ9nMn7jFfum8"

# Создаем экземпляр класса Бот, указываем переменную в качестве аргумента

my_bot = Bot(token)

# Создаем экземпляр класса Диспетчер, указываем объект my_bot в качестве аргумента

dp = Dispatcher(my_bot)

# Добавляем обработчик для команды старт

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Я загадал число от 1 до 3 угадайте')

# Добавляем обработчик для команды старт

@dp.message_handler(text=range(1,4))
async def number_check(message: types.Message):

    # Создаем переменную number со случайным значением из диапазона 1-3

    number = random.randrange(1, 4)

    if int(message.text) == number:
            await message.reply('Правильно, вы отгадали')
    else:
            await message.reply(f'Неправильно, я загадывал число {number}')

executor.start_polling(dp)



