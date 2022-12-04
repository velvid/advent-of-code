# programming challenge from https://adventofcode.com/2020/day/6


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


def parse_data(filename:str) -> typing.List[typing.List[str]]:
    data = read_file(filename)
    return [group.split() for group in data.split("\n\n")]


def part1() -> int:
    groups = parse_data("input.txt")
    group_sets = [set("".join(group)) for group in groups]
    count_sum = sum(len(group) for group in group_sets)
    return count_sum


def part2() -> int:
    groups = parse_data("input.txt")
    count_sum = 0
    for group in groups:
        intersection = set(group[0])
        for i in range(1, len(group)):
            intersection = intersection & set(group[i])
        count_sum += len(intersection)
    return count_sum


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())