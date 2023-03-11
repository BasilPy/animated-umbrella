from menus.models import MenuItem, MultiLangText

all_ciders = [
    MenuItem(
        name=MultiLangText(
            eng='CHESTER ◇ 2000₸',
            ru='CHЄSTER ◇ 2000₸',
            kz='Chester ◇ 2000₸'
        ),
        price=2000,
        item_id='chester'
    ),
    MenuItem(
        name=MultiLangText(
            eng='BOZY ◇ 1500₸',
            ru='BOzY ◇ 1500₸',
            kz='Bozy ◇ 1500₸',
        ),
        price=1500,
        item_id='bozy'
    ),
]
