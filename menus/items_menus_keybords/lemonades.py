from menus.models import MenuItem, MultiLangText

all_lemonades = [
    MenuItem(
        name=MultiLangText(
            eng='Classical -> 1000₸',
            ru='Классический -> 1000₸',
            kz='Классикалық -> 1000₸'
        ),
        price=1000,
        item_id='сlassical'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Wild berries -> 1000₸',
            ru='Лесные ягоды -> 1000₸',
            kz='Жидектер -> 1000₸'
        ),
        price=1000,
        item_id='wild_berries'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Fruity -> 1000₸',
            ru='Фруктовый -> 1000₸',
            kz='Жемісті -> 1000₸'
        ),
        price=1000,
        item_id='fruity'
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
