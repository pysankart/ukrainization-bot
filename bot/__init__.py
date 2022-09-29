from telegram.ext import CommandHandler, Filters, MessageHandler, Updater


def create_bot(token: str) -> Updater:
    """Create bot factory function."""
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher
    from .commands import start_command, help_command, news_command
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("news", news_command))

    from .message import message_handler
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    return updater 
