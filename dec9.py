import networkx as nx


def get_data(day: int = 9, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        lines = csv_file.readlines()
        rows = [row.strip("\n") for row in lines]
        return [[int(item) for item in row] for row in rows]


def check_for_low_point(data: list[list[int]], x: int, y: int) -> bool:
    item = data[y][x]

    return (
        (y == len(data) - 1 or data[y + 1][x] > item)
        and (y == 0 or data[y - 1][x] > item)
        and (x == len(data[y]) - 1 or data[y][x + 1] > item)
        and (x == 0 or data[y][x - 1] > item)
    )


def get_low_points(data: list[list[int]]) -> list[int]:
    low_points = []
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if check_for_low_point(data, x, y):
                low_points.append(item)

    return low_points


def get_risk_levels(data: list[list[int]]) -> list[int]:
    low_points = []
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if check_for_low_point(data, x, y):
                low_points.append(item)

    return [point + 1 for point in low_points]


def get_risk_sum(data: list[list[int]]) -> int:
    return sum(get_risk_levels(data))


def make_graph(data: list[list[int]]) -> nx.Graph:
    G = nx.Graph()
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if data[y][x] != 9:
                G.add_node((x, y))
    for y, row in enumerate(data[:-1]):
        for x, item in enumerate(row):
            if data[y][x] != 9 and data[y + 1][x] != 9:
                G.add_edge((x, y), (x, y + 1))
    for y, row in enumerate(data):
        for x, item in enumerate(row[:-1]):
            if data[y][x] != 9 and data[y][x + 1] != 9:
                G.add_edge((x, y), (x + 1, y))

    return G


def count_components(data: list[list[int]]) -> int:
    G = make_graph(data)
    return nx.number_connected_components(G)


def get_component_sizes(data: list[list[int]]) -> list[int]:
    G = make_graph(data)
    return [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]


def product_of_component_sizes(data: list[list[int]]) -> int:
    sizes = get_component_sizes(data)
    return sizes[0] * sizes[1] * sizes[2]
