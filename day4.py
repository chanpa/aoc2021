from helper.utils import solver, parse_file_rows_to_list, group_on_empty_line
from copy import deepcopy


DAY = 4


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=" ")
    return group_on_empty_line(raw_data)


@solver
def part_a(boards):
    return bingo_game(boards)


@solver
def part_b(boards):
    return bingo_game(boards, num_winners=len(boards) - 1)


def bingo_game(boards, num_winners=1):
    draw_sequence = boards.pop(0)[0][0].split(",")
    reference_boards = _create_reference_boards(boards)
    winners = {}
    for drawn_number in draw_sequence:
        for board_number, board in boards.items():
            if board_number in winners:
                continue
            for row_index, row in enumerate(board):
                if drawn_number in row:
                    reference_boards[board_number][row_index][row.index(drawn_number)] = True
                    break  # numbers are unique
            else:
                # If drawn_number is not found we don't need to check this board
                # Reduces runtime to about 1/3 for me
                continue
            if _check_if_winner(reference_boards[board_number]):
                winners[board_number] = _calculate_score(
                    board, reference_boards[board_number], drawn_number
                )
                if len(winners) == num_winners:
                    return winners[board_number]


def _create_reference_boards(data):
    reference_boards = {}
    for group, board in data.items():
        reference_boards[group] = _create_board(len(board))
    return reference_boards


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
        reference_board,
        num
):
    depth = len(board_nums)
    unmarked_nums = [
        int(board_nums[i][j])
        for i in range(depth)
        for j in range(depth)
        if not reference_board[i][j]
    ]
    return sum(unmarked_nums) * int(num)


def main():
    data = prepare_data()
    part_a(deepcopy(data))
    part_b(deepcopy(data))


if __name__ == '__main__':
    main()
