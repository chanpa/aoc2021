from helper.utils import solver, parse_file_rows_to_list, list_str_to_list_number
from collections import defaultdict


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


def simulate_fish(all_fish_ages, days=80):
    ages = defaultdict(lambda: [0, 0])
    for fish in all_fish_ages:
        ages[fish] = [ages[fish][0] + 1, 0]

    for day in range(days):
        birthday_group = day % 7
        new_fish_delivery_day = (day + 9) % 7

        adult_fish = ages[birthday_group][0]
        ages[birthday_group][0] = adult_fish + ages[birthday_group][1]
        ages[birthday_group][1] = 0

        ages[new_fish_delivery_day][1] += adult_fish
    return sum([group[0] + group[1] for group in ages.values()])


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

