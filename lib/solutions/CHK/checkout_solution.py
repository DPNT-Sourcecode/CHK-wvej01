

# noinspection PyUnusedLocal
# skus = unicode string
from price_rate_card import price_data, offers_data


def calc_items_quantity(skus: str) -> dict:
    dict_with_item_quantity = dict()
    for letter in skus:
        if letter in dict_with_item_quantity.keys():
            continue
        dict_with_item_quantity[letter] = {"quantity": skus.count(letter)}
    return dict_with_item_quantity

def apply_offers_price(dict_with_item_quantity: dict):
    for item_name, data in dict_with_item_quantity.items():
        while data["qa"]


def checkout(skus):
    print(skus)
    raise NotImplementedError()

