

# noinspection PyUnusedLocal
# skus = unicode string

price_data = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

offers_data = {
    "A": {3: 130},
    "B": {2: 45}
}

def calc_items_quantity(skus: str) -> dict:
    data_dict = dict()
    for letter in skus:
        if letter in data_dict.keys():
            continue
        data_dict[letter] = {"total_quantity": skus.count(letter)}
    return data_dict

def apply_offers_price(data_dict: dict) -> dict:
    for item_name, data in data_dict.items():
        data["quantity_to_calc"] = data["total_quantity"]
        offers = offers_data.get(item_name)
        if offers is None:
            continue
        for offer_quantity, offer_price in offers.items():
            while int(data["quantity_to_calc"]) >= offer_quantity:
                data["quantity_to_calc"]-= offer_quantity
                data["offers_price"] = data.get("offers_price", 0) + offer_price
    return data_dict


def apply_regular_prices(data_dict: dict) -> dict:
    for item_name, data in data_dict.items():
        data["regular_price"] = price_data.get(item_name) * data["quantity_to_calc"]
        data["quantity_to_calc"] = 0
    
    for _, data in data_dict.items():
        data["total_price"] = data["offers_price"] + data["regular_price"]
    return data_dict

def get_total_price(skus: str):
    quantity_data = calc_items_quantity(skus)
    items_with_offers_proccessed = apply_offers_price(quantity_data)


def checkout(skus: str):
    if not isinstance(skus, str):
        return -1
    for item_name in skus:
        if price_data.get(item_name) is None:
            return -1
    if len(skus) == 0:
        return -1
    

    print(skus)
    raise NotImplementedError()





