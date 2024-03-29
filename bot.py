import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
from config_reader import config
from aiogram import F, html
from aiogram.types import Message  
from aiogram.types import InputFile


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер
dp = Dispatcher()

import os

from subprocess import run, STDOUT, PIPE
# указывайте полный путь к запускаемой 
# программе/команде или она не будет работать
 

@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    path = 'git_dowland_py.sh'
    await message.answer_document(InputFile(path))
    

# Запуск процесса поллинга новых апдейтов
async def main():   
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
