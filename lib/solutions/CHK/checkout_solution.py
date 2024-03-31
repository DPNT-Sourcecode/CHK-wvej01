

# noinspection PyUnusedLocal
# skus = unicode string

price_data_card = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

offers_data_card = {
    "A": {5: 200, 3: 130},
    "E": {2: {"B": 1}},
    "B": {2: 45},
    
}

def calc_items_quantity(skus: str) -> dict:
    data_dict = dict()
    for letter in skus:
        if letter in data_dict.keys():
            continue
        data_dict[letter] = {"total_quantity": skus.count(letter), "quantity_to_calc": skus.count(letter)}
    return data_dict

def apply_offers_price(data_dict: dict, offers_data: dict) -> dict:
    for item_name, offers_info in offers_data.items():
        item_data = data_dict.get(item_name)
        if item_data is None:
            continue
        for offer_quantity, offer_data in offers_info.items():
            quantity_to_calc_for_offer = item_data["quantity_to_calc"]
            while quantity_to_calc_for_offer >= offer_quantity:
                quantity_to_calc_for_offer -= offer_quantity
                if isinstance(offer_data, dict):
                    for item_offer, item_quantity in offer_data.items():
                        if data_dict.get(item_offer, {}).get("quantity_to_calc", 0) > 0:
                            data_dict[item_offer]["quantity_to_calc"] -= item_quantity
                else:
                    item_data["quantity_to_calc"]-= offer_quantity
                    item_data["offers_price"] = item_data.get("offers_price", 0) + offer_data
    return data_dict


def apply_regular_prices(data_dict: dict, price_data: dict) -> dict:
    for item_name, data in data_dict.items():
        data["regular_price"] = price_data.get(item_name) * data.get("quantity_to_calc", 0)
        data["quantity_to_calc"] = 0
    
    for _, data in data_dict.items():
        data["total_price"] = data.get("offers_price", 0) + data["regular_price"]
    return data_dict

def get_total_price(skus: str, offers_data, price_data):
    quantity_data = calc_items_quantity(skus)
    items_with_offers_processed = apply_offers_price(quantity_data, offers_data)
    items_with_reg_prices_processed = apply_regular_prices(items_with_offers_processed, price_data)
    return sum([data["total_price"] for _, data in items_with_reg_prices_processed.items()])


def checkout(skus: str):
    if not isinstance(skus, str):
        return -1
    for item_name in skus:
        if price_data_card.get(item_name) is None:
            return -1
    if len(skus) == 0:
        return 0
        
    return get_total_price(skus, offers_data_card, price_data_card)








