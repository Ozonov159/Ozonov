print("BOT IS STARTING...")

import asyncio

async def main():
    try:
        print("RUNNING POLLING...")
        await dp.start_polling(bot)
    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    asyncio.run(main())
