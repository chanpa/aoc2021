from helper.utils import solver, parse_file_rows_to_list


DAY = 1


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, output_type=int)
    return raw_data


@solver
def part_a(data):
    return general_solution(data)


@solver
def part_b(data):
    return general_solution(data, chunk_size=3)


def general_solution(data, chunk_size=1):
    count = 0
    for i, num in enumerate(data):
        if i < chunk_size:
            continue
        if data[i] > data[i-chunk_size]:
            count += 1
    return count


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()
