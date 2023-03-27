from menus.models import MenuItem, MultiLangText

all_snacks = [
    MenuItem(
        name=MultiLangText(
            eng='Nachos 🍴 1000₸',
            ru='Начос 🍴 1000₸',
            kz='Нахосч 🍴 1000₸',
        ),
        price=1000,
        item_id='nachos'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Kurt ⚪ 1000₸',
            ru='Курт ⚪ 1000₸ ',
            kz='Курт ⚪ 1000₸ '
        ),
        price=1000,
        item_id='kurt'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Penuts 🥥 1000₸',
            ru='Арахис 🥥 1000₸',
            kz='Жержаңғақ 🥥 1000₸',
        ),
        price=1000,
        item_id='nuts'
    ),

    MenuItem(
        name=MultiLangText(
            eng='Chechil @ 1000₸',
            ru='Чечил @ 1000₸ ',
            kz='Чечил @ 1000₸ '
        ),
        price=1000,
        item_id='сhechil'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Dried meat with croutons @ 2000₸',
            ru='Вяленое мясо с сухариками @ 2000₸',
            kz='Крутон қосылған кептірілген ет @ 2000₸'
        ),
        price=2000,
        item_id='dried_meat'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Sandwiches @ 2000₸',
            ru='Cэндвичи @ 2000₸',
            kz='Сэндвичи @ 2000₸'
        ),
        price=2000,
        item_id='dried_meat'
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
