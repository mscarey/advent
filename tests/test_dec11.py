import dec11


class TestDec11:
    def test_get_data(self):
        assert dec11.get_data()[0] == [5, 4, 8, 3, 1, 4, 3, 2, 2, 3]

    def test_two_steps(self):
        data = dec11.get_data()
        grid, total_flashes = dec11.multiple_steps(data, 2)
        assert grid[0] == [8, 8, 0, 7, 4, 7, 6, 5, 5, 5]
        assert grid[1] == [5, 0, 8, 9, 0, 8, 7, 0, 5, 4]
        assert grid[2] == [8, 5, 9, 7, 8, 8, 9, 6, 0, 8]
        assert grid[3] == [8, 4, 8, 5, 7, 6, 9, 6, 0, 0]
        assert grid[4] == [8, 7, 0, 0, 9, 0, 8, 8, 0, 0]

    def test_10_steps(self):
        data = dec11.get_data()
        grid, total_flashes = dec11.multiple_steps(data, 10)
        assert total_flashes == 204

        assert grid[1] == [0, 0, 3, 1, 1, 1, 2, 0, 0, 9]

    def test_100_steps(self):
        data = dec11.get_data()
        grid, total_flashes = dec11.multiple_steps(data, 100)
        assert total_flashes == 1656
        assert grid[1] == [0, 7, 4, 9, 7, 6, 6, 9, 1, 8]

    def test_100_steps_real(self):
        data = dec11.get_data(toy=False)
        grid, total_flashes = dec11.multiple_steps(data, 100)
        assert total_flashes == 1739

    def test_all_flash_simultaneously(self):
        data = dec11.get_data()
        assert dec11.all_flash_simultaneously(data) == 195

    def test_all_flash_simultaneously(self):
        data = dec11.get_data(toy=False)
        assert dec11.all_flash_simultaneously(data) == 324
