import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types

# Токен вашего бота, полученный от @BotFather
TOKEN = "ТОКЕН_ВАШЕГО_БОТА"

# Пачка запрещенных слов (всегда пишите их в нижнем регистре)
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
    "xd"
}

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def filter_messages(message: types.Message):
    text_lower = message.text.lower()
    
    # Проверяем, есть ли хоть одно слово из списка в тексте сообщения
    if any(word in text_lower for word in BANNED_WORDS):
        try:
            # Удаляем сообщение нарушителя
            await message.delete()
        except Exception as e:
            logging.error(f"Не удалось удалить сообщение: {e}")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен и фильтрует пачку слов...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
