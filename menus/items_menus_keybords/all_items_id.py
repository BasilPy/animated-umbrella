from menus.items_menus_keybords.cocktails import all_cocktails
from menus.items_menus_keybords.types_of_beer import all_bears
from menus.items_menus_keybords.types_of_cider import all_ciders
from menus.items_menus_keybords.tinctures import all_tinctures
from menus.items_menus_keybords.snacks import all_snacks
from menus.items_menus_keybords.wines import all_wines
from menus.items_menus_keybords.non_alco_drinks import all_non_alco
from menus.items_menus_keybords.juices import all_juices
all_items = [
    'absolut_j', 'jameson_j', 'rom_soda',
    'non_a_beer', 'cola', 'red_bull', 'juice', 'tea', 'coffee', 'water',
    'nachos', 'nuts', 'dried_meat', 'kurt', 'chelel',
    't_cherry', 't_currant', 't_sea_buckthorn', 't_cranberry',
    'hineken', 'miller',
    'chester', 'bozy',
    'red_semi', 'white_dry', 'pink',
    'apple_j', 'cherry_j', 'orange_j',
]

list_of_menu_items = [all_cocktails, all_non_alco, all_snacks, all_tinctures,
                      all_bears, all_ciders, all_wines, all_juices]

all_list_id = [item.item_id for sub in list_of_menu_items for item in sub]
all_dict_id_price = {a.item_id: a.price for sublist in list_of_menu_items for a in sublist}
all_dict_id_name = {a.item_id: a.name.__getattribute__("ru") for sublist in list_of_menu_items for a in sublist}

# all_cock_prices = [item.price for item in all_cocktails]
# print(dict_id_price)
# print(list_id)
#print(all_dict_id_name["jameson_j"])
