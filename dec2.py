import csv


def get_data(day: int = 2, toy: bool = True) -> list[int]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        return [row[0] for row in csv_reader]


def navigate(data: list[str]) -> tuple[int, int]:
    x = 0
    y = 0
    for row in data:
        direction, distance = row.split(" ")
        if direction == "forward":
            x += int(distance)
        elif direction == "down":
            y += int(distance)
        elif direction == "up":
            y -= int(distance)
    return x, y


def get_answer(data: list[str]) -> int:
    x, y = navigate(data)
    return x * y


def aim(data: list[str]) -> tuple[int, int]:
    aim = 0
    x = 0
    y = 0
    for row in data:
        direction, distance = row.split(" ")
        if direction == "forward":
            x += int(distance)
            y += int(distance) * aim
        elif direction == "down":
            aim += int(distance)
        elif direction == "up":
            aim -= int(distance)
    return x, y


def get_aim_answer(data: list[str]) -> int:
    x, y = aim(data)
    return x * y
