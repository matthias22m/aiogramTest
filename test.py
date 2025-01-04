from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

from ex.db_helper import Db_interaction

db = Db_interaction()

# db.insert_user(User(12,'girma bekele','girma@gmail.com'))

users = db.get_users()
# print(users[0].name)

TOKEN = "6778524790:AAFpJS51I0RO-zCi5pGvQiLheCfpBtJ0o30"

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Handler for the /start command
@dp.message(Command("start"))
async def send_welcome(message: Message):
    for user in users:
        await message.answer(user.email)
        await bot.delete_message(message.chat.id, 155881)

@dp.message(Command("get_message"))
async def get_specific_message(message: Message):
    try:
        message_id = int(message.text.split()[1])  # Extract message_id from user input
        chat_id = message.chat.id

        # Fetch the specific message using bot.get_message
        retrieved_message = await bot.forward_message(
            chat_id=chat_id, 
            from_chat_id=chat_id, 
            message_id=message_id
        )
        
        await message.answer(f"Message retrieved: {retrieved_message.text}")

    except IndexError:
        await message.answer("Please provide a message ID after the /get_message command.")
    except Exception as e:
        await message.answer(f"Failed to retrieve message: {str(e)}")

# Handler for any text message
@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    # Start polling updates
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
