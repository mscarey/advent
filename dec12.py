from typing import Iterator, Optional

import networkx as nx


def get_data(day: int = 12, toy: bool = True, mega: bool = False) -> list[list[str]]:
    filename = f"data/{'toy' if toy else 'dec'}{'mega' if mega else ''}{int(day)}.csv"
    with open(filename) as csv_file:
        lines = csv_file.readlines()
        rows = [row.strip("\n") for row in lines]
        return [row.split("-") for row in rows]


def get_graph(data: list[list[str]]) -> nx.Graph:
    graph = nx.Graph()
    for row in data:
        graph.add_edge(row[0], row[1])
    return graph


def get_paths(
    graph: nx.Graph, start: str, end: str, current_path: Optional[list[str]] = None
) -> Iterator[list[str]]:
    current_path = current_path or [start]
    if start == end:
        yield current_path + [end]
    else:
        for neighbor in graph.adj[start].keys():
            if neighbor not in current_path or neighbor.upper() == neighbor:
                yield from get_paths(graph, neighbor, end, current_path + [neighbor])


def get_paths_revisit_small(
    graph: nx.Graph, start: str, end: str, current_path: Optional[list[str]] = None
) -> Iterator[list[str]]:
    current_path = current_path or [start]
    if start == end:
        yield current_path + [end]
    else:
        small_visited = [visited for visited in current_path if visited.islower()]
        for neighbor in graph.adj[start].keys():
            if (
                neighbor not in current_path
                or neighbor.upper() == neighbor
                or (
                    neighbor != "start"
                    and len(small_visited) == len(set(small_visited))
                )
            ):
                yield from get_paths_revisit_small(
                    graph, neighbor, end, current_path + [neighbor]
                )
