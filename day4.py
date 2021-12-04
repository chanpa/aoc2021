from helper.utils import solver, parse_file_rows_to_list, group_on_empty_line
from copy import deepcopy

DAY = 4


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=" ")
    return group_on_empty_line(raw_data)


@solver
def part_a(boards_with_nums):
    return bingo_game(boards_with_nums)


@solver
def part_b(boards_with_nums):
    return bingo_game(boards_with_nums, num_winners=len(boards_with_nums) - 1)


def bingo_game(boards_with_nums, num_winners=1):
    draw_sequence = boards_with_nums.pop(0)[0][0].split(",")
    boards_with_bools = _create_boards(boards_with_nums)
    winners = {}
    for drawn_number in draw_sequence:
        for board_number, board in boards_with_nums.items():
            if board_number in winners:
                continue
            for i, row in enumerate(board):
                if drawn_number in row:
                    boards_with_bools[board_number][i][row.index(drawn_number)] = True
                    break  # numbers are unique
            if _check_if_winner(boards_with_bools[board_number]):
                winners[board_number] = _calculate_score(
                    board, boards_with_bools[board_number], drawn_number
                )
                if len(winners) == num_winners:
                    return winners[board_number]


def _create_boards(data):
    marking_boards = {}
    for group, board in data.items():
        if group == 0:
            continue
        marking_boards[group] = _create_board(len(board))
    return marking_boards


def _create_board(depth):
    return [
        [False] * depth
        for _ in range(depth)
    ]


def _check_if_winner(board):
    for i in range(len(board)):
        if sum(board[i]) == len(board):
            return True
        if sum([row[i] for row in board]) == len(board):
            return True
    return None


def _calculate_score(
        board_nums,
        board_bools,
        num
):
    depth = len(board_nums)
    unmarked_nums = [
        int(board_nums[i][j])
        for i in range(depth)
        for j in range(depth)
        if not board_bools[i][j]
    ]
    return sum(unmarked_nums) * int(num)


def main():
    data = prepare_data()
    part_a(deepcopy(data))
    part_b(deepcopy(data))


if __name__ == '__main__':
    main()
