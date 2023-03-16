import random
import os
from dotenv import load_dotenv
from importlib import reload

import messages_text
from config import ATTEMPTS, USERS, CREATE_NEW_USER

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
    if message.from_user.id not in USERS:
        USERS[message.from_user.id] = CREATE_NEW_USER



@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(messages_text.COMMAND_HELP)


@dp.message(Command(commands=['stat']))
async def stat_comand(message: Message):
    await message.answer(f"Всего игр сыграно: {USERS[message.from_user.id]['total_games']}.\n"
                         f"Игр выиграно: {USERS[message.from_user.id]['wins']}")


@dp.message(Command(commands=['cancel']))
async def cancle_comand(message: Message):
    if USERS[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Захотите сыграть снова - напишите!')
        USERS[message.from_user.id]['in_game'] = False
    else:
        await message.answer('Мы с вами итак не играли. Может, сыграем раунд?')


@dp.message(Text(text=messages_text.POSITIVE_RESPONSES, ignore_case=True))
async def positive_answer(message: Message):
    if not USERS[message.from_user.id]['in_game']:
        await message.answer(messages_text.GREETING_IN_GAME)
        USERS[message.from_user.id]["in_game"] = True
        USERS[message.from_user.id]['attempts'] = ATTEMPTS
        USERS[message.from_user.id]['secret_number'] = create_random_number()
    else:
        await message.answer(messages_text.ERROR_MES_IN_GAME1)


@dp.message(Text(text=messages_text.NEGATIVE_RESPONSES, ignore_case=True))
async def negative_answer(message: Message):
    if not USERS[message.from_user.id]['in_game']:
        await message.answer(messages_text.UPSET)
    else:
        await message.answer(messages_text.ERROR_MES_IN_GAME2)


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def numbers_answer(message: Message):
    if USERS[message.from_user.id]['in_game']:
        number = int(message.text)
        if number == USERS[message.from_user.id]['secret_number']:
            await message.answer('Поздравляю! Вы угадали! Может еще разок?')
            USERS[message.from_user.id]["in_game"] = False
            USERS[message.from_user.id]['wins'] += 1
            USERS[message.from_user.id]['total_games'] += 1
        elif number < USERS[message.from_user.id]['secret_number']:
            await message.answer('Загаданное число больше')
            USERS[message.from_user.id]['attempts'] -= 1
        elif number > USERS[message.from_user.id]['secret_number']:
            await message.answer('Загаданное число меньше')
            USERS[message.from_user.id]['attempts'] -= 1

        if USERS[message.from_user.id]['attempts'] == 0:
            answer = f"{messages_text.GAME_OVER} {USERS[message.from_user.id]['secret_number']} \nДавайте сыграем еще?"
            await message.answer(answer)
            USERS[message.from_user.id]['in_game'] = False
            USERS[message.from_user.id]['total_games'] += 1

    else:
        await message.answer('Мы еще не играем. Хотите сыграть? Отправьте положительный ответ')


@dp.message()
async def other_anser(message: Message):
    if message.from_user.id not in USERS:
        USERS[message.from_user.id] = CREATE_NEW_USER   
        if USERS[message.from_user.id]['in_game']:
            await message.answer('Мы же сейчас играем! Присылайте выши числа.')
        else:
            await message.answer('Давайте лучше сыграем в игру!')


if __name__ == "__main__":
    dp.run_polling(bot)