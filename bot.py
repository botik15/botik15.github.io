import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime
from config_reader import config
from aiogram import F, html
from aiogram.types import Message  


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер
dp = Dispatcher()



# @dp.message(F.text.lower() == "с пюрешкой")
# async def with_puree(message: types.Message):
#     await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())

# @dp.message(F.text.lower() == "без пюрешки")
# async def without_puree(message: types.Message):
#     await message.reply("Так невкусно!", reply_markup=types.ReplyKeyboardRemove())


# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton(text="С пюрешкой"),
#             types.KeyboardButton(text="Без пюрешки")
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите способ подачи"
#     )
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)




# # новый импорт!
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

# @dp.message(Command("reply_builder"))
# async def reply_builder(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     for i in range(1, 17):
#         builder.add(types.KeyboardButton(text=str(i)))
#     builder.adjust(4)
#     await message.answer(
#         "Выберите число:",
#         reply_markup=builder.as_markup(resize_keyboard=True),
#     )




# # новый импорт!
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

# @dp.message(Command("special_buttons"))
# async def cmd_special_buttons(message: types.Message):
#     builder = ReplyKeyboardBuilder()
#     # метод row позволяет явным образом сформировать ряд
#     # из одной или нескольких кнопок. Например, первый ряд
#     # будет состоять из двух кнопок...
#     builder.row(
#         types.KeyboardButton(text="Запросить геолокацию", request_location=True),
#         types.KeyboardButton(text="Запросить контакт", request_contact=True)
#     )
#     # ... второй из одной ...
#     builder.row(types.KeyboardButton(
#         text="Создать викторину",
#         request_poll=types.KeyboardButtonPollType(type="quiz"))
#     )
#     # ... а третий снова из двух
#     builder.row(
#         types.KeyboardButton(
#             text="Выбрать премиум пользователя",
#             request_user=types.KeyboardButtonRequestUser(
#                 request_id=1,
#                 user_is_premium=True
#             )
#         ),
#         types.KeyboardButton(
#             text="Выбрать супергруппу с форумами",
#             request_chat=types.KeyboardButtonRequestChat(
#                 request_id=2,
#                 chat_is_channel=False,
#                 chat_is_forum=True
#             )
#         )
#     )
#     # WebApp-ов пока нет, сорри :(

#     await message.answer(
#         "Выберите действие:",
#         reply_markup=builder.as_markup(resize_keyboard=True),
#     )








# новый импорт!
from aiogram.utils.keyboard import InlineKeyboardBuilder

@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )
    # или просто await callback.answer()



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot,mylist=[1, 2, 3])

if __name__ == "__main__":
    asyncio.run(main())
