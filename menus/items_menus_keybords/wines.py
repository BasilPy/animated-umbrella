from menus.models import MenuItem, MultiLangText

all_wines = [
    MenuItem(
        name=MultiLangText(
            eng='Dry Red 🍷 2000₸',
            ru='Красное сухое 🍷 2000₸',
            kz='Кызыл құрғақ 🍷 2000₸'
        ),
        price=2000,
        item_id='dry_red'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Dry White 🥂 2000₸',
            ru='Белое сухое 🥂 2000₸',
            kz='Құрғақ ақ 🥂 2000₸'
        ),
        price=2000,
        item_id='dry_white'
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
    MenuItem(
        name=MultiLangText(
            eng='<-Main menu',
            ru='<-Главное меню',
            kz='<-Басты мәзір',
        ),
        price=0,
        item_id='lang'
    ),
]
