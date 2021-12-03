from helper.utils import solver, parse_file_rows_to_list
from collections import defaultdict


DAY = 3


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return raw_data


@solver
def part_a(data):
    freqs = determine_one_freqs(data)
    gamma = ""
    epsi = ""
    for pos in freqs:
        if freqs[pos] >= len(data)//2:
            gamma += "1"
            epsi += "0"
        else:
            gamma += "0"
            epsi += "1"
    return int(gamma, 2) * int(epsi, 2)


@solver
def part_b(data):
    oxy = filter_by_bit(0, data)
    co2 = filter_by_bit(0, data, most=False)
    return int(oxy, 2) * int(co2, 2)


def filter_by_bit(bit_pos, nums, most=True):
    if len(nums) == 1:
        return nums[0]

    freqs = determine_one_freqs(nums)
    most_common = "1" if freqs[bit_pos] >= len(nums)/2 else "0"
    keep = []
    for num in nums:
        if most:
            if num[bit_pos] == most_common:
                keep.append(num)
        else:
            if num[bit_pos] != most_common:
                keep.append(num)
    return filter_by_bit(bit_pos + 1, keep, most=most)


def determine_one_freqs(nums):
    freqs = defaultdict(int)
    for i in range(len(nums[0])):
        for num in nums:
            if num[i] == "1":
                freqs[i] += 1
    return freqs


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

