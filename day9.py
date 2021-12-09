from helper.utils import *
from math import prod


DAY = 9


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return [[int(ch) for ch in row] for row in raw_data]


@time_function
def part_a(data):
    kernel = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return _calc_total_risk_level(data, kernel)


@time_function
def part_b(data):
    kernel = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return prod(_map_all_basins(data, kernel)[-3:])


def _calc_total_risk_level(data, kernel):
    low_points = _find_low_points(data, kernel)
    return sum(data[x][y] + 1 for x, y in low_points)


def _find_low_points(data, kernel):
    return [
        (i, j)
        for i in range(len(data))
        for j in range(len(data[0]))
        if _is_low_point((i, j), kernel, data)
    ]


def _is_low_point(position, kernel, data):
    for neighbour in neighbours(position, kernel):
        nx, ny = neighbour
        if nx < 0 or ny < 0:
            continue
        try:
            x, y = position
            if data[x][y] >= data[nx][ny]:
                return False
        except IndexError:
            pass  # IndexError means we are at the edge and it's trying to check outside the bounds
    return True


def _map_all_basins(data, kernel):
    low_points = _find_low_points(data, kernel)
    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(_get_basin_size(low_point, data, kernel))
    return sorted(basin_sizes)


def _get_basin_size(low_point, data, kernel):
    queue = [low_point]
    visited = set()
    while queue:
        point = queue.pop(0)
        for n in neighbours(point, kernel):
            nx, ny = n
            try:
                if nx < 0 or ny < 0 or n in visited or data[nx][ny] == 9:
                    continue
            except IndexError:
                continue
            visited.add(n)
            queue.append(n)
    return len(visited)


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()
