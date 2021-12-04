from typing import Optional, Tuple

import csv


def get_data(day: int = 4, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        return [[int(item) for item in row] for row in csv_reader]


class Board:
    def __init__(self, rows: list[list[int]]):
        self.rows = rows
        self.called = [[False for x in range(5)] for y in range(5)]

    def hear_call(self, call: int) -> None:
        for y in range(5):
            for x in range(5):
                if self.rows[y][x] == call:
                    self.called[y][x] = True

    def check_for_h_win(self) -> bool:
        for y in range(5):
            if all(self.called[y]):
                return True
        return False

    def check_for_v_win(self) -> bool:
        for x in range(5):
            if all(self.called[y][x] for y in range(5)):
                return True
        return False

    def check_for_win(self) -> bool:
        if self.check_for_h_win():
            return True
        if self.check_for_v_win():
            return True
        return False

    def unmarked_score(self) -> int:
        result = 0
        for y in range(5):
            for x in range(5):
                if not self.called[y][x]:
                    result += self.rows[y][x]
        return result


def get_boards(data: list[list[int]]) -> list[Board]:
    boards = []
    for group in range((len(data) + 1) // 6):
        boards.append(Board(rows=data[6 * group : 6 * group + 5]))
    return boards


class BoardSet:
    def __init__(self, boards: list[Board]):
        self.boards = boards

    def hear_call(self, call: int) -> None:
        for board in self.boards:
            board.hear_call(call)

    def check_for_win(self) -> Optional[int]:
        for i, board in enumerate(self.boards):
            if board.check_for_win():
                return i
        return None

    def find_score(self, calls: list[int]) -> tuple[int, int]:
        for call in calls:
            self.hear_call(call)
            winner = self.check_for_win()
            if winner is not None:
                return call, self.boards[winner].unmarked_score()

    def find_answer(self, calls: list[int]) -> int:
        last_called, unmarked_points = self.find_score(calls)
        return last_called * unmarked_points


def make_toy_boards() -> BoardSet:
    return BoardSet(boards=get_boards(get_data(toy=True)))


def make_real_boards() -> BoardSet:
    return BoardSet(boards=get_boards(get_data(toy=False)))


toy_calls = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]

real_calls = [
    57,
    9,
    8,
    30,
    40,
    62,
    24,
    70,
    54,
    73,
    12,
    3,
    71,
    95,
    58,
    88,
    23,
    81,
    53,
    80,
    22,
    45,
    98,
    37,
    18,
    72,
    14,
    20,
    66,
    0,
    19,
    31,
    82,
    34,
    55,
    29,
    27,
    96,
    48,
    28,
    87,
    83,
    36,
    26,
    63,
    21,
    5,
    46,
    33,
    86,
    32,
    56,
    6,
    38,
    52,
    16,
    41,
    74,
    99,
    77,
    13,
    35,
    65,
    4,
    78,
    91,
    90,
    43,
    1,
    2,
    64,
    60,
    94,
    85,
    61,
    84,
    42,
    76,
    68,
    10,
    49,
    89,
    11,
    17,
    79,
    69,
    39,
    50,
    25,
    51,
    47,
    93,
    44,
    92,
    59,
    75,
    7,
    97,
    67,
    15,
]
