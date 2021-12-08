from helper.utils import time_function, parse_file_rows_to_list


DAY = 8


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, test=True, split_line=" | ")
    return raw_data


@time_function
def part_a(data):
    answer = 0
    for _, output_values in data:
        for digit in output_values:
            if len(digit) in [2, 3, 4, 7]:
                answer += 1
    return answer


@time_function
def part_b(data):
    answer = data
    return answer


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

