import random
import os
from dotenv import load_dotenv
from importlib import reload

import messages_text
from config import ATTEMPTS, USER

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command


load_dotenv()

TOKEN: str = os.getenv("TOKEN")

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()


def create_random_number() -> int:
    return random.randint(1, 100)


@dp.message(Command(commands=['start']))
async def start_comand(message: Message):
    await message.answer(messages_text.COMAND_START)


@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(messages_text.COMMAND_HELP)


@dp.message(Command(commands=['stat']))
async def stat_comand(message: Message):
    reload(messages_text)
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


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def numbers_answer(message: Message):
    if USER['in_game']:
        number = int(message.text)
        if number == USER['secret_number']:
            await message.answer('Поздравляю! Вы угадали! Может еще разок?')
            USER["in_game"] = False
            USER['wins'] += 1
            USER['total_games'] += 1
        elif number < USER['secret_number']:
            await message.answer('Загаданное число больше')
            USER['attempts'] -= 1
        elif number > USER['secret_number']:
            await message.answer('Загаданное число меньше')
            USER['attempts'] -= 1

        if USER['attempts'] == 0:
            reload(messages_text)
            await message.answer(messages_text.GAME_OVER)
            USER['in_game'] = False
            USER['total_games'] += 1

    else:
        await message.answer('Мы еще не играем. Хотите сыграть? Отправьте положительный ответ')


@dp.message()
async def other_anser(message: Message):
    if USER['in_game']:
        await message.answer('Мы же сейчас играем! Присылайте выши числа.')
    else:
        await message.answer('Давайте лучше сыграем в игру!')


if __name__ == "__main__":
    dp.run_polling(bot)