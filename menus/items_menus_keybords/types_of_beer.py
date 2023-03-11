from menus.models import MenuItem, MultiLangText

all_bears = [
    MenuItem(
        name=MultiLangText(
            eng='500мл ◇ HINEKEN 🍺 1500₸',
            ru='500мл ◇ HINEkEN 🍺 1500₸',
            kz='500ml ◇ Hineken 🍺 1500₸'
        ),
        price=1500,
        item_id='hineken'
    ),
    MenuItem(
        name=MultiLangText(
            eng='300мл ◇ MILLER 🍺 1500₸',
            ru='300мл ◇ MiLLeR 🍺 1500₸',
            kz='300ml ◇ Miller 🍺 1500₸'
        ),
        price=1500,
        item_id='miller'
    ),
    MenuItem(
        name=MultiLangText(
            eng='500мл ◇ draft 🍺 1500₸',
            ru='500мл ◇ Разливное 🍺 1500₸',
            kz='500мл ◇ Құйылмалы 🍺 1500₸',
        ),
        price=1500,
        item_id='draft'
    ),
]
