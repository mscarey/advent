import dec3


class TestDec3:
    def test_totals(self):
        data = dec3.get_data(toy=True)
        assert dec3.totals(data)[0] == 7

    def test_common_digits(self):
        data = dec3.get_data(toy=True)
        assert dec3.common_digits(data) == ["1", "0", "1", "1", "0"]

    def test_gamma(self):
        data = dec3.get_data(toy=True)
        assert dec3.gamma(data) == int("10110", 2)

    def test_epsilon(self):
        data = dec3.get_data(toy=True)
        assert dec3.epsilon(data) == int("01001", 2)

    def test_answer(self):
        data = dec3.get_data(toy=True)
        assert dec3.answer(data) == 198

    def test_answer_real(self):
        data = dec3.get_data(toy=False)
        assert dec3.answer(data) == 852500

    def test_oxygen(self):
        data = dec3.get_data(toy=True)
        assert dec3.oxygen(data) == int("10111", 2)

    def test_co2(self):
        data = dec3.get_data(toy=True)
        assert dec3.co2(data) == int("01010", 2)

    def test_life_support(self):
        data = dec3.get_data(toy=True)
        assert dec3.life_support(data) == 230

    def test_life_support_real(self):
        data = dec3.get_data(toy=False)
        assert dec3.life_support(data) == 1007985
