

# noinspection PyUnusedLocal
# skus = unicode string
from price_rate_card import price_data, offers_data
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    quantity: int
    

def calc_items_quantity(skus: str) -> dict:
    dict_with_item_quantity = dict()
    for letter in skus:
        if letter in dict_with_item_quantity.keys():
            continue
        dict_with_item_quantity[letter] = {"quantity": skus.count(letter)}
    return dict_with_item_quantity

def apply_offers_price(dict_with_item_quantity: dict)


def checkout(skus):
    print(skus)
    raise NotImplementedError()


