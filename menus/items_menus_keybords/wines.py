from menus.models import MenuItem, MultiLangText

all_wines = [
    MenuItem(
        name=MultiLangText(
            eng='Red_semi-sweet 🍷 1500₸',
            ru='Красное полусладкое 🍷 1500₸',
            kz='Қызыл жартылай тәтті 🍷 1500₸'
        ),
        price=1500,
        item_id='red_semi'
    ),
    MenuItem(
        name=MultiLangText(
            eng='White dry 🥂 1500₸',
            ru='Белое сухое 🥂 1500₸',
            kz='Құрғақ ақ 🥂 1500₸'
        ),
        price=1500,
        item_id='white_dry'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Pink 💗 1500₸',
            ru='Розовое 💗 1500₸',
            kz='Қызғылт 💗 1500₸',
        ),
        price=1500,
        item_id='pink'
    ),
]
