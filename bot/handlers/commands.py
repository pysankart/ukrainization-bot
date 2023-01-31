from aiogram import types

from .. import answers


async def start(message: types.Message):
    """
    Start command. Type /start to start bot.
    """
    await message.answer(answers.START_MESSAGE)


async def help(message: types.Message):
    """
    Help command. Type /help to ask for help.
    """
    await message.answer(answers.HELP_MESSAGE)


async def news(message: types.Message):
    """
    News command. Type /news to see bot latest updates.
    """
    await message.answer(answers.NEWS_MESSAGE)
