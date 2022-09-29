import os
from bot import create_bot

token = os.environ.get("BOT_TOKEN")
bot = create_bot(token)

if __name__ == "__main__":
    bot.start_polling(1.0)
    bot.idle()
    