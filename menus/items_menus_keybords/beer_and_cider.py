from menus.models import MenuItem, MultiLangText

all_beer_cider = [
    MenuItem(
        name=MultiLangText(
            eng='BAZA LAGER 🍺 2000₸',
            ru='BAZA LAGER 🍺 2000₸',
            kz='BAZA LAGER 🍺 2000₸'
        ),
        price=2000,
        item_id='baza_lager'
    ),
    MenuItem(
        name=MultiLangText(
            eng='IPA 🍺 2000₸',
            ru='IPA 🍺 2000₸',
            kz='IPA 🍺 2000₸'
        ),
        price=2000,
        item_id='dark_lager'
    ),
    MenuItem(
        name=MultiLangText(
            eng='DARK LAGER 🍺 2000₸',
            ru='Тёмный LAGER 🍺 2000₸',
            kz='DARK LAGER 🍺 2000₸'
        ),
        price=2000,
        item_id='dark_lager'
    ),

    MenuItem(
        name=MultiLangText(
            eng="CHESTER'S * 2500₸",
            ru="CHESTER'S * 2500₸",
            kz="CHESTER'S * 2500₸"
        ),
        price=2500,
        item_id='chester'
    ),
]
