import pytest

import dec8

ONE_LINE = [
    [
        "acedgfb",
        "cdfbe",
        "gcdfa",
        "fbcad",
        "dab",
        "cefabd",
        "cdfgeb",
        "eafb",
        "cagedb",
        "ab",
        "|",
        "cdfeb",
        "fcadb",
        "cdfeb",
        "cdbaf",
    ]
]


class TestDec8:
    def test_get_data(self):
        assert len(dec8.get_data(toy=True)[0]) == 15

    def test_make_displays_one_line(self):

        displays = dec8.make_displays(ONE_LINE)
        assert displays[0].digits[0] == "abcdefg"
        assert displays[0].cypher[1] == "abcdf"

    def test_get_easy_digits_one_line(self):

        displays = dec8.make_displays(ONE_LINE)
        assert displays[0].count_easy_digits() == 0

    def test_make_displays_toy(self):
        data = dec8.get_data(toy=True)
        displays = dec8.make_displays(data)
        assert displays[0].digits[0] == "be"
        assert displays[0].cypher[0] == "abcdefg"

    def test_count_all_easy_digits_toy(self):
        data = dec8.get_data(toy=True)
        displays = dec8.make_displays(data)
        assert dec8.count_all_easy_digits(displays) == 26

    @pytest.mark.parametrize(
        "i, expected",
        [
            (0, 2),
            (1, 3),
            (2, 3),
            (3, 1),
            (4, 3),
            (5, 4),
            (6, 3),
            (7, 1),
            (8, 4),
            (9, 2),
        ],
    )
    def test_count_easy_digits_toy(self, i, expected):
        data = dec8.get_data(toy=True)
        displays = dec8.make_displays(data)
        assert displays[i].count_easy_digits() == expected

    def test_count_all_easy_digits_real(self):
        data = dec8.get_data(toy=False)
        displays = dec8.make_displays(data)
        assert dec8.count_all_easy_digits(displays) == 237

    def test_read_unscrambled(self):
        assert dec8.Display.read_decoded(["acdfg", "bcdf", "acf"]) == 347

    def test_assign_easy_line_toy(self):
        displays = dec8.make_displays(ONE_LINE)
        assert displays[0].assign_easy_line() == "d"

    def test_get_guesses_toy(self):
        displays = dec8.make_displays(ONE_LINE)
        guesses = list(displays[0].get_guesses())
        assert len(guesses) == 720

    def test_get_line_key_toy(self):
        displays = dec8.make_displays(ONE_LINE)
        assert displays[0].get_line_key() == "deafgbc"

    def test_encode_picture_toy(self):
        displays = dec8.make_displays(ONE_LINE)
        assert displays[0].encode_picture(picture="acf", key="deafgbc") == "abd"

    def test_get_cypher_digits_toy(self):
        displays = dec8.make_displays(ONE_LINE)
        line_key = displays[0].get_line_key()

    def test_read_display_toy(self):
        displays = dec8.make_displays(ONE_LINE)
        assert displays[0].read_display() == 5353

    def test_read_display_several(self):
        data = dec8.get_data(toy=True)
        displays = dec8.make_displays(data)
        assert sum(display.read_display() for display in displays) == 61229

    def test_read_display_real(self):
        data = dec8.get_data(toy=False)
        displays = dec8.make_displays(data)
        assert sum(display.read_display() for display in displays) == 1009098
