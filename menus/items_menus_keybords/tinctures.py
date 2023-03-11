from menus.models import MenuItem, MultiLangText

all_tinctures = [
    MenuItem(
        name=MultiLangText(
            eng='t.Cherry 🍒 1500₸',
            ru='н.Вишня 🍒 1500₸',
            kz='т.Шие 🍒 1500₸'
        ),
        price=1500,
        item_id='t_cherry'
    ),
    MenuItem(
        name=MultiLangText(
            eng='t.Currant ◇ 1500₸',
            ru='н.Смородина ◇ 1500₸',
            kz='т.Қарақат ◇ 1500₸'
        ),
        price=1500,
        item_id='t_currant'
    ),
    MenuItem(
        name=MultiLangText(
            eng='t.Sea buckthorn ◇ 1500₸',
            ru='н.Облепиха ◇ 1500₸',
            kz='т.Теңіз шырғаны ◇ 1500₸'
        ),
        price=1500,
        item_id='t_sea_buckthorn'
    ),
    MenuItem(
        name=MultiLangText(
            eng='t.Cranberry ◇ 1500₸',
            ru='н.Клюква ◇ 1500₸',
            kz='т.Мүкжидек ◇ 1500₸'
        ),
        price=1500,
        item_id='t_cranberry'
    )
]
