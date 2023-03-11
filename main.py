from aiogram import executor
from create_bot import dispatcher
from handlers import client


async def on_startup(_):
    print("Bot stated!")
    # db_lite_clients.sql_start()
    await client.set_default_commands(dispatcher)


client.register_handlers_client(dispatcher)

if __name__ == "__main__":
    executor.start_polling(dispatcher, on_startup=on_startup)
