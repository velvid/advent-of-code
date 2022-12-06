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


def find_unique_substring(data: str, window_size: int) -> int:
    data = parse_data("input.txt")
    for i in range(len(data) - window_size):
        window = data[i:i+window_size]
        if len(set(window)) == window_size:
            return i + window_size


def part1() -> int:
    return find_unique_substring(parse_data("input.txt"), 4)


def part2() -> int:
    return find_unique_substring(parse_data("input.txt"), 14)


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())
