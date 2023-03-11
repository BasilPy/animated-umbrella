from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from menus.main_menu import menu
from menus.models import MenuItem, MenuCategory, FinishFork
from menus.fork_vs_finish.fork_decision import fork_finish
from menus.items_menus_keybords.juices import all_juice_fork
# from menus.basket import basket


def _create_button_inline(menu_item: MenuItem, lang) -> InlineKeyboardButton:
    text = menu_item.name.__getattribute__(lang)
    button = InlineKeyboardButton(text=text, callback_data=menu_item.item_id)
    return button



def _create_button_finish(fork_item: MenuItem, lang) -> InlineKeyboardButton:
    text = fork_item.name.__getattribute__(lang)
    button = InlineKeyboardButton(text=text, callback_data=fork_item.id_)
    return button


def get_exact_category(category_name) -> MenuCategory:
    for category in menu.categories:
        if category_name == category.item_id:
            return category


def get_title_of_main_menu(lang):
    return menu.title_categories.get_text_by_language(lang)


def get_title_of_category(call, lang):
    return get_exact_category(category_name=call.data).instruction.get_text_by_language(lang)


def get_category_items_markup(category: MenuCategory, lang: str) -> InlineKeyboardMarkup:
    category_items = get_exact_category(category).category_items
    buttons = [
        _create_button_inline(menu_item=category_item, lang=lang) for category_item in category_items
    ]
    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.add(button)
    return markup


def get_categories_markup(lang: str) -> InlineKeyboardMarkup:
    buttons = [
        _create_button_inline(menu_item=category, lang=lang) for category in menu.categories
    ]
    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.row(button)
    return markup


def get_title_fork(fork, lang: str):
    return fork.title.get_text_by_language(lang)


def get_fork_decision_markup(fork, lang: str) -> InlineKeyboardMarkup:
    buttons = [
        _create_button_inline(menu_item=category, lang=lang) for category in fork.forks
    ]
    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.row(button)
    return markup


