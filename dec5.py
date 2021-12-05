import csv

from collections import Counter
from dataclasses import dataclass
from os import X_OK


def get_data(day: int = 5, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        lines = csv_file.readlines()
        rows = [row.strip("\n").split(" -> ") for row in lines]
        return [[item.split(",") for item in row] for row in rows]


@dataclass
class Point:
    x: int
    y: int

    def __str__(self) -> str:
        return f"{self.x},{self.y}"


@dataclass
class Line:
    start: Point
    end: Point

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def is_relevant(self) -> bool:
        """For first puzzle."""
        return self.is_horizontal() or self.is_vertical()

    def get_h_points(self) -> list[Point]:
        less = min(self.start.x, self.end.x)
        more = max(self.start.x, self.end.x)
        return [Point(h, self.start.y) for h in range(less, more + 1)]

    def get_v_points(self) -> list[Point]:
        less = min(self.start.y, self.end.y)
        more = max(self.start.y, self.end.y)
        return [Point(self.start.x, v) for v in range(less, more + 1)]

    def get_points(self) -> list[Point]:
        if self.is_horizontal():
            return self.get_h_points()
        elif self.is_vertical():
            return self.get_v_points()
        raise NotImplementedError


def count_overlap_points(list_of_lines: list[Line]) -> int:
    deep = Counter()
    for line in list_of_lines:
        for point in line.get_points():
            deep[str(point)] += 1
    total = 0
    for item in deep.most_common(10):
        if item[1] > 1:
            total += 1
        else:
            return total
    return total


def get_lines(data: list[list[int]]) -> list[list[int]]:
    lines = []
    for row in data:
        lines.append(
            Line(
                start=Point(x=int(row[0][0]), y=int(row[0][1])),
                end=Point(x=int(row[1][0]), y=int(row[1][1])),
            )
        )
    return lines


def get_relevant_lines(data: list[list[int]]) -> list[Line]:
    lines = get_lines(data)
    return [line for line in lines if line.is_relevant()]
