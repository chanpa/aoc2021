from copy import deepcopy

from helper.utils import *

DAY = 11


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=False)
    return {
        (x, y): int(energy)
        for x, rows in enumerate(raw_data)
        for y, energy in enumerate(rows)
    }


@time_function
def part_a(data):
    return _sim_steps(data, 100)


@time_function
def part_b(data):
    return _sim_steps(data, 1_000_000, sync=True)


def neighbours(x, y, energy_levels):
    kernel = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    return filter(
        energy_levels.get,
        [(x + dx, y + dy) for dx, dy in kernel]
    )


def _sim_steps(energy_levels, steps, sync=False):
    flashes = 0
    for step in range(1, steps + 1):
        for position in energy_levels:
            energy_levels[position] += 1

        flashing = set(position for position in energy_levels if energy_levels[position] > 9)
        while flashing:
            position = flashing.pop()
            energy_levels[position] = 0
            flashes += 1
            for n in neighbours(*position, energy_levels):
                energy_levels[n] += 1
                if energy_levels[n] > 9:
                    flashing.add(n)

        if sync and sum(energy_levels.values()) == 0:
            return step
    return flashes


def main():
    data = prepare_data()
    part_a(deepcopy(data))
    part_b(deepcopy(data))


if __name__ == '__main__':
    main()

