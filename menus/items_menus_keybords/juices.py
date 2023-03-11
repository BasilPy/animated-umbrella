from menus.models import MultiLangText, FinishFork, MenuItem

all_juices = [
    MenuItem(
        name=MultiLangText(
            eng='j.Apple 🍎 1000₸',
            ru='c.Яблоко 🍎 1000₸',
            kz='ш.Алма 🍎 1000₸'
        ),
        price=1000,
        item_id='apple_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='j.Cherry 🍒 1000₸',
            ru='с.Вишня 🍒 1000₸',
            kz='ш.Шие 🍒 1000₸'
        ),
        price=1000,
        item_id='cherry_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='j.Orange 🍊 1000₸',
            ru='с.Апєльсин 🍊 1000₸',
            kz='ш.Апельсин 🍊 1000₸'
        ),
        price=1000,
        item_id='orange_j'
    ),
]

all_juice_fork = FinishFork(
    title=MultiLangText(
        eng="Choose a juice:",
        ru="Выберите сок:",
        kz="Шырынды таңдаңыз"
    ),
    forks=all_juices
)
