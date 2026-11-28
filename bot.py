from google import genai
from google.genai import types
import os
import sys
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
load_dotenv()

token = os.getenv("BOT_TOKEN")
if not token:
    print("Такого токена нету")
    sys.exit()

Api = os.getenv("GEMINI_API_KEY")
if not Api:
    print("Апи не найден")
    sys.exit()
SYSTEM_PROMPT =  """Ты наставник по Python для новичка, пиши простыми словами, пиши на русском и коротко, пиши обычным текстом
без Markdown и т.д, на вопросы которые не связаны с программированием вежливо отказывай, так же не спрашивай не каких личных данных, паролей, и подобного"""
client = genai.Client(api_key=Api)
bot = Bot(token=token)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message:Message):
    await message.reply("Привет")

@dp.message(F.text)
async def text_return(message:Message):
    try:
        response = await client.aio.models.generate_content(model= "gemini-3.5-flash", contents= message.text, config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT))
        await message.answer(response.text[:4000])
    except Exception as e:
        print(f"Не удалось вывести: {e}")
        await message.answer("ИИ сейчас занят")

async def main():
    await dp.start_polling(bot)
asyncio.run(main())