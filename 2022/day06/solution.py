# programming challenge from https://adventofcode.com/2022/day/6


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


def parse_data(filename: str) -> str:
    data = read_file(filename)
    return data.strip()


def part1() -> int:
    data = parse_data("input.txt")

    window_size = 4
    window = set()

    for i in range(len(data)):
        window.add(data[i])
        if len(window) == window_size:
            return i + 1
        if i >= len(data) - window_size:
            return -1

    return -1  # failure


def part2() -> int:
    data = parse_data("input.txt")

    window_size = 14
    window = set()

    for i in range(len(data)):
        window.add(data[i])
        if len(window) == window_size:
            return i + 1
        if i >= len(data) - window_size:
            return -1

    return -1  # failure


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())
