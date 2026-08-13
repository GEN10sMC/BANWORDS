import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F, types

# Токен подтягивается из переменных окружения сервера
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
    "xd"
}

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def filter_messages(message: types.Message):
    text_lower = message.text.lower()
    if any(word in text_lower for word in BANNED_WORDS):
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
