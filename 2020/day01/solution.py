# programming challenge from https://adventofcode.com/2020/day/1


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


def parse_data(filename:str) -> typing.List[int]:
    data = read_file(filename)
    return [int(line.strip()) for line in data.splitlines()]


def part1() -> int:
    data = parse_data("input.txt")

    # find two numbers in data that add to 2020
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

    print("No solution found.")
    return 0


def part2() -> int:
    data = parse_data("input.txt")

    # find three numbers in data that add to 2020
    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

    print("No solution found.")
    return 0


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())