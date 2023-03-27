from aiogram import types, Dispatcher
import datetime
from db_sqlite.sqlite_worker import SQLWorker
from menus.keybord_start_lang import keyboard_start
from menus.items_menus_keybords.all_items_id import all_dict_id_price, all_list_id, all_dict_id_name
from common import get_category_items_markup, get_categories_markup, get_title_of_main_menu, \
    get_title_of_category, get_fork_decision_markup, get_title_fork
from menus.fork_vs_finish.fork_decision import fork_finish
from menus.fork_vs_finish.new_order import new_order
from menus.fork_vs_finish.cash_or_transfer import payment_fork
from menus.items_menus_keybords.juices import all_juice_fork
from google_sheets import add_data_to_sheet

instance_sqlite = SQLWorker()

async def set_default_commands(db: Dispatcher):
    await db.bot.set_my_commands(
        [
            types.BotCommand('start', 'Выбрать язык заново'),
        ]
    )


async def welcome_and_choose_language(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    formatted_date = datetime.datetime.now().strftime('%H:%M:%S')
    SQLWorker.add_new_bot_client(instance_sqlite, formatted_date, user_id, username)
    # print("client +")
    greeting = await message.reply("Hello Almaty! This is Stәnd By Club \
                        \n🗣️👅💬", reply_markup=keyboard_start)


async def pass_category_by_language(call: types.CallbackQuery):
    if call.data == "lang":
        current_lang = SQLWorker.get_user_lang(instance_sqlite, call.from_user.id)
    else:
        current_lang = call.data
    SQLWorker.update_lang(instance_sqlite, call.from_user.id, current_lang)
    await call.message.answer(
        text=get_title_of_main_menu(current_lang),  # "Выберите категорию:",
        reply_markup=get_categories_markup(lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


async def pass_items_by_category(call: types.CallbackQuery):
    # print(call.from_user.id)
    current_lang = str(SQLWorker.get_user_lang(instance_sqlite, call.from_user.id))
    await call.message.answer(
        text=get_title_of_category(call, current_lang),
        reply_markup=get_category_items_markup(category=call.data, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


async def pass_juices(call: types.CallbackQuery):
    print(call.from_user.id)
    current_lang = str(SQLWorker.get_user_lang(instance_sqlite, call.from_user.id))
    await call.message.answer(
        text=get_title_fork(fork=all_juice_fork, lang=current_lang),
        reply_markup=get_fork_decision_markup(fork=all_juice_fork, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


async def pass_items_to_show_basket(call: types.CallbackQuery):
    orders, cost = SQLWorker.get_order_and_total_cost(instance_sqlite, call.from_user.id)
    current_lang = str(SQLWorker.get_user_lang(instance_sqlite, call.from_user.id))
    await call.message.answer(
        text=f"{orders} \ntotal: {cost}₸",
        reply_markup=get_fork_decision_markup(fork=fork_finish, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id

    )


async def clear_and_go_to_main_menu(call: types.CallbackQuery):
    SQLWorker.clear_by_id(instance_sqlite, call.from_user.id)
    current_lang = str(SQLWorker.get_user_lang(instance_sqlite, call.from_user.id))
    await call.message.answer(
        text=f"all clear :)\n" + get_title_fork(new_order, current_lang),
        reply_markup=get_fork_decision_markup(fork=new_order, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )



async def pass_fork_decision(call: types.CallbackQuery):
    current_lang = SQLWorker.get_user_lang(instance_sqlite, call.from_user.id)
    # print("call command", call.data)
    # print("call id", call.id)
    # print("user id", call.from_user.id)

    SQLWorker.update_order_and_payment(instance_sqlite, call.from_user.id, all_dict_id_name[call.data], all_dict_id_price[call.data])
    await call.message.answer(
        text=get_title_fork(fork_finish, current_lang),
        reply_markup=get_fork_decision_markup(fork=fork_finish, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


async def send_row_to_google_sheets(call: types.CallbackQuery):
    # print(SQLWorker.get_one_raw(instance_sqlite, call.from_user.id))
    current_lang = str(SQLWorker.get_user_lang(instance_sqlite, call.from_user.id))
    SQLWorker.update_time(instance_sqlite, call.from_user.id, datetime.datetime.now().strftime('%-H:%-M:%-S'))
    # SQLWorker.update_table(call.from_user.id, )
    await call.message.answer(
        text=get_title_fork(payment_fork, current_lang),
        reply_markup=get_fork_decision_markup(fork=payment_fork, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )



async def get_payment(call: types.CallbackQuery):
    instance_sqlite.current_orger += 1
    SQLWorker.update_payment_type_and_num_order(instance_sqlite, datetime.datetime.now().strftime('%-H:%-M:%-S'),
                                                call.from_user.id, call.data, instance_sqlite.current_orger)
    add_data_to_sheet.add_users_string(SQLWorker.get_one_raw(instance_sqlite, call.from_user.id))
    orders, cost = SQLWorker.get_order_and_total_cost(instance_sqlite, call.from_user.id)
    if call.data == "cash":
        await call.message.answer(
            text=f"Order:{orders}\ntotal: {cost}₸"
        )
        await call.message.answer(
            text=f"Подойдите к бару и скажите номер заказа: {instance_sqlite.current_orger}\n\
                   __Рахмет__"
        )
    elif call.data == "kaspi":
        await call.message.answer(
            text=f"Order:{orders}\ntotal: {cost}₸"
        )
        await call.message.answer(
            text="Перевод на kaspi по номеру:"
        )
        await call.message.answer(
            text="+77476187893"
        )
        await call.message.answer(
            text=f"АЛЕКСАНДР Н.\n\
            после подойдите к бару,\n\
            скажите номер заказа: {instance_sqlite.current_orger} \n\
                 и покажите чек :)\n\
                 __Рахмет__"
        )
    current_lang = str(SQLWorker.get_user_lang(instance_sqlite, call.from_user.id))
    await call.message.answer(
        text=get_title_fork(new_order, current_lang),
        reply_markup=get_fork_decision_markup(fork=new_order, lang=current_lang)
    )
    await call.bot.delete_message(
        chat_id=call.message.chat.id, message_id=call.message.message_id
    )


def register_handlers_client(_dispatcher: Dispatcher):
    _dispatcher.register_message_handler(welcome_and_choose_language, commands=['start', 'help', 'again'])
    _dispatcher.register_callback_query_handler(pass_category_by_language, text=['kz', 'ru', 'eng', 'lang'])
    _dispatcher.register_callback_query_handler(pass_items_by_category,
                                                text=['cocktails', 'tinctures', 'beer_cider', 'tea',
                                                      'snacks', 'wine', 'other_drinks', 'lemonades'])
    _dispatcher.register_callback_query_handler(pass_juices,
                                                text=['juice'])
    _dispatcher.register_callback_query_handler(pass_fork_decision, text=all_list_id)
    _dispatcher.register_callback_query_handler(pass_items_to_show_basket, text=["basket"])
    _dispatcher.register_callback_query_handler(clear_and_go_to_main_menu, text=["clear"])
    _dispatcher.register_callback_query_handler(send_row_to_google_sheets, text=["end"])
    _dispatcher.register_callback_query_handler(get_payment, text=["cash", "kaspi"])
