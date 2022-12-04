# programming challenge from https://adventofcode.com/2022/day/1


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


def parse_data(filename:str) -> typing.List[typing.List[int]]:
    data = read_file(filename)
    groups = [[int(n) for n in group.split("\n")] for group in data.split("\n\n")]
    return groups


def part1() -> int:
    groups = parse_data("input.txt")

    max_calories = 0

    for group in groups:
        calories = sum(group)
        if calories > max_calories:
            max_calories = calories

    return max_calories


def part2() -> int:
    groups = parse_data("input.txt")

    max_calories = [0] * 3
    min_index = 0

    for group in groups:
        calories = sum(group)
        if calories > max_calories[min_index]:
            max_calories[min_index] = calories
            min_index = max_calories.index(min(max_calories))

    return sum(max_calories)


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())