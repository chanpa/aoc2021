import numpy as np
import sys
from heapq import heappush, heappop
from time import perf_counter_ns
from typing import List, Any
from locale import atof, atoi, setlocale, LC_NUMERIC
from collections import defaultdict
from pathlib import Path
from math import inf


setlocale(LC_NUMERIC, "en_US.UTF-8")
NS_TO_MILLI = 1_000_000
NS_TO_MICRO = 1_000
NEIGHBOUR_KERNELS = {
    "diagonal": [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
    "default": [(0, 1), (0, -1), (1, 0), (-1, 0)]
}


def time_function(fn):
    def wrap(*args, **kwargs):
        start = perf_counter_ns()
        res = fn(*args, **kwargs)
        elapsed_time = perf_counter_ns() - start
        print(f"{fn.__name__}:")
        if "part" in fn.__name__:
            print(f"Answer is: {res}")
        print(f"Took: {(elapsed_time / NS_TO_MICRO):_.3f} µs\n")
        return res

    return wrap


def parse_file_rows_to_list(day: int, test=False, split_row_on=None) -> List:
    if test:
        filename = f"{Path(__file__).parents[1].resolve()}/inputs_test/{day}.data"
    else:
        filename = f"{Path(__file__).parents[1].resolve()}/inputs/{day}.data"
    rows = []
    with open(filename) as f:
        for row in f:
            row = row.strip()
            if split_row_on:
                row = [e.strip() for e in row.split(split_row_on) if e]
            rows.append(row)
    return rows


def list_str_to_list_number(data, out_type=int):
    new_data = []
    for element in data:
        if out_type == int:
            num = atoi(element)
        else:
            num = atof(element)
        new_data.append(num)
    return new_data


def group_on_empty_line(rows: List[str]) -> defaultdict[Any, List]:
    groups = defaultdict(list)
    group = 0
    for e in rows:
        if not e:
            group += 1
            continue
        groups[group].append(e)
    return groups


def liststr_to_listlist(group: List[str]) -> List[List]:
    new_vals = []
    for value in group:
        if not type(value) == str:
            print(f"Encountered {value} that is not a str")
            sys.exit(1)
        new_vals.append(list(value))
    return new_vals


def neighbours_dict(point, values, diagonal=False):
    x, y = point
    return filter(
        values.get,
        [(x + dx, y + dy) for dx, dy in _get_kernel(diagonal)]
    )


def neighbours_grid(point, xmax, ymax, diagonal=False):
    x, y = point
    return [
        (x + dx, y + dy)
        for dx, dy in _get_kernel(diagonal)
        if 0 <= (x + dx) <= xmax and 0 <= (y + dy) <= ymax
    ]


def get_list_depth(lst):
    if isinstance(lst, list):
        return 1 + max(get_list_depth(element) for element in lst)
    else:
        return 0


class Node:
    def __init__(self, pos=None, parent=None, weight=None):
        self.parent = parent
        self.pos = pos
        self.weight = weight
        self.total_cost = inf
        self.visited = False

    def __eq__(self, other):
        print("e")
        return self.pos == other.pos

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __str__(self):
        return f"N{self.pos} r={self.weight} tr={self.total_cost}"

    def __repr__(self):
        return self.__str__()


def dijkstra(grid, start, end):
    nodes = _create_nodes(grid, start)
    queue = [nodes[start[0]][start[1]]]

    i_count = 0
    while queue:
        i_count += 1
        node = heappop(queue)
        if node.pos == end:
            print(f"Iterations: {i_count}")
            return _build_path(node)

        if node.visited:
            continue

        node.visited = True
        for n_pos in neighbours_grid(node.pos, len(grid) - 1, len(grid[0]) - 1):
            nx, ny = n_pos
            n_node = nodes[ny][nx]
            total_risk = node.total_cost + nodes[nx][ny].weight

            if total_risk < n_node.total_cost:
                n_node.total_cost = total_risk
                n_node.parent = node
                heappush(queue, n_node)
    return []


def astar(grid, start, end, blocked_values=None):
    nodes = _create_nodes(grid, start)
    grid_dimensions = len(grid), len(grid[0])
    heap = [(0, start)]
    max_x, max_y = grid_dimensions

    i_count = 0
    while heap and np.isinf(nodes[end[0]][end[1]].total_cost):
        i_count += 1
        _, (x, y) = heappop(heap)
        node = nodes[x][y]
        if node.visited:
            continue

        node.visited = True
        for nx, ny in neighbours_grid((x, y), max_x - 1, max_y - 1):
            n_node = nodes[nx][ny]
            if blocked_values and n_node.weight in blocked_values:
                continue
            new_total = node.total_cost + n_node.weight
            if new_total < n_node.total_cost:
                n_node.total_cost = new_total
                n_node.parent = node
                heappush(heap, (new_total, (nx, ny)))
    print(f"Iterations: {i_count}")
    return _build_path(nodes[end[0]][end[1]])


def _create_nodes(grid, start) -> List[List[Node]]:
    nodes = []
    for y, row in enumerate(grid):
        nodes.append([])
        for x, risk in enumerate(row):
            n = Node((x, y), weight=risk)
            if x == start[0] and y == start[1]:
                n.total_cost = 0
            nodes[y].append(n)
    return nodes


def _build_path(node):
    path = []
    while node is not None:
        path.append(node)
        node = node.parent
    return path[::-1]


def gauss_sum(n):
    return n * (n + 1) // 2


def _get_kernel(diagonal=False):
    if diagonal:
        return NEIGHBOUR_KERNELS["diagonal"]
    return NEIGHBOUR_KERNELS["default"]
