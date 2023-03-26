from menus.models import MenuItem, MultiLangText

all_other_drinks = [
    MenuItem(
        name=MultiLangText(
            eng='250мл * Red BULL 🧚🏾‍ ️1500₸',
            ru='250мл * RED BULL 🧚🏾‍ ️1500₸',
            kz='250ml * RED BULL 🧚🏾‍ ️1500₸'
        ),
        price=1500,
        item_id='red_bull'
    ),
    MenuItem(
        name=MultiLangText(
            eng='250ml * Cola 1000₸',
            ru='250ml * Cola 1000₸',
            kz='250мл * COLA 1000₸'
        ),
        price=1000,
        item_id='cola'
    ),
    MenuItem(
        name=MultiLangText(
            eng='BORJOMI ~ 1000₸',
            ru='BORJOMI ~ 1000₸',
            kz='BORJOMI ~ 1000₸'
        ),
        price=1000,
        item_id='borjomi'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Water ~ 500₸',
            ru='500мл ◇ Вода ~ 500₸',
            kz='500мл ◇ Су ~ 500₸'
        ),
        price=500,
        item_id='water'
    ),

]
