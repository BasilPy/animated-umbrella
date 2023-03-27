from menus.models import MenuItem, MultiLangText

all_other_drinks = [
    MenuItem(
        name=MultiLangText(
            eng='250мл * Red BULL classic 🧚🏾‍ ️1500₸',
            ru='250мл * RED BULL classic 🧚🏾‍ ️1500₸',
            kz='250ml * RED BULL classic 🧚🏾‍ ️1500₸'
        ),
        price=1500,
        item_id='red_bull'
    ),
    MenuItem(
        name=MultiLangText(
            eng='250мл * Red BULL sugar-free 🧚🏾‍ ️1500₸',
            ru='250мл * RED BULL sugar-free 🧚🏾‍ ️1500₸',
            kz='250ml * RED BULL sugar-free 🧚🏾‍ ️1500₸'
        ),
        price=1500,
        item_id='red_bull_free'
    ),
    MenuItem(
        name=MultiLangText(
            eng='250ml * Cola classic 1000₸',
            ru='250ml * Cola classic 1000₸',
            kz='250мл * Cola classic 1000₸'
        ),
        price=1000,
        item_id='cola'
    ),
    MenuItem(
        name=MultiLangText(
            eng='250ml * Cola sugar-free 1000₸',
            ru='250ml * Cola sugar-free 1000₸',
            kz='250мл * Cola sugar-free 1000₸'
        ),
        price=1000,
        item_id='cola_free'
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
