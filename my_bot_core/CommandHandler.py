from telegram import Update
from telegram.ext import ContextTypes
from my_bot_core.openrouter_client import ask_llm

BAD_WORDS = ["хуй", "пизд", "еба", "сука", "бляд"]


def contains_bad_words(text: str) -> bool:
    lowered = (text or "").lower()
    return any(w in lowered for w in BAD_WORDS)


class BotLogicHandler:
    def __init__(self):
        self.reply_kd = {}

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Привет! Я бот техподдержки. Напиши, какая у тебя проблема."
        )

    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_text = update.message.text or ""

        if "оператор" in user_text.lower() or "живой человек" in user_text.lower():
            await update.message.reply_text(
                "Сейчас я могу только ответить сам. "
                "Если вопрос сложный — опиши его подробнее, я постараюсь помочь."
            )
            return

        if contains_bad_words(user_text):
            await update.message.reply_text(
                "Давай без мата, пожалуйста. Опишите проблему спокойнее"
            )
            return

        answer = await ask_llm(user_text)

        if contains_bad_words(answer):
            answer = "Мне не удалось корректно сформулировать ответ. Попробуй переформулировать вопрос."

        await update.message.reply_text(answer)
