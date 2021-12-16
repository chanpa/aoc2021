from collections import Counter

from helper.utils import *


DAY = 14


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=False)
    data = group_on_empty_line(raw_data)
    rules = {}
    for row in data[1]:
        pair, char = tuple(row.split(" -> "))
        rules[pair] = char
    return {
        "template": data[0][0],
        "rules": rules
    }


@time_function
def part_a(data):
    counts = _count_chars(_count_pairs(data, 10), data["template"][-1])
    return max(counts) - min(counts)


@time_function
def part_b(data):
    counts = _count_chars(_count_pairs(data, 40), data["template"][-1])
    return max(counts) - min(counts)


def _count_pairs(data, steps):
    template = data["template"]
    rules = data["rules"]
    pair_counter = Counter([template[i: i + 2] for i in range(len(template) - 1)])
    for _ in range(steps):
        new_count = defaultdict(int)
        for pair, count in pair_counter.items():
            new_count[pair[0] + rules[pair]] += count
            new_count[rules[pair] + pair[1]] += count
        pair_counter = new_count
    return pair_counter


def _count_chars(pairs, last_char_in_template):
    char_count = defaultdict(int)
    for pair, count in pairs.items():
        char_count[pair[0]] += count
    char_count[last_char_in_template] += 1
    return sorted(count for _, count in char_count.items())


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()
