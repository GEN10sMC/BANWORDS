import asyncio
import logging
import os
import re
from aiogram import Bot, Dispatcher, F, types

TOKEN = os.getenv("TOKEN")

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
    "Холодные",
    "Халодные",
    "Халадные",
    "холодные",
    "халодные",
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
            if word in text_lower:
                is_banned = True
                break
        else:
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
