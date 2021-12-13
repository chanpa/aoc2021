from collections import deque

from helper.utils import time_function, parse_file_rows_to_list


DAY = 10


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=True)
    return raw_data


@time_function
def part_a(data):
    answer = data
    return answer


@time_function
def part_b(data):
    answer = data
    return answer


OPENERS = set("([{<")
CLOSERS = set(")]}>")


def _char_queue(chars):
    stack = deque()
    for ch in chars:
        if ch in OPENERS:
            stack.append(ch)
        else:



def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

