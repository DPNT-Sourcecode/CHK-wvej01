

# noinspection PyUnusedLocal
# skus = unicode string

price_data_card = {
  "A": 50,
  "B": 30,
  "C": 20,
  "D": 15,
  "E": 40,
  "F": 10,
  "G": 20,
  "H": 10,
  "I": 35,
  "J": 60,
  "K": 70,
  "L": 90,
  "M": 15,
  "N": 40,
  "O": 10,
  "P": 50,
  "Q": 30,
  "R": 50,
  "S": 20,
  "T": 20,
  "U": 40,
  "V": 50,
  "W": 20,
  "X": 17,
  "Y": 20,
  "Z": 21
}

offers_data_card = {
    "E": {2: {"B": 1}},
    "F": {3: {"F": 1}},
    "N": {3: {"M": 1}},
    "R": {3: {"Q": 1}},
    "U": {4: {"U": 1}},
    "A": {5: 200, 3: 130},
    "B": {2: 45},
    "H": {10: 80, 5: 45},
    "K": {2: 120},
    "P": {5: 200},
    "Q": {3: 80},
    "V": {3: 130, 2: 90}
}

multiply_offer_card = [
    {"items": ["S", "T", "X", "Y", "Z"], "total_quantity": 3, "total_price": 45}
]


def apply_multi_offers(data_dict: dict, multiply_offer: dict) -> dict:
    for offer in multiply_offer:

        total_items_quantity = sum([item_data["quantity_to_calc"] for item_name, item_data in data_dict.items() if item_name in offer["items"]])

        while total_items_quantity >= offer["total_quantity"]:

            item_price = offer["total_price"] / offer["total_quantity"]

            items_to_process = offer["total_quantity"]
            while items_to_process > 0:
                for item_name, item_data in data_dict.items():
                    if items_to_process == 0:
                        break

                    if item_name not in offer["items"] or item_data["quantity_to_calc"] == 0:
                        continue

                    max_item_price_for_multi_offer = max([price_data_card[item_name] for item_name, item_data in data_dict.items() if item_name in offer["items"] and item_data["quantity_to_calc"] > 0])
                    
                    if price_data_card[item_name] < max_item_price_for_multi_offer:
                        # breakpoint()
                        continue

                    item_quantity_to_process = min(item_data["quantity_to_calc"], items_to_process)
                    offer_price =  item_quantity_to_process * item_price
                    item_data["offers_price"] = item_data.get("offers_price", 0) + offer_price
                    item_data["quantity_to_calc"] -= item_quantity_to_process
                    items_to_process -= item_quantity_to_process

                    total_items_quantity -= item_quantity_to_process


    return data_dict



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

def get_total_price(skus: str, offers_data, price_data, multiply_offer):
    quantity_data = calc_items_quantity(skus)
    # if skus == "STX":
    #     breakpoint()
    items_with_multi_offers_processed = apply_multi_offers(quantity_data, multiply_offer)
    items_with_offers_processed = apply_offers_price(items_with_multi_offers_processed, offers_data)
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
        
    return get_total_price(skus, offers_data_card, price_data_card, multiply_offer_card)


