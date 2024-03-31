

# noinspection PyUnusedLocal
# skus = unicode string

price_data = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

offers_data = {
    "A": [{3: 130},],
    "B": [{2: 45},]
}

def calc_items_quantity(skus: str) -> dict:
    data_dict = dict()
    for letter in skus:
        if letter in data_dict.keys():
            continue
        data_dict[letter] = {"total_quantity": skus.count(letter)}
    return data_dict

def apply_offers_price(data_dict: dict):
    for item_name, data in data_dict.items():
        data["quantity_to_calc"] = data["total_quantity"]
        offers = offers_data.get(item_name)
        for offer_number, offer_price in offers:
            while data["quantity_to_calc"] < offer_number:
                data["quantity_to_calc"]-= offer_number
                data["offers_price"] = data.get("offers_price", 0) + offer_price
    return data_dict


def checkout(skus):
    print(skus)
    raise NotImplementedError()


