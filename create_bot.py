from aiogram import Bot, Dispatcher
from token import TOKEN
from os import environ

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

# # ____________________________________________________________________
# import asyncio
# import aiogram
# from aiogram import Bot, types, Dispatcher
#
# # create bot object
# TOKEN = "5848810697:AAEQxWHOPWS0PICaQZj6j8foysi5MC9yuEU"
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
# # create event handler for the message sent by the bot
# @dp.message_handler(commands=['last_message'])
# async def delete_last_message(message: types.Message):
#     # get the chat ID of the message
#     chat_id = message.chat.id
#
#     # get the last message sent by the bot in the chat
#     last_message = await bot.send_message(chat_id, "This message will be deleted soon.")
#
#     # delete the last message sent by the bot
#     await bot.delete_message(chat_id, last_message.message_id)
#
#
# # start the bot
# if __name__ == '__main__':
#     aiogram.executor.start_polling(dp, skip_updates=True)