import random
import os
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
import messages_text
from config import ATTEMPTS, USER

load_dotenv()

TOKEN: str = os.getenv("TOKEN")

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()


def create_random_number():
    


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
    if not USER['in_game']:
        await message.answer(messages_text.GREETING_IN_GAME)
        USER["in_game"] = True
        USER['attempts'] = ATTEMPTS
        USER['secret_number'] = create_random_number()
    else:
        await message.answer(messages_text.ERROR_MES_IN_GAME1)


@dp.message(Text(text=messages_text.NEGATIVE_RESPONSES, ignore_case=True))
async def negative_answer(message: Message):
    if not USER['in_game']:
        await message.answer(messages_text.UPSET)
    else:
        await message.answer(messages_text.ERROR_MES_IN_GAME2)






if __name__ == "__main__":
    dp.run_polling(bot)

