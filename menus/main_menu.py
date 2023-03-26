from menus.items_menus_keybords.cocktails import all_cocktails
from menus.items_menus_keybords.beer_and_cider import all_beer_cider
from menus.items_menus_keybords.wines import all_wines
from menus.items_menus_keybords.tinctures import all_tinctures
from menus.items_menus_keybords.snacks import all_snacks
from menus.items_menus_keybords.tea_teapot import all_tea
from menus.items_menus_keybords.other_drinks import all_other_drinks
from menus.items_menus_keybords.lemonades import all_lemonades
from menus.models import Menu, MenuCategory, MultiLangText


menu = Menu(
    title_categories=MultiLangText(
            eng='Chose category:',
            ru='Выберите категорию:',
            kz='Санат таңдаңыз:'
    ),
    categories=[
        MenuCategory(
            name=MultiLangText(
                eng='Cocktails',
                ru='Коктели',
                kz='Коктейльдер'
            ),
            instruction=MultiLangText(
                eng='Choose a cocktail 🍸 400мл:',
                ru='Выберите коктейль 🍸 400мл:',
                kz='Коктейльді таңдаңыз 🍸 400мл:',
            ),
            category_items=all_cocktails,
            item_id="cocktails"
        ),

        MenuCategory(
            name=MultiLangText(
                eng='Bear & Cider',
                ru='Пиво & Сидр',
                kz='Сыра & Сидр'
            ),
            instruction=MultiLangText(
                eng='Choose a bear or a cider 🍺🍏 500мл:',
                ru='Выберите пиво или сидр 🍺🍏 500мл:',
                kz='Пиво немесе сидрді таңдаңыз 🍺🍏 500мл:',
            ),
            category_items=all_beer_cider,
            item_id="beer_cider"
        ),

        MenuCategory(
            name=MultiLangText(
                eng='Wine',
                ru='Вино',
                kz='Шарап'
            ),
            instruction=MultiLangText(
                eng='Choose a wine',
                ru='Выберите вино ',
                kz='Шарап таңдаңыз ',
            ),
            category_items=all_wines,
            item_id="wine"
        ),

        MenuCategory(
            name=MultiLangText(
                eng='Tinctures * shot',
                ru='Настойки * shot',
                kz='Тұндырмалар * shot'
            ),
            instruction=MultiLangText(
                eng='Choose a tincture 🍋🍍🍇 50мл:',
                ru='Выберите настойку 🍋🍍🍇 50мл:',
                kz='Тұнбаны таңдаңыз 🍋🍍🍇 50мл:',
            ),
            category_items=all_tinctures,
            item_id="tinctures"
        ),

        MenuCategory(
            name=MultiLangText(
                eng='Snacks',
                ru='Снеки',
                kz='Жеңіл тағамдар'
            ),
            instruction=MultiLangText(
                eng='Choose a snack 🍴',
                ru='Выберите snack 🍴',
                kz='Жеңіл тамақ таңдаңыз 🍴',
            ),
            category_items=all_snacks,
            item_id="snacks"
        ),
        MenuCategory(
            name=MultiLangText(
                eng='TEA',
                ru='ЧАЙ',
                kz='ШАЙ'
            ),
            instruction=MultiLangText(
                eng='Choose tea Cup/Teapot',
                ru='Выберите чай Чашка/Чайник',
                kz='Шай кесе/шәйнекті таңдаңыз',
            ),
            category_items=all_tea,
            item_id="tea"
        ),
        MenuCategory(
            name=MultiLangText(
                eng='Lemonades',
                ru='Лимонады',
                kz='Лимонадтар'
            ),
            instruction=MultiLangText(
                eng='Choose a lemonade',
                ru='Выберите лимонад',
                kz='Лимонадты таңдаңыз',
            ),
            category_items=all_lemonades,
            item_id="lemonades"
        ),
        MenuCategory(
            name=MultiLangText(
                eng='Other drinks',
                ru='Другие напитки',
                kz='Басқа сусындар'
            ),
            instruction=MultiLangText(
                eng='Choose a drink ',
                ru='Выберите напиток',
                kz='Сусын таңдаңыз',
            ),
            category_items=all_other_drinks,
            item_id="other_drinks"
        ),
    ]
)
