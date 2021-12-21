import re
from helper.utils import *
from functools import cache


DAY = 21
pattern = re.compile(r"\d+$")


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=False)
    return [int(pattern.findall(line)[0]) for line in raw_data]


@time_function
def part_a(data):
    game_outcome = _dirac_dice(data[0], data[1])
    return min(game_outcome[0]) * game_outcome[1]


@time_function
def part_b(data):
    game_outcome = _quantum_wins(
        data[0],
        data[1],
        0,
        0
    )
    return max(game_outcome)


def _dirac_dice(p1_pos, p2_pos, winning_score=1000):
    p1_score = p2_score = turn = 0
    while p1_score < winning_score and p2_score < winning_score:
        turn += 1
        turn_dice = _deterministic_dice((turn - 1) * 3)
        if turn % 2 == 0:
            p2_pos = (p2_pos + turn_dice) % 10 or 10
            p2_score += p2_pos
        else:
            p1_pos = (p1_pos + turn_dice) % 10 or 10
            p1_score += p1_pos
    return (p1_score, p2_score), turn * 3


@cache
def _quantum_wins(p1_pos, p2_pos, s1, s2, sides=3, max_score=21):
    if s1 >= max_score:
        return 1, 0
    if s2 >= max_score:
        return 0, 1

    die_results = list(range(1, sides + 1))
    answer = (0, 0)
    for d1 in die_results:
        for d2 in die_results:
            for d3 in die_results:
                new_p1 = (p1_pos + d1 + d2 + d3) % 10 or 10
                new_s1 = s1 + new_p1
                x1, y1 = _quantum_wins(p2_pos, new_p1, s2, new_s1)
                answer = (answer[0] + y1, answer[1] + x1)
    return answer


def _deterministic_dice(previous_rolls, num_rolls=3, sides=100):
    total = 0
    for roll in range(previous_rolls + 1, previous_rolls + num_rolls + 1, 1):
        total += roll % sides or 100
    return total


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

