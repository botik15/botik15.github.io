import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
    
# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.answer("Test 1")

# Хэндлер на команду /test2 
@dp.message(Command("test2"))
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")













dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")


@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot,mylist=[1, 2, 3])

if __name__ == "__main__":
    asyncio.run(main())
