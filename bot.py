import asyncio
import logging
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from aiogram import Bot, Dispatcher, F, types

TOKEN = os.getenv("TOKEN")

BANNED_WORDS = {
    "холодн",
    "думайт",
    "размышляйт",
    "думойт",
    "халадн",
    "xd",
    "хд",
    "эксди",
    "думай",
    "doomай",
    "коч",
    "на подумайть",
    "наподумать",
    "засчитан",
    "зосчитан"
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
    
    if any(word in text_lower for word in BANNED_WORDS):
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
