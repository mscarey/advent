import dec4


class TestDec4:
    def test_totals(self):
        data = dec4.get_data(toy=True)
        assert data[0][0] == 22
        assert data[5] == []

    def test_call_1(self):
        boardset = dec4.make_toy_boards()
        boardset.hear_call(7)
        assert boardset.boards[0].called[2] == [False, False, False, False, True]

    def test_call_2(self):
        boardset = dec4.make_toy_boards()
        boardset.hear_call(7)
        boardset.hear_call(16)
        assert boardset.boards[0].called[2] == [False, False, False, True, True]

    def test_call_5(self):
        boardset = dec4.make_toy_boards()
        for call in dec4.toy_calls[:5]:
            boardset.hear_call(call)
        assert boardset.boards[0].called[0] == [False, False, False, True, False]

    def test_almost_win(self):
        boards = dec4.make_toy_boards()
        for call in dec4.toy_calls[:11]:
            boards.hear_call(call)
        assert boards.check_for_win() is None

    def test_win(self):
        boards = dec4.make_toy_boards()
        for call in dec4.toy_calls[:12]:
            boards.hear_call(call)
        assert boards.check_for_win() == 2

    def test_find_score(self):
        boardset = dec4.make_toy_boards()
        last_called, unmarked_points = boardset.find_score(calls=dec4.toy_calls)
        assert last_called == 24
        assert unmarked_points == 188

    def test_answer(self):
        boardset = dec4.make_toy_boards()
        assert boardset.find_answer(calls=dec4.toy_calls) == 4512

    def test_real_score(self):
        boardset = dec4.make_real_boards()
        last_called, unmarked_points = boardset.find_score(calls=dec4.real_calls)
        assert last_called == 14
        assert unmarked_points == 741

    def test_number_of_real_boards(self):
        boardset = dec4.make_real_boards()
        assert len(boardset.boards) == 100

    def test_real_answer(self):
        boardset = dec4.make_real_boards()
        assert boardset.find_answer(calls=dec4.real_calls) == 10374

    def test_last_score(self):
        boardset = dec4.make_toy_boards()
        last_called, unmarked_points = boardset.get_all_scores(calls=dec4.toy_calls)[-1]
        assert last_called == 13
        assert unmarked_points == 148

    def test_last_answer(self):
        boardset = dec4.make_toy_boards()
        assert boardset.get_last_answer(calls=dec4.toy_calls) == 1924

    def test_real_last_answer(self):
        boardset = dec4.make_real_boards()
        assert boardset.get_last_answer(calls=dec4.real_calls) == 24742
