from helper.utils import solver, parse_file_rows_to_list, group_on_empty_line


DAY = 4


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=" ")
    return group_on_empty_line(raw_data)


@solver
def part_a(boards_with_nums):
    boards_with_bools = _create_boards(boards_with_nums)
    for num in boards_with_nums[0][0][0].split(","):
        for group, board_nums in boards_with_nums.items():
            if group == 0:
                continue
            for i, row in enumerate(board_nums):
                if num in row:
                    j = row.index(num)
                    boards_with_bools[group][i][j] = True
            if _check_if_winner(boards_with_bools[group]):
                return _calculate_score(
                    group,
                    boards_with_nums,
                    boards_with_bools,
                    num
                )


@solver
def part_b(boards_with_nums):
    boards_with_bools = _create_boards(boards_with_nums)
    winners = {}
    for num in boards_with_nums[0][0][0].split(","):
        for group, board_nums in boards_with_nums.items():
            if group == 0 or group in winners:
                continue
            for i, row in enumerate(board_nums):
                if num in row:
                    boards_with_bools[group][i][row.index(num)] = True
            if _check_if_winner(boards_with_bools[group]):
                winners[group] = _calculate_score(
                    group,
                    boards_with_nums,
                    boards_with_bools,
                    num
                )
                if len(winners) == len(boards_with_bools):
                    return winners[group]


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
        winning_group,
        boards_with_nums,
        boards_with_bools,
        num
):
    depth = len(boards_with_bools[winning_group])
    unmarked_nums = [
        int(boards_with_nums[winning_group][i][j])
        for i in range(depth)
        for j in range(depth)
        if not boards_with_bools[winning_group][i][j]
    ]
    return sum(unmarked_nums) * int(num)


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

