import logging
import os
from my_settings_env import BOT_TOKEN

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from my_bot_core.CommandHandler import BotLogicHandler

logging.basicConfig(level=logging.INFO)
logic = BotLogicHandler()
app_telegram = Application.builder().token(BOT_TOKEN).build()
app_telegram.add_handler(CommandHandler('start', logic.start))
app_telegram.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, logic.handle_text)
)