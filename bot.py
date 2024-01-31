import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
from config_reader import config
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()
 

# Если не указать фильтр F.text, 
# то хэндлер сработает даже на картинку с подписью /test
@dp.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Hello, <b>world</b>!", 
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "Hello, *world*\!", 
        parse_mode=ParseMode.MARKDOWN_V2
    )
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot,mylist=[1, 2, 3])

if __name__ == "__main__":
    asyncio.run(main())
