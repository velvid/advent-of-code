

import os
import typing


def read_file(filename:str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not in same directory as solution.py")
    return data.strip() # remove leading/trailing whitespace


# TODO appropriately change return type
def parse_data(filename:str) -> typing.List[str]:
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]
    return lines


def part1() -> int:
    data = parse_data("test.txt")
    return 0xdeadbeef


def part2() -> int:
    data = parse_data("test.txt")
    return 0xdeadbeef


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())