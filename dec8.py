import csv
from itertools import permutations
from dataclasses import dataclass
from typing import Dict, Iterator, OrderedDict


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

    def assign_easy_line(self) -> str:
        for digit in self.digits:
            if len(digit) == 2:
                right_side = digit
        for digit in self.digits:
            if len(digit) == 3:
                for line in digit:
                    if line not in right_side:
                        return line
        raise ValueError("No easy line found")

    @classmethod
    def read_decoded(cls, decoded_displays: list[str]) -> int:
        word = []
        for dd in decoded_displays:
            word.append(str(DISPLAY_MEANINGS.index(dd)))
        return int("".join(word))

    def get_guesses(self) -> Iterator[str]:
        first = self.assign_easy_line()
        others = [letter for letter in "abcdefg" if letter != first]
        for permutation in permutations(others):
            yield first + "".join(permutation)

    def encode_picture(self, picture: str, key: str) -> str:
        encoder = {letter: key[i] for i, letter in enumerate("abcdefg")}
        encoded = "".join(encoder[letter] for letter in picture)
        return "".join(sorted(encoded))

    def get_line_key(self) -> str:
        for guess in self.get_guesses():
            if all(
                self.encode_picture(picture=meaning, key=guess) in self.digits
                for meaning in DISPLAY_MEANINGS
            ):
                return guess

    def get_meaning_of_digit(self, digit: str, line_key: str) -> str:
        for meaning in DISPLAY_MEANINGS:
            if self.encode_picture(meaning, line_key) == digit:
                return meaning

    def decode_cypher(self) -> list[str]:
        line_key = self.get_line_key()
        answer = []
        for digit in self.cypher:
            answer.append(self.get_meaning_of_digit(digit=digit, line_key=line_key))
        return answer

    def read_display(self) -> int:
        digits = [DISPLAY_MEANINGS.index(digit) for digit in self.decode_cypher()]
        return int("".join([str(digit) for digit in digits]))


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
