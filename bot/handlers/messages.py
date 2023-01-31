from aiogram import types

from .. import utils
from ..languages.provider import LanguageProvider
from ..languages.core import UkrainianLanguage, RussianLanguage

forbidden_languages = [RussianLanguage()]
destination = UkrainianLanguage()
language_provider = LanguageProvider(forbidden_languages, destination)


async def message_handler(message: types.Message):
    """
    Telegram bot message handler.
    """
    text = str(message.text)
    translated_text = await language_provider.traslate(text)

    if text != translated_text:
        from_user = message.forward_from or message.from_user
        author = f"@{from_user.username}" if from_user.username else str(from_user.first_name)

        chat_id = message.chat.id
        message_id = message.message_id
        bot = message.bot

        await utils.delete_message(bot, chat_id, message_id)
        await utils.send_message(bot, chat_id, author, translated_text)
