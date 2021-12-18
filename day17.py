from helper.utils import *
from collections import namedtuple
import re


DAY = 17
pattern = re.compile(r"-?\d+")
Area = namedtuple("Area", ["topleft", "botright"])


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=False)
    xmin, xmax, ymin, ymax = list_str_to_list_number(pattern.findall(raw_data[0]))
    return Area(Point(xmin, ymax), Point(xmax, ymin))


@time_function
def part_a(data):
    return _calc_all_hitting_trajectories(data, get_highest=True)


@time_function
def part_b(data):
    return len(_calc_all_hitting_trajectories(data))


def _calc_all_hitting_trajectories(target, get_highest=False):
    xvel_max = target.botright.x
    xvel_min = _find_min_xvel(target.topleft.x)
    yvel_max = abs(target.botright.y) - 1
    yvel_min = -yvel_max - 1
    heights = []
    for yvel in range(yvel_max, yvel_min - 1, -1):
        for xvel in range(xvel_min, xvel_max + 1, 1):
            velocity = Point(xvel, yvel)
            height = _calc_trajectory(velocity, target)
            if height is not None:
                if get_highest:
                    return height
                heights.append(height)
    return heights


def _find_min_xvel(target_distance):
    for n in range(1, target_distance):
        if gauss_sum(n) > target_distance:
            return n


def _calc_trajectory(velocity, target):
    projectile = Point(0, 0)
    max_height = gauss_sum(velocity.y)
    while projectile.x < target.botright.x and projectile.y > target.botright.y:
        projectile += velocity
        if (target.topleft.x <= projectile.x <= target.botright.x)\
                and (target.botright.y <= projectile.y <= target.topleft.y):
            return max_height
        velocity.y -= 1
        if velocity.x > 0:
            velocity.x -= 1
    return None


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"p({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == "__main__":
    main()
