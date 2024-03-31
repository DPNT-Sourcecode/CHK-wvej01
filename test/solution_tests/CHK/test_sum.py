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
        assert checkout_solution.calc_items_quantity("AA") == {"A": 2}
        assert checkout_solution.calc_items_quantity("AAABBBCCC") == {"A": 3, "B": 3, "C": 3}
        assert checkout_solution.calc_items_quantity("AABCCCC") == {"A": 2, "B": 1, "C": 4}
   
