from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang_list = ["Kz", "Ru", "Eng"]
buttons = [InlineKeyboardButton(text=lang, callback_data=lang.lower()) for lang in lang_list]
keyboard_start = InlineKeyboardMarkup().add(*buttons)
