import asyncio
import logging
import os
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
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

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

web_thread = Thread(target=run_web_server, daemon=True)
web_thread.start()

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
    print("Бот и веб-сервер запущены...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
