import csv
from dataclasses import dataclass
from typing import OrderedDict


def get_data(day: int = 8, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        return [row for row in csv_reader]


DISPLAY_MEANINGS: list[str] = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


@dataclass
class Display:
    digits: list[str]
    cypher: list[str]

    def count_easy_digits(self) -> int:
        result = 0
        for cy in self.cypher:
            if len(cy) in (2, 3, 4, 7):
                result += 1
        return result

    def assign_easy_digits(self) -> dict[str, str]:
        blank = {letter: set("abcdefg") for letter in "abcdefg"}
        for cy in self.cypher:
            if len(cy) == 2:
                for letter in cy:
                    blank[letter] = blank[letter].intersection(set("cf"))
            elif len(cy) == 3:
                for letter in cy:
                    blank[letter] = blank[letter].intersection(set("acf"))
            elif len(cy) == 4:
                for letter in cy:
                    blank[letter] = blank[letter].intersection(set("bcdf"))
        return blank

    @classmethod
    def read_decoded(cls, decoded_displays: list[str]) -> int:
        word = []
        for dd in decoded_displays:
            word.append(str(DISPLAY_MEANINGS.index(dd)))
        return int("".join(word))


def make_displays(data: list[list[str]]) -> list[Display]:
    return [
        Display(
            digits=["".join(sorted(i)) for i in row[:10]],
            cypher=["".join(sorted(i)) for i in row[11:]],
        )
        for row in data
    ]


def count_all_easy_digits(data: list[Display]) -> int:
    result = 0
    for display in data:
        result += display.count_easy_digits()
    return result
