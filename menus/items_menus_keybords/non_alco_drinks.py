from menus.models import MenuItem, MultiLangText

all_non_alco = [
    MenuItem(
        name=MultiLangText(
            eng='330ml ◇ Non-alcoholic_beer 1000₸',
            ru='330мл ◇ Безалкогольное піво 1000₸',
            kz='330мл ◇ Алкогольсіз сыра 1000₸'
        ),
        price=1000,
        item_id='non_a_beer'
    ),
    MenuItem(
        name=MultiLangText(
            eng='330ml ◇ Cola 1000₸',
            ru='330ml ◇ Cola 1000₸',
            kz='330мл ◇ COLA 1000₸'
        ),
        price=2000,
        item_id='cola'
    ),
    MenuItem(
        name=MultiLangText(
            eng='330мл ◇ Red BULL 🧚🏾‍♀️1000₸',
            ru='330мл ◇ RED BULL 🧚🏾‍♀️1000₸',
            kz='330ml ◇ RED BULL 🧚🏾‍♀️1000₸'
        ),
        price=1000,
        item_id='red_bull'
    ),
    MenuItem(
        name=MultiLangText(
            eng='330мл ◇ Juice + 1000₸',
            ru='330мл ◇ COK + 1000₸',
            kz='330мл ◇ ШЫРЫН + 1000₸'
        ),
        price=2000,
        item_id='juice'
    ),
    MenuItem(
        name=MultiLangText(
            eng='400ml ◇ Tea 🥤 500₸',
            ru='400мл ◇ Чай 🥤 500₸',
            kz='400мл ◇ Шай 🥤 500₸'
        ),
        price=500,
        item_id='tea'
    ),
    MenuItem(
        name=MultiLangText(
            eng='400мл ◇ Сoffee ☕ 500₸',
            ru='400мл ◇ Кофє ☕ 500₸',
            kz='400мл ◇ Кофе ☕ 500₸'
        ),
        price=500,
        item_id='coffee'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Water 🧊 500₸',
            ru='500мл ◇ Вода 🧊 500₸',
            kz='500мл ◇ Су 🧊 500₸'
        ),
        price=500,
        item_id='water'
    ),

]
