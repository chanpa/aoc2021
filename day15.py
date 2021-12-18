from helper.utils import *


DAY = 15


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=False)
    return [[int(n) for n in row] for row in raw_data]


@time_function
def part_a(grid):
    start = (0, 0)
    end = len(grid) - 1, len(grid[0]) - 1
    path = dijkstra(
        grid,
        start,
        end
    )
    return path[-1].total_cost


@time_function
def part_b(grid):
    grid = _expand_grid_from_tile(grid, tiles=5)
    start = (0, 0)
    end = len(grid) - 1, len(grid[0]) - 1
    path = dijkstra(
        grid,
        start,
        end
    )
    return path[-1].total_cost


def _expand_grid_from_tile(tile, tiles):
    tile_width = len(tile)
    tile_height = len(tile[0])
    grid = tile

    for _ in range(tiles - 1):
        for row in grid:
            tail = row[-tile_width:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)

    for _ in range(tiles - 1):
        for row in grid[-tile_height:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            grid.append(row)

    return grid


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

