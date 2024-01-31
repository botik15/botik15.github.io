import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5985975773:AAEoB0jrr9Z0Jmt7vnELZvfAa9Bx4r_fiNI")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    
# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")
    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
