import logging

import asyncio
from telegram import Update

from my_bot_core.bot import app_telegram


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)



def main() -> None:
    app_telegram.initialize()
    app_telegram.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
