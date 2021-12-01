from helper.utils import solver, parse_file_rows_to_list


DAY = 6


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, output_type=str)
    return raw_data


@solver
def part_a(data):
    answer = data
    return answer


@solver
def part_b(data):
    answer = data
    return answer


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

