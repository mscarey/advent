import csv


def get_data(day: int = 1, toy: bool = True) -> list[int]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        return [int(row[0]) for row in csv_reader]


def count_dives(data: list[int]) -> int:
    """Count times a value is followed by a higher value."""
    count = 0
    for before, after in zip(data[:-1], data[1:]):
        if before < after:
            count += 1
    return count


def window_dives(data: list[int]) -> int:
    """Count times the sum of a three-item sliding window increases from the previous sum."""
    count = 0
    for step in range(len(data) - 2):
        if sum(data[step : step + 3]) < sum(data[step + 1 : step + 4]):
            count += 1
    return count
