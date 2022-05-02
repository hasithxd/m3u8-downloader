# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    await update.reply_chat_action(enums.ChatAction.TYPING)
    await update.reply_text(
        text=f"Welcome {update.from_user.mention}", quote=True
    )

