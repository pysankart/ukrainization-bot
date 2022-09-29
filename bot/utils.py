from telegram.ext import CallbackContext


def delete_message(context: CallbackContext, chat_id: int, message_id: int) -> None:
    """Delete message from chat."""
    context.bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )


def send_message(context: CallbackContext, chat_id: int, author: str, text: str) -> None:
    """Send message to chat."""
    msg = f"{author} сказав(ла): {text}"
    context.bot.send_message(
        chat_id=chat_id,
        text=msg
    )

