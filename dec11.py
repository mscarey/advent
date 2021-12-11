def get_data(day: int = 11, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        lines = csv_file.readlines()
        rows = [row.strip("\n") for row in lines]
        return [[int(x) for x in row] for row in rows]


def flash(data: list[list[int]], x: int, y: int) -> list[list[int]]:
    new_data = [[item for item in row] for row in data]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                new_data[y][x] = 11
                continue
            try:
                new_data[y + i][x + j] = min(11, new_data[y + i][x + j] + 1)
            except IndexError:
                pass
    return new_data


def step(data: list[list[int]]) -> list[list[int]]:
    new_data = [[item + 1 for item in row] for row in data]
    total_flashes = 0
    new_flashes = 1
    while new_flashes > 0:
        new_flashes = 0
        for y, row in enumerate(new_data):
            for x, item in enumerate(row):
                if item == 10:
                    new_data = flash(new_data, x, y)
                    new_flashes += 1
        total_flashes += new_flashes
    for y, row in enumerate(new_data):
        for x, item in enumerate(row):
            if item == 11:
                new_data[y][x] = 0
    return new_data, total_flashes


def multiple_steps(data: list[list[int]], steps: int) -> list[list[int]]:
    total_flashes = 0
    for _ in range(steps):
        data, new_flashes = step(data)
        total_flashes += new_flashes
    return data, total_flashes
