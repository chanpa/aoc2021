from helper.utils import solver, parse_file_rows_to_list, list_str_to_list_number
from collections import Counter


DAY = 6


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=",")
    return list_str_to_list_number(raw_data[0])


@solver
def part_a(data):
    return simulate_fish(data)


@solver
def part_b(data):
    return simulate_fish(data, days=256)


def simulate_fish(all_fish, days=80):
    ages = Counter(all_fish)
    for day in range(days):
        new_births = ages[day % 7]
        ages[(day + 8) % 7] += new_births

    return sum(ages.values())


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

