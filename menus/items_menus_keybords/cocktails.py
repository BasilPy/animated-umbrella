from menus.models import MenuItem, MultiLangText

all_cocktails = [
    MenuItem(
        name=MultiLangText(
            eng='ABSOLUT with juice 🍹 2000₸',
            ru='ABSOLUT c соком 🍹2000₸',
            kz='Шырын қосылған ABSOLUTE 🍹 2000₸'
        ),
        price=2000,
        item_id='absolut_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='JAMESON with juice 🥃 2000₸',
            ru='JAMESON с соком 🥃 2000₸',
            kz='Шырын қосылған JAMESON 🥃 2000₸'
        ),
        price=2000,
        item_id='jameson_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Gin and tonic 🍸 2000₸',
            ru='ДЖИН ТОНИК 🍸 2000₸',
            kz='Джин және тоник 🍸 2000₸'
        ),
        price=2000,
        item_id='gin_ton'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Rum with mint soda 🥃 2000₸',
            ru='РОМ с мятной содовой 🥃 2000₸',
            kz='Жалбыз содасы бар ром 🥃 2000₸'
        ),
        price=2000,
        item_id='rom_soda'
    )
]
