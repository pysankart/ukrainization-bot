from aiogram import Bot


async def delete_message(bot: Bot, chat_id: int, message_id: int):
    """
    Delete message from chat.
    """
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )


async def send_message(bot: Bot, chat_id: int, author: str, text: str):
    """
    Send message to chat.
    """
    message = f"{author} сказав(ла): {text}"
    await bot.send_message(
        chat_id=chat_id,
        text=message
    )
