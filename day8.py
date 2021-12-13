from helper.utils import time_function, parse_file_rows_to_list


DAY = 8


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=" | ")
    return [(row[0].split(" "), row[1].split(" ")) for row in raw_data]


@time_function
def part_a(data):
    answer = 0
    print(data)
    for _, output_values in data:
        for digit in output_values:
            if len(digit) in [2, 3, 4, 7]:
                answer += 1
    return answer


@time_function
def part_b(data):
    answer = 0
    for input_digits, output_digits in data:
        lengths = {len(digit): set(digit) for digit in input_digits}
        output = ""
        for digit in map(set, output_digits):
            match len(digit), len(digit&lengths[4]), len(digit&lengths[2]):
                case 2, _, _: output += "1"
                case 3, _, _: output += "7"
                case 4, _, _: output += "4"
                case 7, _, _: output += "8"
                case 5, 2, _: output += "2"
                case 5, 3, 1: output += "5"
                case 5, 3, 2: output += "3"
                case 6, 4, _: output += "9"
                case 6, 3, 1: output += "6"
                case 6, 3, 2: output += "0"
        answer += int(output)
    return answer


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

