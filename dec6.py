import csv

from collections import Counter


def get_data(day: int = 6, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        return [[int(item) for item in row] for row in csv_reader]


toy = [3, 4, 3, 1, 2]


def grow(fish: list[int], days: int = 0) -> list[int]:
    for day in range(days):
        fish = [x - 1 for x in fish]
        fish.extend([8] * fish.count(-1))
        fish = [6 if x == -1 else x for x in fish]
    return fish


def efficient_grow(fish: list[int], days: int = 0) -> list[int]:
    counter = Counter(fish)
    for day in range(days):
        new_counter = Counter({k - 1: v for k, v in counter.items()})
        new_counter[8] = counter[0]
        new_counter[6] += counter[0]
        new_counter.pop(-1, None)
        counter = new_counter
    return counter


REAL_FISH = [
    3,
    5,
    1,
    5,
    3,
    2,
    1,
    3,
    4,
    2,
    5,
    1,
    3,
    3,
    2,
    5,
    1,
    3,
    1,
    5,
    5,
    1,
    1,
    1,
    2,
    4,
    1,
    4,
    5,
    2,
    1,
    2,
    4,
    3,
    1,
    2,
    3,
    4,
    3,
    4,
    4,
    5,
    1,
    1,
    1,
    1,
    5,
    5,
    3,
    4,
    4,
    4,
    5,
    3,
    4,
    1,
    4,
    3,
    3,
    2,
    1,
    1,
    3,
    3,
    3,
    2,
    1,
    3,
    5,
    2,
    3,
    4,
    2,
    5,
    4,
    5,
    4,
    4,
    2,
    2,
    3,
    3,
    3,
    3,
    5,
    4,
    2,
    3,
    1,
    2,
    1,
    1,
    2,
    2,
    5,
    1,
    1,
    4,
    1,
    5,
    3,
    2,
    1,
    4,
    1,
    5,
    1,
    4,
    5,
    2,
    1,
    1,
    1,
    4,
    5,
    4,
    2,
    4,
    5,
    4,
    2,
    4,
    4,
    1,
    1,
    2,
    2,
    1,
    1,
    2,
    3,
    3,
    2,
    5,
    2,
    1,
    1,
    2,
    1,
    1,
    1,
    3,
    2,
    3,
    1,
    5,
    4,
    5,
    3,
    3,
    2,
    1,
    1,
    1,
    3,
    5,
    1,
    1,
    4,
    4,
    5,
    4,
    3,
    3,
    3,
    3,
    2,
    4,
    5,
    2,
    1,
    1,
    1,
    4,
    2,
    4,
    2,
    2,
    5,
    5,
    5,
    4,
    1,
    1,
    5,
    1,
    5,
    2,
    1,
    3,
    3,
    2,
    5,
    2,
    1,
    2,
    4,
    3,
    3,
    1,
    5,
    4,
    1,
    1,
    1,
    4,
    2,
    5,
    5,
    4,
    4,
    3,
    4,
    3,
    1,
    5,
    5,
    2,
    5,
    4,
    2,
    3,
    4,
    1,
    1,
    4,
    4,
    3,
    4,
    1,
    3,
    4,
    1,
    1,
    4,
    3,
    2,
    2,
    5,
    3,
    1,
    4,
    4,
    4,
    1,
    3,
    4,
    3,
    1,
    5,
    3,
    3,
    5,
    5,
    4,
    4,
    1,
    2,
    4,
    2,
    2,
    3,
    1,
    1,
    4,
    5,
    3,
    1,
    1,
    1,
    1,
    3,
    5,
    4,
    1,
    1,
    2,
    1,
    1,
    2,
    1,
    2,
    3,
    1,
    1,
    3,
    2,
    2,
    5,
    5,
    1,
    5,
    5,
    1,
    4,
    4,
    3,
    5,
    4,
    4,
]
