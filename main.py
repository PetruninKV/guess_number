import random
import os
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
import messages_text
import config

load_dotenv()

TOKEN: str = os.getenv("TOKEN")

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()



@dp.message(Command(commands=['start']))
async def start_comand(message: Message):
    await message.answer(messages_text.COMAND_START)


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(messages_text.COMMAND_HELP)


@dp.message(Command(commands=['stat']))
async def stat_comand(message: Message):
    await message.answer(messages_text.COMMAND_STAT)


@dp.message(Command(commands=['cancel']))
async def cancle_comand(message: Message):
    pass


@dp.message(Text(text=messages_text.POSITIVE_RESPONSES, ignore_case=True))
async def positive_answer(message: Message):
    pass



@dp.message(Text(text=messages_text.NEGATIVE_RESPONSES, ignore_case=True))
async def negative_answer(message: Message):
    await message.answer('отрицательный ответ')






if __name__ == "__main__":
    dp.run_polling(bot)

