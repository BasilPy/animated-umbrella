from menus.models import MultiLangText, FinishFork, MenuItem

new_order = FinishFork(
    title=MultiLangText(
        eng='\nYou can change the language in "☰Menu".',
        ru='\nВы можете изменить язык в «☰Menu».',
        kz='\nТілді "☰Menu" арқылы өзгертуге болады.'
    ),
    forks=[
        MenuItem(
            name=MultiLangText(
                eng='New order',
                ru='Новый заказ',
                kz='Жаңа тапсырыс',
            ),
            price=0,
            item_id="lang"
        ),
    ]
)