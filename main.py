from aiogram import executor
from create_bot import dispatcher
from handlers import client
from db_sqlite import create_db

async def on_startup(_):

    print("Bot stated!")
    await client.set_default_commands(dispatcher)


client.register_handlers_client(dispatcher)


if __name__ == "__main__":
    create_db.create_db_if_not_exists()
    executor.start_polling(dispatcher, on_startup=on_startup, reset_webhook=True)
