import asyncio
from aiogram import Bot, Dispatcher

TOKEN = "твой_токен"

bot = Bot(token=TOKEN)
dp = Dispatcher()

print("BOT IS STARTING...")

async def main():
    try:
        print("RUNNING POLLING...")
        await dp.start_polling(bot)
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    asyncio.run(main())
