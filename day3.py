from helper.utils import time_function, parse_file_rows_to_list
from collections import defaultdict


DAY = 3


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return raw_data


@time_function
def part_a(data):
    freqs = determine_one_freqs(data)
    gamma = ""
    epsi = ""
    for pos in freqs:
        if freqs[pos] >= len(data)/2:
            gamma += "1"
            epsi += "0"
        else:
            gamma += "0"
            epsi += "1"
    return int(gamma, 2) * int(epsi, 2)


@time_function
def part_b(data):
    oxy = filter_by_bit(0, data)
    co2 = filter_by_bit(0, data, keep_most_common=False)
    return int(oxy, 2) * int(co2, 2)


def filter_by_bit(bit_pos, nums, keep_most_common=True):
    if len(nums) == 1:
        return nums[0]

    frequencies = determine_one_freqs(nums)
    most_common = "1" if frequencies[bit_pos] >= len(nums)/2 else "0"
    numbers_kept = []
    for num in nums:
        if keep_most_common and num[bit_pos] == most_common:
            numbers_kept.append(num)
        elif not keep_most_common and num[bit_pos] != most_common:
            numbers_kept.append(num)
    return filter_by_bit(bit_pos + 1, numbers_kept, keep_most_common=keep_most_common)


def determine_one_freqs(nums):
    frequencies = defaultdict(int)
    for i in range(len(nums[0])):
        for num in nums:
            if num[i] == "1":
                frequencies[i] += 1
    return frequencies


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

