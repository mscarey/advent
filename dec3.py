import csv
from copy import copy


def get_data(day: int = 3, toy: bool = True) -> list[str]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        return [row[0] for row in csv_reader]


def totals(data: list[str]) -> list[int]:
    return [sum(row[i] == "1" for row in data) for i in range(len(data[0]))]


def common_digits(data: list[str]) -> str:
    answer = totals(data)
    return ["1" if t >= len(data) / 2 else "0" for t in answer]


def uncommon_digits(data: list[str]) -> str:
    answer = totals(data)
    return ["0" if t >= len(data) / 2 else "1" for t in answer]


def gamma(data: list[str]) -> str:
    answer = common_digits(data)
    return int("".join(answer), 2)


def epsilon(data: list[str]) -> str:
    answer = uncommon_digits(data)
    return int("".join(answer), 2)


def answer(data: list[str]) -> str:
    return epsilon(data) * gamma(data)


def oxygen(data: list[str]) -> int:
    for i in range(len(copy(data[0]))):
        total = sum(row[i] == "1" for row in data)
        common = "1" if total >= len(data) / 2 else "0"
        data = [row for row in data if row[i] == common]
        if len(data) == 1:
            return int(data[0], 2)
    return -1


def co2(data: list[str]) -> int:
    for i in range(len(copy(data[0]))):
        total = sum(row[i] == "1" for row in data)
        uncommon = "0" if total >= len(data) / 2 else "1"
        data = [row for row in data if row[i] == uncommon]
        if len(data) == 1:
            return int(data[0], 2)
    return -1


def life_support(data: list[str]) -> int:
    return oxygen(data) * co2(data)
