from aiogram import types, Dispatcher
import datetime
from menus.keybord_start_lang import keyboard_start
from menus.items_menus_keybords.all_items_id import all_dict_id_price, all_list_id, all_dict_id_name
from common import get_category_items_markup, get_categories_markup, get_title_of_main_menu, \
    get_title_of_category, get_fork_decision_markup, get_title_fork
from menus.fork_vs_finish.fork_decision import fork_finish
from menus.items_menus_keybords.juices import all_juice_fork
from db_sqlite import sqlite_db_edit


async def set_default_commands(db : Dispatcher):
    await db.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),
        ]
    )


async def welcome_and_choose_language(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    formatted_date = datetime.date.today().strftime("%d/%m/%Y")
    sqlite_db_edit.add_new_bot_client(formatted_date, user_id, username)
    print("client +")
    greeting = await message.reply("Hello Almaty! This is Stәnd By Club \
                        \n🗣️👅💬", reply_markup=keyboard_start)


async def pass_category_by_language(call: types.CallbackQuery):
    current_lang = call.data
    sqlite_db_edit.update_lang(call.from_user.id, current_lang)
    await call.message.answer(
        text=get_title_of_main_menu(current_lang),  # "Выберите категорию:",
        reply_markup=get_categories_markup(lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


async def pass_items_by_category(call: types.CallbackQuery):
    print(call.from_user.id)
    current_lang = str(sqlite_db_edit.get_user_lang(call.from_user.id))
    await call.message.answer(
        text=get_title_of_category(call, current_lang),
        reply_markup=get_category_items_markup(category=call.data, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


async def pass_juices(call: types.CallbackQuery):
    print(call.from_user.id)
    current_lang = str(sqlite_db_edit.get_user_lang(call.from_user.id))
    await call.message.answer(
        text=get_title_fork(fork=all_juice_fork, lang=current_lang),
        reply_markup=get_fork_decision_markup(fork=all_juice_fork, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


async def pass_items_to_show_basket(call: types.CallbackQuery):
    orders, cost = sqlite_db_edit.get_order_and_total_cost(call.from_user.id)
    await call.message.answer(
        text=f"{orders} \n {cost}",
    )


async def clear_and_go_to_main_menu(call: types.CallbackQuery):
    sqlite_db_edit.clear_by_id(call.from_user.id, datetime.date.today().strftime("%d/%m/%Y"))
    new_call = types.CallbackQuery()
    await call.message.answer(
        text=f"all clear :)",
    )


async def pass_fork_decision(call: types.CallbackQuery):
    current_lang = sqlite_db_edit.get_user_lang(call.from_user.id)
    print("call command", call.data)
    print("call id", call.id)
    print("user id", call.from_user.id)
    sqlite_db_edit.update_order_and_payment(call.from_user.id, all_dict_id_name[call.data], all_dict_id_price[call.data])
    await call.message.answer(
        text=get_title_fork(fork_finish, current_lang),
        reply_markup=get_fork_decision_markup(fork=fork_finish, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


def register_handlers_client(_dispatcher: Dispatcher):
    _dispatcher.register_message_handler(welcome_and_choose_language, commands=['start', 'help', 'again'])
    _dispatcher.register_callback_query_handler(pass_category_by_language, text=['kz', 'ru', 'eng'])
    _dispatcher.register_callback_query_handler(pass_items_by_category,
                                                text=['cocktails', 'tinctures', 'beer', 'cider', 'snacks', 'wine',
                                                      'non_alcoholic'])
    _dispatcher.register_callback_query_handler(pass_juices,
                                                text=['juice'])
    _dispatcher.register_callback_query_handler(pass_fork_decision, text=all_list_id)
    _dispatcher.register_callback_query_handler(pass_items_to_show_basket, text=["basket"])
    _dispatcher.register_callback_query_handler(clear_and_go_to_main_menu, text=["clear"])
