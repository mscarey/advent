import pytest

import dec7


class TestCrabs:
    def test_cheapest(self):
        result = dec7.find_cheapest(positions=dec7.TOY)
        assert result == 2

    @pytest.mark.parametrize("guess, cost", [(1, 41), (2, 37), (3, 39), (10, 71)])
    def test_cost_toy(self, guess, cost):
        positions = dec7.TOY
        assert dec7.find_cost(answer=guess, positions=positions) == cost

    def test_real_cheapest(self):
        result = dec7.find_cheapest(positions=dec7.REAL)
        assert result == 333

    def test_find_fuel_for_cheapest(self):
        result = dec7.find_fuel_for_cheapest(positions=dec7.TOY)
        assert result == 37

    def test_find_fuel_for_cheapest_real(self):
        result = dec7.find_fuel_for_cheapest(positions=dec7.REAL)
        assert result == 348664

    @pytest.mark.parametrize("guess, cost", [(2, 206), (5, 168)])
    def test_cost_crabstyle_toy(self, guess, cost):
        positions = dec7.TOY
        assert dec7.find_cost_crabstyle(guess=guess, positions=positions) == cost

    def test_cheapest(self):
        result = dec7.find_cheapest_crabstyle(positions=dec7.TOY)
        assert result == 5

    def test_find_fuel_for_cheapest_crabstyle(self):
        result = dec7.find_fuel_for_cheapest_crabstyle(positions=dec7.TOY)
        assert result == 168

    def test_find_fuel_for_cheapest_crabstyle_real(self):
        result = dec7.find_fuel_for_cheapest_crabstyle(positions=dec7.REAL)
        assert result == 168
