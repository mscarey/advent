import dec11


class TestDec11:
    def test_get_data(self):
        assert dec11.get_data()[0] == [5, 4, 8, 3, 1, 4, 3, 2, 2, 3]

    def test_two_steps(self):
        data = dec11.get_data()
        grid, total_flashes = dec11.multiple_steps(data, 2)
        assert grid[1] == [5, 0, 8, 9, 0, 8, 7, 0, 5, 4]
