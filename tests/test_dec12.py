import dec12


class TestDec12:
    def test_read_data(self):
        data = dec12.get_data(toy=True)
        assert data[0] == ["start", "A"]
