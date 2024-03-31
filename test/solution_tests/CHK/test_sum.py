from solutions.CHK import checkout_solution
import pytest

# class TestCheckout():
#     def test_checkout(self):

#         "AAAAAABBBBCCCC"
#         assert checkout_solution.compute(1, 2) == 3

#         with pytest.raises(ValueError):
#             sum_solution.compute(-5, 2)

#         with pytest.raises(ValueError):
#             sum_solution.compute(5, 101)


class TestQuantityCheck():
    def test_q_check(self):
        assert checkout_solution.calc_items_quantity("AA") == {"A": {"total_quantity": 2}}
        assert checkout_solution.calc_items_quantity("AAABBBCCC") == {"A": {"total_quantity": 3}, "B": {"total_quantity": 3}, "C": {"total_quantity": 3}}
        assert checkout_solution.calc_items_quantity("AABCCCC") == {"A": {"total_quantity": 2}, "B": {"total_quantity": 1}, "C": {"total_quantity": 4}}
   
class TestOffersApply():
    def test_offers_apply(self):
        assert checkout_solution.apply_offers_price({"A": {"total_quantity": 7}}) == {"A": {"total_quantity": 7, "quantity_to_calc": 1, "offers_price": 260}}

        assert checkout_solution.apply_offers_price({"A": {"total_quantity": 7}}) == {"A": {"total_quantity": 7, "quantity_to_calc": 1, "offers_price": 260}}

        assert checkout_solution.apply_offers_price({"B": {"total_quantity": 6}, "D": {"total_quantity": 5}}) == {"B": {"total_quantity": 6, "quantity_to_calc": 0, "offers_price": 135}, "D": {"total_quantity": 5, "quantity_to_calc": 5}}


