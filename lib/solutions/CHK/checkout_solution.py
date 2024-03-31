

# noinspection PyUnusedLocal
# skus = unicode string
from price_rate_card import price_data, offers_data


def calc_items_quantity(skus: str) -> dict:
    data_dict_with_item_quantity = dict()
    for letter in skus:
        if letter in dict_with_item_quantity.keys():
            continue
        dict_with_item_quantity[letter] = {"total_quantity": skus.count(letter)}
    return dict_with_item_quantity

def apply_offers_price(dict_with_item_quantity: dict):
    for item_name, data in dict_with_item_quantity.items():
        data["quantity_to_calc"] = data["total_quantity"]
        offers = offers_data.get(item_name)
        for offer_number, offer_price in offers:
            while data["quantity_to_calc"] < offer_number:
                data["quantity_to_calc"]-= offer_number
                data["offers_price"] = data.get("offers_price", 0) + offer_price
    return 


def checkout(skus):
    print(skus)
    raise NotImplementedError()


