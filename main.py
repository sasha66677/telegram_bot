import os
from os.path import join, dirname
from dotenv import load_dotenv

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


bot = Bot(token=os.environ.get("TG_API_TOKEN"))
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("Test 1"))
async def cmd_test1(message: types.Message):
    await message.answer("Test 1")


@dp.message(Command("test2"))
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")




async def main():
    #dp.message.register(cmd_test2, Command("test2"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())