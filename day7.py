from helper.utils import *


DAY = 7


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=",")
    return list_str_to_list_number(raw_data[0])


@solver
def part_a(data):
    return _calc_fuel_consumption(data)


@solver
def part_b(data):
    return _calc_fuel_consumption(data, gaussian_sum=True)


def _calc_fuel_consumption(positions, gaussian_sum=False):
    gather_at = _calc_median(positions) if not gaussian_sum else int(sum(positions) / len(positions))
    total_consumption = 0
    for depth in positions:
        steps = abs(depth - gather_at)
        if gaussian_sum:
            total_consumption += steps * (steps + 1) / 2
        else:
            total_consumption += steps
    return int(total_consumption)


def _calc_median(data: List[int]) -> int:
    data = sorted(data)
    data_len = len(data)
    data_middle_index = data_len // 2
    if data_len % 2 != 0:
        return data[data_middle_index]
    return (data[data_middle_index] + data[data_middle_index - 1]) // 2


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

