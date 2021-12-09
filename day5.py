from collections import defaultdict

from helper.utils import time_function, parse_file_rows_to_list


DAY = 5


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=" -> ")
    data = []
    for row in raw_data:
        x1, y1 = row[0].split(",")
        x2, y2 = row[1].split(",")
        data.append([(int(x1), int(y1)), (int(x2), int(y2))])
    return data


@time_function
def part_a(data):
    board = _draw_lines(data)
    return sum(1 for pts in board.values() if pts > 1)


@time_function
def part_b(data):
    board = _draw_lines(data, diagonals=True)
    return sum(1 for pts in board.values() if pts > 1)


def _draw_lines(lines, diagonals=False):
    board = defaultdict(int)
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 == x2:
            for delta in range(abs(y1 - y2) + 1):
                board[(x1, min(y1, y2) + delta)] += 1
        elif y1 == y2:
            for delta in range(abs(x1 - x2) + 1):
                board[(min(x1, x2) + delta, y1)] += 1
        elif diagonals:
            _draw_diagonals((x1, y1), (x2, y2), board)
    return board


def _draw_diagonals(p1, p2, board):
    x1, y1 = p1
    x2, y2 = p2
    if x1 - x2 == y1 - y2:
        for delta in range(abs(x1 - x2) + 1):
            board[min(x1, x2) + delta, min(y1, y2) + delta] += 1
    else:
        for delta in range(abs(x1 - x2) + 1):
            board[min(x1, x2) + delta, max(y1, y2) - delta] += 1


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

