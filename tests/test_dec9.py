import networkx as nx

import dec9


class TestDec9(object):
    def test_get_data_toy(self):
        assert dec9.get_data(toy=True)[0] == [2, 1, 9, 9, 9, 4, 3, 2, 1, 0]

    def test_get_low_points_toy(self):
        data = dec9.get_data(toy=True)
        assert dec9.get_low_points(data=data) == [1, 0, 5, 5]

    def test_get_risk_levels_toy(self):
        data = dec9.get_data(toy=True)
        assert dec9.get_risk_levels(data=data) == [2, 1, 6, 6]

    def test_get_risk_sum_toy(self):
        data = dec9.get_data(toy=True)
        assert dec9.get_risk_sum(data=data) == 15

    def test_get_risk_sum_toy(self):
        data = dec9.get_data(toy=False)
        assert dec9.get_risk_sum(data=data) == 575

    def test_count_components(self):
        data = dec9.get_data(toy=True)
        assert dec9.count_components(data=data) == 4

    def test_get_three_largest(self):
        data = dec9.get_data(toy=True)
        assert dec9.get_component_sizes(data=data) == [14, 9, 9, 3]

    def test_get_toy_answer(self):
        data = dec9.get_data(toy=True)
        assert dec9.product_of_component_sizes(data=data) == 1134

    def test_get_real_three_largest(self):
        data = dec9.get_data(toy=False)
        assert dec9.get_component_sizes(data=data)[:3] == [103, 100, 99]

    def test_get_real_answer(self):
        data = dec9.get_data(toy=False)
        assert dec9.product_of_component_sizes(data=data) == 1019700
