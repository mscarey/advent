import pytest

import dec10


class TestDec10:
    def test_get_data(self):
        assert dec10.get_data()[0] == "[({(<(())[]>[[{[]{<()<>>"

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("[({(<(())[]>[[{[]{<()<>>", ""),
            ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
            ("[[<[([]))<([[{}[[()]]]", ")"),
            ("[{[{({}]{}}([{[{{{}}([]", "]"),
            ("[<(<(<(<{}))><([]([]()", ")"),
            ("<{([([[(<>()){}]>(<<{{", ">"),
        ],
    )
    def test_check_corrupted(self, text, expected):

        assert dec10.check_corrupted(text) == expected

    def test_get_score_toy(self):
        data = dec10.get_data(toy=True)
        assert sum(dec10.get_score(row) for row in data) == 26397

    def test_get_score_real(self):
        data = dec10.get_data(toy=False)
        assert sum(dec10.get_score(row) for row in data) == 268845

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("])}>", 294),
            ("}}]])})]", 288957),
            (")}>]})", 5566),
            ("}}>}>))))", 1480781),
            ("]]}}]}]}>", 995444),
        ],
    )
    def test_score_completion_string(self, text, expected):
        assert dec10.score_completion_string(text) == expected

    def test_filter_corrupted(self):
        data = dec10.get_data(toy=True)
        filtered = dec10.filter_corrupted(data)
        assert len(filtered) == 5

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
            ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ],
    )
    def test_get_autocomplete(self, text, expected):
        assert dec10.get_autocomplete(text) == expected

    def test_get_autocompletes_toy(self):
        data = dec10.get_data(toy=True)
        scores = dec10.get_autocomplete_scores(data)
        assert len(scores) == 5

    def test_get_middle_score_toy(self):
        data = dec10.get_data(toy=True)
        middle = dec10.get_middle_score(data)
        assert middle == 288957

    def test_get_middle_score_real(self):
        data = dec10.get_data(toy=False)
        middle = dec10.get_middle_score(data)
        assert middle == 4038824534
