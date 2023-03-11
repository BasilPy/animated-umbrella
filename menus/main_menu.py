from menus.items_menus_keybords.cocktails import all_cocktails
from menus.items_menus_keybords.types_of_beer import all_bears
from menus.items_menus_keybords.types_of_cider import all_ciders
from menus.items_menus_keybords.tinctures import all_tinctures
from menus.items_menus_keybords.snacks import all_snacks
from menus.items_menus_keybords.wines import all_wines
from menus.items_menus_keybords.non_alco_drinks import all_non_alco
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
                eng='Tinctures',
                ru='Настойки',
                kz='Тұндырмалар'
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
                eng='Bear',
                ru='Пиво',
                kz='Сыра'
            ),
            instruction=MultiLangText(
                eng='Choose a bear 🍺 500мл:',
                ru='Выберите пиво 🍺 500мл:',
                kz='Сыраны таңдаңыз 🍺 500мл:',
            ),
            category_items=all_bears,
            item_id="beer"
        ),

        MenuCategory(
            name=MultiLangText(
                eng='Cider',
                ru='Сидр',
                kz='Сидр'
            ),
            instruction=MultiLangText(
                eng='Choose a ciders 🍏🍺🍐 500мл:',
                ru='Выберите сидр 🍏🍺🍐 500мл:',
                kz='Сидр таңдаңыз 🍏🍺🍐 500мл:',
            ),
            category_items=all_ciders,
            item_id="cider"
        ),

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
                eng='Non alcoholic',
                ru='Везалкогольные',
                kz='Алкогольсіз'
            ),
            instruction=MultiLangText(
                eng='Choose a non alco drink ',
                ru='Выберите безалкогольный напиток',
                kz='Алкогольсіз сусынды таңдаңыз',
            ),
            category_items=all_non_alco,
            item_id="non_alcoholic"
        ),
    ]
)
