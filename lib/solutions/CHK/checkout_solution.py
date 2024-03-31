

# noinspection PyUnusedLocal
# skus = unicode string


def calc_items_quantity(skus: str) -> dict:
    dict_with_item_quantity = dict()
    for letter in skus:
        if letter in dict_with_item_quantity.keys():
            continue
        dict_with_item_quantity[letter] = skus.count(letter)
    return dict_with_item_quantity

def apply_

def checkout(skus):
    print(skus)
    raise NotImplementedError()
