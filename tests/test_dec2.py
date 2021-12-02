import dec2


def test_get_data():
    result = dec2.get_data(2, toy=True)
    assert result[0] == "forward 5"


def test_navigate():
    data = dec2.get_data(2, toy=True)
    x, y = dec2.navigate(data)
    assert x == 15
    assert y == 10


def test_get_answer():
    data = dec2.get_data(2, toy=True)
    result = dec2.get_answer(data)
    assert result == 150


def test_navigate_real():
    data = dec2.get_data(2, toy=False)
    x, y = dec2.navigate(data)
    assert x == 1962
    assert y == 987


def test_get_answer_real():
    data = dec2.get_data(2, toy=False)
    result = dec2.get_answer(data)
    assert result == 1936494


def test_aim():
    data = dec2.get_data(2, toy=True)
    x, y = dec2.aim(data)
    assert x == 15
    assert y == 60


def test_get_aim_answer():
    data = dec2.get_data(2, toy=True)
    result = dec2.get_aim_answer(data)
    assert result == 900


def test_aim_real():
    data = dec2.get_data(2, toy=False)
    x, y = dec2.aim(data)
    assert x == 1962
    assert y == 1017893


def test_get_aim_answer_real():
    data = dec2.get_data(2, toy=False)
    result = dec2.get_aim_answer(data)
    assert result == 1997106066
