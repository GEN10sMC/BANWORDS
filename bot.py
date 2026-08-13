import asyncio
import logging
import os
import re
from aiogram import Bot, Dispatcher, F, types

# Токен подтягивается из переменных окружения сервера
TOKEN = os.getenv("TOKEN")

# Ваши слова и фразы (все переведены в нижний регистр для точного поиска)
BANNED_WORDS = {
    "холодный",
    "думайте",
    "размышляйте",
    "думойте",
    "халадный",
    "XD",
    "Xd",
    "xD",
    "хд",
    "ХД",
    "Хд",
    "хД",
    "эксди",
    "думай",
    "doomай",
    "коч",
    "на подумайть",
    "наподумать",
    "Засчитано",
    "засчитано",
    "Зосчитано",
    "xd"
}

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def filter_messages(message: types.Message):
    text_lower = message.text.lower()
    
    is_banned = False
    for word in BANNED_WORDS:
        if " " in word:
            # Если это фраза с пробелом (например, "на подумайть"), ищем её целиком в тексте
            if word in text_lower:
                is_banned = True
                break
        else:
            # Если это отдельное слово (например, "xd", "хд", "коч"), 
            # ищем строго по границам слов, чтобы не задевать другие части текста
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, text_lower):
                is_banned = True
                break

    if is_banned:
        try:
            await message.delete()
        except Exception as e:
            logging.error(f"Не удалось удалить сообщение: {e}")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен и фильтрует пачку слов...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
