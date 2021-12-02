import dec1


def test_get_data():
    result = dec1.get_data(1, toy=True)
    assert result[0] == 199


def test_count_dives():
    data = dec1.get_data(1, toy=True)
    result = dec1.count_dives(data)
    assert result == 7


def test_count_real_dives():
    data = dec1.get_data(1, toy=False)
    result = dec1.count_dives(data)
    assert result == 1688


def test_window_dives():
    data = dec1.get_data(1, toy=True)
    result = dec1.window_dives(data)
    assert result == 5


def test_window_dives_real():
    data = dec1.get_data(1, toy=False)
    result = dec1.window_dives(data)
    assert result == 1728
