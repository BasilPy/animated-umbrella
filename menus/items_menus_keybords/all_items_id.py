from menus.items_menus_keybords.cocktails import all_cocktails
from menus.items_menus_keybords.tinctures import all_tinctures
from menus.items_menus_keybords.snacks import all_snacks
from menus.items_menus_keybords.wines import all_wines
from menus.items_menus_keybords.beer_and_cider import all_beer_cider
from menus.items_menus_keybords.lemonades import all_lemonades
from menus.items_menus_keybords.tea_teapot import all_tea
from menus.items_menus_keybords.other_drinks import all_other_drinks

list_of_menu_items = [all_cocktails, all_snacks, all_tinctures, all_tea,
                      all_wines, all_lemonades, all_beer_cider, all_other_drinks]

all_list_id = [item.item_id for sub in list_of_menu_items for item in sub]
all_dict_id_price = {a.item_id: a.price for sublist in list_of_menu_items for a in sublist}
all_dict_id_name = {a.item_id: a.name.__getattribute__("ru") for sublist in list_of_menu_items for a in sublist}

# all_cock_prices = [item.price for item in all_cocktails]
# print(dict_id_price)
# print(list_id)
# print(all_dict_id_name["jameson_j"])
