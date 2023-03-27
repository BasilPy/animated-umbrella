from menus.models import MenuItem, MultiLangText

all_tea = [
    MenuItem(
        name=MultiLangText(
            eng='Black Tea 🥤 500₸',
            ru='Черный Чай 🥤 500₸',
            kz='Қара Шай 🥤 500₸'
        ),
        price=500,
        item_id='cup_tea'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Black Tea /teapot/ 1500₸',
            ru='Черный Чай /чайник/ 1500₸',
            kz='Қара Шай /шайнек/ 1500₸'
        ),
        price=1500,
        item_id='teapot'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Tashkent Tea 🥤 500₸',
            ru='Ташкентский Чай 🥤 500₸',
            kz='Ташкент шайы 🥤 500₸'
        ),
        price=500,
        item_id='tash_tea'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Tashkent Tea /teapot/ 1500₸',
            ru='Ташкентский Чай /чайник/ 1500₸',
            kz='Ташкент Шай /шайнек/ 1500₸'
        ),
        price=1500,
        item_id='tash_teapot'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Fruit and berry 🥤 500₸',
            ru='Фруктово-ягодный 🥤 500₸',
            kz='Жеміс және жидек 🥤 500₸'
        ),
        price=500,
        item_id='fruit_tea'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Fruit and berry Tea /teapot/ 1500₸',
            ru='Фруктово-ягодный Чай /чайник/ 1500₸',
            kz='Жеміс және жидек /шайнек/ 1500₸'
        ),
        price=1500,
        item_id='fruit_teapot'
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