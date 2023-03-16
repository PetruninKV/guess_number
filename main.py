import random
import os
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
import messages_text

load_dotenv()

TOKEN: str = os.getenv("TOKEN")

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPTS: int = 5
USER: dict = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
            }











@dp.message(Command(commands=['start']))
async def start_comand(message: Message):
    await message.answer(messages_text.COMAND_START)


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(messages_text.COMMAND_HELP)




if __name__ == "__main__":
    dp.run_polling(bot)

