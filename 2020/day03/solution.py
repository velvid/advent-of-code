# programming challenge from https://adventofcode.com/2020/day/3


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


def parse_data(filename:str) -> typing.List[str]:
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]
    return lines


def part1() -> int:
    rows = parse_data("input.txt") # list of rows

    row = 0
    col = 0
    encounters = 0

    while row < len(rows):
        if rows[row][col] == "#":
            encounters += 1
        col = (col + 3) % len(rows[0])
        row += 1

    return encounters


def part2() -> int:
    rows = parse_data("input.txt")

    # list of (col_increment, row_increment)
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1

    for step in steps:
        row = 0
        col = 0
        encounters = 0

        while row < len(rows):
            if rows[row][col] == "#":
                encounters += 1
            col = (col + step[0]) % len(rows[0])
            row += step[1]

        product *= encounters

    return product


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())