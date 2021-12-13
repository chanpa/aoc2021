from collections import deque, Counter, defaultdict

from helper.utils import time_function, parse_file_rows_to_list


DAY = 10
OPENERS = set("([{<")
CLOSERS = set(")]}>")


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return raw_data


@time_function
def part_a(data):
    return _calc_points_a(Counter([_char_stack(row) for row in data]))


@time_function
def part_b(data):
    chars = set(_char_stack(row) for row in data) - CLOSERS
    return _calc_answer_b(chars)


def _char_stack(chars):
    stack = deque()
    for ch in chars:
        if ch in OPENERS:
            stack.append(ch)
        else:
            prev = stack.pop()
            match abs(ord(ch) - ord(prev)) > 2:
                case False:
                    continue
                case True:
                    return ch
    return _finish_incomplete_line(stack)


def _finish_incomplete_line(stack):
    completion_string = ""
    for ch in reversed(stack):
        if ch == "(":
            completion_string += chr(ord(ch) + 1)
        else:
            completion_string += chr(ord(ch) + 2)
    return completion_string


def _calc_points_a(counter):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    return sum(counter[sign] * value for sign, value in points.items())


def _calc_answer_b(lines):
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    scores = []
    for line in lines:
        score = 0
        for ch in line:
            score *= 5
            score += points[ch]
        scores.append(score)
    return sorted(scores)[len(scores) // 2]


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

