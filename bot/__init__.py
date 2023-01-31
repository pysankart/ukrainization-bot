from aiogram import Bot, Dispatcher, executor

from .config import config
from .handlers import commands, messages


def create_dispatcher() -> Dispatcher:
    """
    Aiogram dispatcher factory.
    """
    bot = Bot(token=config.API_TOKEN)
    dp = Dispatcher(bot)

    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.help, commands=['help'])
    dp.register_message_handler(commands.news, commands=['news'])

    dp.register_message_handler(messages.message_handler)

    return dp


def run_bot(dp: Dispatcher):
    """
    Start bot in long-polling mode.
    """
    executor.start_polling(dp, skip_updates=True)
