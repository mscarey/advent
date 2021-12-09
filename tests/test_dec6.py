from dec6 import toy, grow, efficient_grow, REAL_FISH


class TestFish:
    def test_one_day(self):
        result = grow(fish=toy, days=1)
        assert result == [2, 3, 2, 0, 1]

    def test_18_days(self):
        result = grow(fish=toy, days=18)
        assert len(result) == 26

    def test_80_days(self):
        result = grow(fish=toy, days=80)
        assert len(result) == 5934

    def test_80_days_real(self):
        result = grow(fish=REAL_FISH, days=80)
        assert len(result) == 351188

    def test_e_one_day(self):
        result = efficient_grow(fish=toy, days=1)
        assert result[2] == 2
        assert result[3] == 1
        assert result[0] == 1
        assert result[5] == 0

    def test_e_two_days(self):
        result = efficient_grow(fish=toy, days=2)
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 1
        assert result[3] == 0
        assert result[4] == 0
        assert result[5] == 0
        assert result[6] == 1
        assert result[7] == 0
        assert result[8] == 1

    def test_e_18_days(self):
        result = efficient_grow(fish=toy, days=18)
        assert sum(result.values()) == 26

    def test_e_80_days(self):
        result = efficient_grow(fish=toy, days=80)
        assert sum(result.values()) == 5934

    def test_e_256_days(self):
        result = efficient_grow(fish=toy, days=256)
        assert sum(result.values()) == 26984457539

    def test_e_80_days_real(self):
        result = efficient_grow(fish=REAL_FISH, days=80)
        assert sum(result.values()) == 351188

    def test_e_256_days_real(self):
        result = efficient_grow(fish=REAL_FISH, days=256)
        assert sum(result.values()) == 1595779846729
