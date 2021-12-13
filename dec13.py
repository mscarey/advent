import csv
from dataclasses import dataclass
from typing import NamedTuple


def get_data(day: int = 13, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        return [tuple(int(item) for item in row) for row in csv_reader]


class Point(NamedTuple):
    x: int
    y: int


@dataclass
class Paper:
    points: set[Point]

    def fold_left(self, x: int) -> None:
        new_points = set()
        for point in self.points:
            if point.x > x:
                new_points.add(Point(x=x - (point.x - x), y=point.y))
            else:
                new_points.add(point)
        self.points = new_points

    def fold_up(self, y: int) -> None:
        new_points = set()
        for point in self.points:
            if point.y > y:
                new_points.add(Point(x=point.x, y=y - (point.y - y)))
            else:
                new_points.add(point)
        self.points = new_points

    def get_code(self) -> int:
        """
        Follow instructions.

        fold along x=655
        fold along y=447
        fold along x=327
        fold along y=223
        fold along x=163
        fold along y=111
        fold along x=81
        fold along y=55
        fold along x=40
        fold along y=27
        fold along y=13
        fold along y=6
        """
        self.fold_left(x=655)
        self.fold_up(y=447)
        self.fold_left(x=327)
        self.fold_up(y=223)
        self.fold_left(x=163)
        self.fold_up(y=111)
        self.fold_left(x=81)
        self.fold_up(y=55)
        self.fold_left(x=40)
        self.fold_up(y=27)
        self.fold_up(y=13)
        self.fold_up(y=6)

    def __str__(self) -> str:
        result = ""
        for row in range(6):
            for col in range(40):
                if Point(x=col, y=row) in self.points:
                    result += "#"
                else:
                    result += "."
            result += "\n"
        return result


def get_paper(data: list[tuple[int, int]]) -> Paper:
    paper = Paper(points=set())
    for x, y in data:
        paper.points.add(Point(x, y))
    return paper
