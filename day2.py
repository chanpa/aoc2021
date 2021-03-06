from helper.utils import time_function, parse_file_rows_to_list


DAY = 2


def prepare_data():
    raw_data = parse_file_rows_to_list(DAY, split_row_on=" ")
    commands = [(command, int(units)) for command, units in raw_data]
    return commands


@time_function
def part_a(data):
    x_pos, z_pos = 0, 0
    for command_name, units in data:
        command = COMMANDS[command_name]
        if command_name == "forward":
            x_pos += command(units)
        else:
            z_pos += command(units)
    return z_pos * x_pos


@time_function
def part_b(data):
    pos = [0, 0]
    aim = 0
    for command_name, units in data:
        if command_name == "forward":
            pos = COMMANDS[f"{command_name}_b"](pos, units, aim)
        else:
            aim += COMMANDS["aim"](units, command_name)
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

