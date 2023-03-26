from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from menus.models import MultiLangText, FinishFork, MenuItem
from db_sqlite import sqlite_db_edit

payment_fork = FinishFork(
    title=MultiLangText(
        eng="Payment by cash or transfer:",
        ru="Оплата наличными или переводом:",
        kz="Қолма-қол ақшамен немесе аударыммен төлеу:"
    ),
    forks=[
        MenuItem(
            name=MultiLangText(
                eng="Kaspi transfer",
                ru="Kaspi перевод",
                kz="Kaspi аудармасы"
            ),
            price=0,
            item_id="kaspi"
        ),
        MenuItem(
            name=MultiLangText(
                eng="cash",
                ru="наличные",
                kz="қолма-қол ақша"
            ),
            price=0,
            item_id="cash"
        ),
    ]
)

