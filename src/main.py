from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

TOKEN = "6504076274:AAFu78aVLjPnHihZxmH4aAQbXYU4T5iYYjw"

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(text='Привет') # Декоратор
async def hello_func(message: Message):
    print(message)
    await message.answer(text=f'Добрый день, {message.from_user.first_name}')

@dp.message_handler(text='Пока') # Декоратор
async def goodbye_func(message: Message):
    print(message)
    await message.answer(text='Удачи тебе!')


executor.start_polling(dispatcher=dp)

