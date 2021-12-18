import ast
import itertools
import math
from functools import reduce
from helper.utils import *


DAY = 18


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return [SnailNumber(ast.literal_eval(row)) for row in raw_data]


@time_function
def part_a(data):
    return reduce(SnailNumber.__add__, data).magnitude


@time_function
def part_b(data):
    return max((a + b).magnitude for a, b in itertools.permutations(data, 2))


class SnailNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, b):
        x = [self.num, b.num]
        while True:
            change, _, x, _ = SnailNumber.explode(x)
            if change:
                continue
            change, x = SnailNumber.split(x)
            if not change:
                break
        return SnailNumber(x)

    def __str__(self):
        return f"{self.num}"

    @property
    def magnitude(self):
        return SnailNumber._calc_magnitude(self.num)

    @staticmethod
    def _calc_magnitude(num):
        if isinstance(num, int):
            return num
        return 3 * SnailNumber._calc_magnitude(num[0]) + 2 * SnailNumber._calc_magnitude(num[1])

    @staticmethod
    def explode(num, n=4):
        if isinstance(num, int):
            return False, None, num, None
        if n == 0:
            return True, num[0], 0, num[1]
        a, b = num
        exp, left, a, right = SnailNumber.explode(a, n - 1)
        if exp:
            return True, left, [a, SnailNumber.add_left(b, right)], None
        exp, left, b, right = SnailNumber.explode(b, n - 1)
        if exp:
            return True, None, [SnailNumber.add_right(a, left), b], right
        return False, None, num, None

    @staticmethod
    def add_left(x, n):
        if n is None:
            return x
        if isinstance(x, int):
            return x + n
        return [SnailNumber.add_left(x[0], n), x[1]]

    @staticmethod
    def add_right(x, n):
        if n is None:
            return x
        if isinstance(x, int):
            return x + n
        return [x[0], SnailNumber.add_right(x[1], n)]

    @staticmethod
    def split(x):
        if isinstance(x, int):
            if x >= 10:
                return True, [x // 2, math.ceil(x / 2)]
            return False, x
        a, b = x
        change, a = SnailNumber.split(a)
        if change:
            return True, [a, b]
        change, b = SnailNumber.split(b)
        return change, [a, b]


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()
