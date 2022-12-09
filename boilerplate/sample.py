

import os


def read_file(filename: str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"{filename} not in same directory as solution.py")
    return data


# TODO appropriately change return type
def parse_data(filename: str):
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]
    return lines


def part1(data) -> int:
    return -1


def part2(data) -> int:
    return -1


if __name__ == '__main__':
    data = parse_data("test.txt")
    print("part 1:", part1(data))
    print("part 2:", part2(data))
