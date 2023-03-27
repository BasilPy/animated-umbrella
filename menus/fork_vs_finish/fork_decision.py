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
                eng='<-Main menu',
                ru='<-Главное меню',
                kz='<-Басты мәзір',
            ),
            price=0,
            item_id="lang"
        ),
        MenuItem(
            name=MultiLangText(
                eng="Сomplete the order",
                ru="Завершить заказ",
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
    ]
)

