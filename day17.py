from helper.utils import *
from collections import namedtuple
import re


DAY = 17
pattern = re.compile(r"-?\d+")
Area = namedtuple("Area", ["topleft", "botright"])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    

    def __repr__(self):
        return self.__str__()


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=False)
    xmin, xmax, ymin, ymax = list_str_to_list_number(pattern.findall(raw_data[0]))
    return Area(Point(xmin, ymax), Point(xmax, ymin))


@time_function
def part_a(data):
    return _get_highest_trajectory(data)


@time_function
def part_b(data):
    return _get_highest_trajectory(data, highest=False)


def _get_highest_trajectory(target, highest=True):
    xvel_min = _find_min_xvel(target.topleft.x)
    yvel_max = abs(target.botright.y) 
    heights = []
    for yvel in range(yvel_max, -yvel_max - 1, -1):
        for xvel in range(xvel_min, target.botright.x + 1, 1):
            height = _calc_trajectory(xvel, yvel, target)
            if height != None:
                heights.append(height)
    return max(heights) if highest else len(heights)


def _find_min_xvel(target_distance):
    for n in range(1, 1000):
        if (n * (n + 1)) / 2 > target_distance:
            return n


def _calc_trajectory(initial_xvel, initial_yvel, target):
    global found
    projectile = Point(0, 0)
    max_height = -100000000
    xvel, yvel = initial_xvel, initial_yvel
    # print(target)
    while projectile.x < target.botright.x and projectile.y > target.botright.y:
        projectile.x += xvel
        projectile.y += yvel
        # print(projectile)
        if projectile.y > max_height:
            max_height = projectile.y
        if (target.topleft.x <= projectile.x <= target.botright.x) \
            and (target.botright.y <= projectile.y <= target.topleft.y):
            return max_height
        yvel -= 1
        if xvel > 0:
            xvel -= 1
    return None


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == "__main__":
    data = prepare_data()
    part_a(data)
    part_b(data)
