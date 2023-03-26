from menus.models import MenuItem, MultiLangText

all_wines = [
    MenuItem(
        name=MultiLangText(
            eng='Red_semi-sweet 🍷 2000₸',
            ru='Красное полусладкое 🍷 2000₸',
            kz='Қызыл жартылай тәтті 🍷 2000₸'
        ),
        price=2000,
        item_id='red_semi'
    ),
    MenuItem(
        name=MultiLangText(
            eng='White dry 🥂 2000₸',
            ru='Белое сухое 🥂 2000₸',
            kz='Құрғақ ақ 🥂 2000₸'
        ),
        price=2000,
        item_id='white_dry'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Pink 💗 2000₸',
            ru='Розовое 💗 2000₸',
            kz='Қызғылт 💗 2000₸',
        ),
        price=2000,
        item_id='pink'
    ),
]
