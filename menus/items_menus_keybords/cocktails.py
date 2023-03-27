from menus.models import MenuItem, MultiLangText

all_cocktails = [
    MenuItem(
        name=MultiLangText(
            eng='WHISKEY COLA 🥃 2500₸',
            ru='WHISKEY COLA 🥃 2500₸',
            kz='WHISKEY COLA 🥃 2500₸'
        ),
        price=2500,
        item_id='whiskey_cola'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Gin and tonic 🍸 2500₸',
            ru='ДЖИН ТОНИК 🍸 2500₸',
            kz='Джин және тоник 🍸 2500₸'
        ),
        price=2500,
        item_id='gin_ton'
    ),
    MenuItem(
        name=MultiLangText(
            eng='ORANGE&SPRITE 🥤 2500₸',
            ru='ORANGE&SPRITE 🥤 2500₸',
            kz='ORANGE&SPRITE 🥤 2500₸'
        ),

        price=2500,
        item_id='orange_sprite'
    ),
    MenuItem(
        name=MultiLangText(
            eng='SCREWDRIVER 🥤 2500₸',
            ru='SCREWDRIVER 🥤 2500₸',
            kz='SCREWDRIVER 🥤 2500₸'
        ),

        price=2500,
        item_id='screwdriver'
    ),
    MenuItem(
        name=MultiLangText(
            eng='CUBA LIBRE 🥤 2500₸',
            ru='CUBA LIBRE 🥤 2500₸',
            kz='CUBA LIBRE 🥤 2500₸'
        ),

        price=2500,
        item_id='cuba_libre'
    ),
    MenuItem(
        name=MultiLangText(
            eng='PINA COLADA LITE 🥤 2500₸',
            ru='PINA COLADA LITE 🥤 2500₸',
            kz='PINA COLADA LITE 🥤 2500₸'
        ),

        price=2500,
        item_id='pina_colada_lite'
    ),
    MenuItem(
        name=MultiLangText(
            eng='TOM COLLINS 🥤 2500₸',
            ru='TOM COLLINS 🥤 2500₸',
            kz='TOM COLLINS 🥤 2500₸'
        ),

        price=2500,
        item_id='tom_collins'
    ),
    MenuItem(
        name=MultiLangText(
            eng='PALOMA 🥤 2500₸',
            ru='PALOMA 🥤 2500₸',
            kz='PALOMA 🥤 2500₸'
        ),

        price=2500,
        item_id='paloma'
    ),
    MenuItem(
        name=MultiLangText(
            eng='APEROL SPRITZ 🥤 2500₸',
            ru='APEROL SPRITZ 🥤 2500₸',
            kz='APEROL SPRITZ 🥤 2500₸'
        ),

        price=2500,
        item_id='aperol_spritz'
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
