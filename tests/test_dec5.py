import dec5
from collections import Counter


class TestDec5:
    def test_data(self):
        data = dec5.get_data(toy=True)
        assert data[0][0] == ["0", "9"]

    def test_get_lines(self):
        data = dec5.get_data(toy=True)
        lines = dec5.get_lines(data)
        assert lines[0].start == dec5.Point(x=0, y=9)

    def test_is_horizontal(self):
        data = dec5.get_data(toy=True)
        lines = dec5.get_lines(data)
        assert lines[2].is_horizontal()

    def test_point_from_line(self):
        data = dec5.get_data(toy=True)
        lines = dec5.get_lines(data)
        points = lines[0].get_points()
        assert points == [
            dec5.Point(x=0, y=9),
            dec5.Point(x=1, y=9),
            dec5.Point(x=2, y=9),
            dec5.Point(x=3, y=9),
            dec5.Point(x=4, y=9),
            dec5.Point(x=5, y=9),
        ]

    def test_get_relevant(self):
        data = dec5.get_data(toy=True)
        lines = dec5.get_lines(data)
        relevant = [line for line in lines if line.is_relevant()]
        assert len(relevant) == 6

    def test_get_relevant(self):
        data = dec5.get_data(toy=True)
        relevant = dec5.get_relevant_lines(data)
        assert len(relevant) == 6

    def test_count_overlap_points(self):
        data = dec5.get_data(toy=True)
        relevant = dec5.get_relevant_lines(data)
        overlap_count = dec5.count_overlap_points(relevant)
        assert overlap_count == 5
