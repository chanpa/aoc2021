from helper.utils import solver, parse_file_rows_to_list


DAY = 2


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=" ")
    commands = [(command, int(units)) for command, units in raw_data]
    return commands


@solver
def part_a(data):
    x_pos, z_pos = 0, 0
    for command, units in data:
        if command == "forward":
            x_pos += COMMANDS[command](units)
        else:
            z_pos += COMMANDS[command](units)
    return z_pos * x_pos


@solver
def part_b(data):
    pos = [0, 0]
    aim = 0
    for command, units in data:
        if command == "forward":
            pos = COMMANDS[f"{command}_b"](pos, units, aim)
        else:
            aim += COMMANDS["aim"](units, command)
    return pos[0] * pos[1]


COMMANDS = {
    "forward": lambda units: units,
    "up": lambda units: -units,
    "down": lambda units: units,
    "aim": lambda units, direction: units if direction == "down" else -units,
    "forward_b": lambda position, units, aim: [position[0] + units, position[1] + units * aim]
}


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

