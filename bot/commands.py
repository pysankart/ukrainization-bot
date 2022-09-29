from telegram import Update
from telegram.ext import CallbackContext


def start_command(update: Update, context: CallbackContext) -> None:
    """Start command. Type /start to start bot."""
    update.message.reply_text(
        "Привіт! Я тут щоб перекладати повідомлення російською на українську мову. Для коректної роботи "
        "мені потрібно надати права адміна!"
    ) 


def help_command(update: Update, context: CallbackContext) -> None:
    """Help command. Type /help to ask for help."""
    update.message.reply_text(
        "Я буду перекладати повідомлення російською на українську мову. Для коректної роботи "
        "мені потрібно надати права адміна! Я проацюю на Google Translate API."
    ) 


def news_command(update: Update, context: CallbackContext) -> None:
    """News command. Type /news to see bot latest updates."""
    new = """Що нового?
- це перша версія бота.
- бот перекладає російські повідомлення на українську мову.
останнє оновлення: 30.09.2022
    """
    update.message.reply_text(new)
