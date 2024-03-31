from solutions.CHK import checkout_solution
import pytest

class TestSum():
    def test_sum(self):
        assert checkout_solution.compute(1, 2) == 3

        with pytest.raises(ValueError):
            sum_solution.compute(-5, 2)

        with pytest.raises(ValueError):
            sum_solution.compute(5, 101)