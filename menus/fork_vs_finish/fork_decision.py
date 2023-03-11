from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from menus.models import MultiLangText, FinishFork, MenuItem
from db_sqlite import sqlite_db_edit

fork_finish = FinishFork(
    title=MultiLangText(
        eng="Choose action:",
        ru="Выберите действие:",
        kz="Әрекетті таңдаңыз"
    ),
    forks=[
        MenuItem(
            name=MultiLangText(
                eng="Back to main Menu",
                ru="Вернуться в главное меню",
                kz="Негізгі мәзірге оралу"
            ),
            price=0,
            item_id="ru"
        ),
        MenuItem(
            name=MultiLangText(
                eng="Сomplete the order",
                ru="Завершить",
                kz="тапсырысты аяқтаңыз"
            ),
            price=0,
            item_id="end"
        ),
        MenuItem(

            name=MultiLangText(
                eng="Basket:",
                ru="Корзина",
                kz="Себет"
            ),
            price=0,
            item_id="basket"
        ),
        MenuItem(

            name=MultiLangText(
                eng="Reset basket",
                ru="Очистить корзину",
                kz="Бос себет"
            ),
            price=0,
            item_id="clear"
        )

        # MenuItem(
        #
        #     name=MultiLangText(
        #         eng="🗣️👅💬",
        #         ru="🗣️👅💬",
        #         kz="🗣️👅💬"
        #     ),
        #     price=0,
        #     item_id="again"
        # )
    ]
)

