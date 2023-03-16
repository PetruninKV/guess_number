import config

COMAND_START = """Привет!
Давай сыграем в игру "Угадай число"?
Чтобы получить правила игры и список доступных команд - отправьте команду /help"""

COMMAND_HELP = f"""\
Правила игры: Я загадываю число от 1 до 100, а вам нужно его угадать. У вас есть {config.ATTEMPTS} \
попыток.
Доступные команды:
    /help - правила игры и список команд
    /cancel - выйти из игры
    /stat - посмотреть статистику

Давай сыграем?
Отправь положительный ответ обратным сообщением\
"""

COMMAND_STAT = f"""\
Всего игр сыграно: {config.USER['total_games']}
Игр выиграно: {config.USER['wins']}\
"""


POSITIVE_RESPONSES = [
    'Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть',
    'Да, с удовольствием!', 'Конечно!', 'Безусловно!', 'Нет проблем!', 'Я согласен!',
    'Давайте делать это!', 'Я не вижу причин, почему нет!', 'Как только можно начинать?', 
    'Я готов!', 'Почему бы и нет!', 'Да!', 'Окей!', 'Конечно!', 'Идем!', 'Го!', 'Согласен!', 
    'Поехали!', 'Ладно!', 'Давай!', 'ок', '+', 'yes', 'let`s go', 'ok', 'okey'
    ]

NEGATIVE_RESPONSES = [
    'Нет, спасибо', 'Извините, но нет', 'Не могу сейчас', 'Сожалею, но нет', 
    'Не думаю, что это возможно', 'Я бы лучше отказался', 'Не сейчас', 'Мне не хочется этого делать', 
    'Нет, я не согласен', 'Извините, но я уже занят', 'Нет', 'Неа', 'Никак', 'Не хочу', 'Не буду' 'Не смогу', 
    'Не получится', 'Отстань', 'Не', 'Ни за что', 'Никогда', '-', 'no'
    ]


GREETING_IN_GAME = """\
Ура!    
Я загадал число от 1 до 100, попробуй угадать!\
"""

ERROR_MES_IN_GAME1 = """\
Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды /cancel и /stat\
"""

UPSET = """\
Жаль :(
Если захотите поиграть - просто напишите об этом.\
"""
ERROR_MES_IN_GAME2 = """\
Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100\
"""