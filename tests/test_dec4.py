import dec4


class TestDec3:
    def test_totals(self):
        data = dec4.get_data(toy=True)
        assert data[0][0] == 22
        assert data[5] == []

    def test_call_1(self):
        boardset = dec4.TOY_BOARDS
        boardset.hear_call(7)
        assert boardset.boards[0].called[2] == [False, False, False, False, True]

    def test_call_2(self):
        boardset = dec4.TOY_BOARDS
        boardset.hear_call(7)
        boardset.hear_call(16)
        assert boardset.boards[0].called[2] == [False, False, False, True, True]

    def test_call_5(self):
        boardset = dec4.TOY_BOARDS
        for call in dec4.toy_calls[:5]:
            boardset.hear_call(call)
        assert boardset.boards[0].called[0] == [False, False, False, True, False]

    def test_almost_win(self):
        boards = dec4.TOY_BOARDS
        for call in dec4.toy_calls[:11]:
            boards.hear_call(call)
        assert boards.check_for_win() is None

    def test_win(self):
        boards = dec4.TOY_BOARDS
        for call in dec4.toy_calls[:12]:
            boards.hear_call(call)
        assert boards.check_for_win() == 2
