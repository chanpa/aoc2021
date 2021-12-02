from helper.utils import solver, parse_file_rows_to_list


DAY = 2


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, output_type=str)
    return raw_data


@solver
def part_a(data):
    commands = [line.split(" ") for line in data]
    hor = 0
    dep = 0
    for c in commands:
        command, l = c
        if command == "forward":
            hor += int(l)
        elif command == "down":
            dep += int(l)
        elif command == "up":
            dep -= int(l)
    return hor * dep


@solver
def part_b(data):
    commands = [line.split(" ") for line in data]
    hor = 0
    dep = 0
    aim = 0
    for c in commands:
        command, l = c[0], int(c[1])
        if command == "down":
            aim += l
        elif command == "up":
            aim -= l
        elif command == "forward":
            hor += l
            dep += aim * l

    return hor * dep


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

