from telegram import Update
from telegram.ext import CallbackContext

from .languages import LanguageProvider, UkrainianLanguage, RussianLanguage
from .utils import delete_message, send_message

provider = LanguageProvider()
provider.register_languages(
    RussianLanguage
)
provider.register_destination(UkrainianLanguage)


def message_handler(update: Update, context: CallbackContext) -> None:
    """Telegram bot message handler."""
    text = str(update.message.text)
    translated = provider.translate(text)

    if text != translated:
        from_user = update.message.forward_from or update.message.from_user 
        author = f"@{from_user.username}" if from_user.username else str(from_user.first_name)

        chat_id = update.message.chat_id
        message_id = update.message.message_id

        delete_message(context, chat_id, message_id)
        send_message(context, chat_id, author, translated)