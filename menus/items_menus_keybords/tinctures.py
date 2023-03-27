from menus.models import MenuItem, MultiLangText

all_tinctures = [
    MenuItem(
        name=MultiLangText(
            eng='t.Cherry 🍒 1000₸',
            ru='н.Вишня 🍒 1000₸',
            kz='т.Шие 🍒 1000₸'
        ),
        price=1000,
        item_id='t_cherry'
    ),
    MenuItem(
        name=MultiLangText(
            eng='t.Currant # 1000₸',
            ru='н.Смородина # 1000₸',
            kz='т.Қарақат # 1000₸'
        ),
        price=1000,
        item_id='t_currant'
    ),
    MenuItem(
        name=MultiLangText(
            eng='t.Cranberry # 1000₸',
            ru='н.Клюква # 1000₸',
            kz='т.Мүкжидек # 1000₸'
        ),
        price=1000,
        item_id='t_cranberry'
    ),
    MenuItem(
        name=MultiLangText(
            eng='JÄGERMEISTER # 2000₸',
            ru='JÄGERMEISTER # 2000₸',
            kz='JÄGERMEISTER # 2000₸'
        ),
        price=2000,
        item_id='jagermeister'
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
