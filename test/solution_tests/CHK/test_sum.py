from solutions.CHK import checkout_solution
import pytest

price_data_card = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

offers_data_card = {
    "A": {5: 200, 3: 130},
    "B": {2: 45},
    "E": {2: {"B": 1}}
}

class TestQuantityCheck:
    def test_q_check(self):
        assert checkout_solution.calc_items_quantity("AA") == {
            "A": {"total_quantity": 2, "quantity_to_calc": 2},
        }
        assert checkout_solution.calc_items_quantity("AAABBBCCC") == {
            "A": {"total_quantity": 3, "quantity_to_calc": 3},
            "B": {"total_quantity": 3, "quantity_to_calc": 3},
            "C": {"total_quantity": 3, "quantity_to_calc": 3},
        }
        assert checkout_solution.calc_items_quantity("AABCCCC") == {
            "A": {"total_quantity": 2, "quantity_to_calc": 2},
            "B": {"total_quantity": 1, "quantity_to_calc": 1},
            "C": {"total_quantity": 4, "quantity_to_calc": 4},
        }


class TestOffersApply:
    def test_offers_apply(self):
        assert checkout_solution.apply_offers_price(
            {"A": {"total_quantity": 7, "quantity_to_calc": 7}}, offers_data_card
        ) == {"A": {"total_quantity": 7, "quantity_to_calc": 2, "offers_price": 200}}

        assert checkout_solution.apply_offers_price(
            {"B": {"total_quantity": 6, "quantity_to_calc": 6}, "D": {"total_quantity": 5, "quantity_to_calc": 5}}, offers_data_card
        ) == {
            "B": {"total_quantity": 6, "quantity_to_calc": 0, "offers_price": 135},
            "D": {"total_quantity": 5, "quantity_to_calc": 5},
        }


class TestApplyRegularPrices:
    def test_apply_regular_prices(self):
        assert checkout_solution.apply_regular_prices(
            {
                "A": {"total_quantity": 7, "quantity_to_calc": 5, "offers_price": 10},
                "B": {"total_quantity": 6, "quantity_to_calc": 10, "offers_price": 50},
            },
            price_data_card,
        ) == {
            "A": {
                "total_quantity": 7,
                "quantity_to_calc": 0,
                "offers_price": 10,
                "total_price": 260,
                "regular_price": 250,
            },
            "B": {
                "total_quantity": 6,
                "quantity_to_calc": 0,
                "offers_price": 50,
                "total_price": 350,
                "regular_price": 300,
            },
        }

class TestGetTotalPrice:
    def test_get_total_price(self):
        # assert checkout_solution.get_total_price("AABBCCC", offers_data_card, price_data_card) == 205

        # assert checkout_solution.get_total_price("AAAAABBCCC", offers_data_card, price_data_card) == 305

        # assert checkout_solution.get_total_price("AAABBBBBBCCCDDD", offers_data_card, price_data_card) == 370
        # assert checkout_solution.get_total_price("EE", offers_data_card, price_data_card) == 80
        # assert checkout_solution.get_total_price("EEB", offers_data_card, price_data_card) == 80
        # assert checkout_solution.get_total_price("EEEEBB", offers_data_card, price_data_card) == 160

        # assert checkout_solution.get_total_price("EEEB", offers_data_card, price_data_card) == 120
        
        assert checkout_solution.get_total_price("BEBEEE", offers_data_card, price_data_card) == 160
        assert checkout_solution.get_total_price("ABCDEABCDE", offers_data_card, price_data_card) == 280



