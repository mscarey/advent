import dec13


class TestDec13(object):
    def test_get_data(self):
        assert dec13.get_data()[0] == (6, 10)

    def test_get_paper_toy(self):
        data = dec13.get_data()
        paper = dec13.get_paper(data)
        assert dec13.Point(x=6, y=10) in paper.points

    def test_fold_paper_toy(self):
        data = dec13.get_data()
        paper = dec13.get_paper(data)
        assert len(paper.points) == 18
        paper.fold_up(y=7)
        assert len(paper.points) == 17

    def test_fold_paper_real(self):
        data = dec13.get_data(toy=False)
        paper = dec13.get_paper(data)
        assert len(paper.points) == 953
        paper.fold_left(x=655)
        assert len(paper.points) == 802

    def test_get_answer_real(self):
        data = dec13.get_data(toy=False)
        paper = dec13.get_paper(data)
        paper.get_code()
        assert str(paper).startswith("#")
