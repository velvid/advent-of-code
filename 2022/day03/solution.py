# programming challenge from https://adventofcode.com/2022/day/3


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
    rucksacks = parse_data("input.txt")

    sum = 0

    for rucksack in rucksacks:

        compartment1 = rucksack[:(len(rucksack) // 2)]
        compartment2 = rucksack[(len(rucksack) // 2):]

        common = set(compartment1) & set(compartment2) # intersection
        common = list(common)[0] # extract element from set

        if ord("a") <= ord(common) <= ord("z"):
            priority = ord(common) - ord("a") + 1
        elif ord("A") <= ord(common) <= ord("Z"):
            priority = ord(common) - ord("A") + 27
        else:
            raise ValueError(f"invalid character {common}")

        sum += priority

    return sum


def part2() -> int:
    rucksacks = parse_data("input.txt")

    sum = 0

    # iterate over groups of 3 rucksacks
    for group in [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]:

        common = set(group[0]) & set(group[1]) & set(group[2]) # intersection
        common = list(common)[0] # extract element from set

        if ord("a") <= ord(common) <= ord("z"):
            priority = ord(common) - ord("a") + 1
        elif ord("A") <= ord(common) <= ord("Z"):
            priority = ord(common) - ord("A") + 27
        else:
            raise ValueError(f"invalid character {common}")

        sum += priority

    return sum


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())