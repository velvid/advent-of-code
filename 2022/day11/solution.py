# programming challenge from https://adventofcode.com/2022/day/11


import os
import re
import math
import argparse

from copy import deepcopy
from typing import Callable
from monkey import Monkey
from monkey import GangOfMonkeys


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


def parse_data(filename: str) -> GangOfMonkeys:
    data = read_file(filename)
    gang = GangOfMonkeys(dict())

    regex = [
        re.compile(r"Monkey (\d+):"),
        re.compile(r"Starting items: (.+)"),
        re.compile(r"Operation: new = (.+)"),
        re.compile(r"Test: divisible by (\d+)"),
        re.compile(r"If true: throw to monkey (\d+)"),
        re.compile(r"If false: throw to monkey (\d+)")
    ]

    per_monkey = data.split("\n\n")
    for monkey in per_monkey:
        fields = [field.strip() for field in monkey.split("\n")]

        index = int(regex[0].match(fields[0]).group(1))
        items = [int(item)
                 for item in regex[1].match(fields[1]).group(1).split(", ")]
        op_eval = regex[2].match(fields[2]).group(1)  # .replace("old", "x")
        divisor = int(regex[3].match(fields[3]).group(1))
        catcher_if_true = int(regex[4].match(fields[4]).group(1))
        catcher_if_false = int(regex[5].match(fields[5]).group(1))

        monkey = Monkey(index, items, op_eval, divisor,
                        catcher_if_true, catcher_if_false)
        gang.add(monkey)

    # print(gang)
    return gang


def part1(gang: GangOfMonkeys, verbose: bool) -> None:

    for round in range(20):
        for monkey in iter(gang):
            while monkey.items != []:
                worry_level = monkey.tosses_item()
                new_level = monkey.causes_anxiety(worry_level) // 3
                if monkey.checks_item(new_level):
                    catcher = gang[monkey.catcher_if_true]
                else:
                    catcher = gang[monkey.catcher_if_false]
                catcher.catches_item(new_level)

        if verbose:
            print(f"after round {round+1}, monkeys are holding items")
            gang.print_items()
            print()

            print(f"after round {round+1}, monkeys have inspected count")
            gang.print_inspection_count()
            print()

    # get top 2 monkeys with inspection count
    top2 = sorted(gang, key=(
        lambda monkey: monkey.inspect_count), reverse=True)[:2]
    monkey_business = top2[0].inspect_count * top2[1].inspect_count
    print(f"part 1: {monkey_business}")


def part2(gang: GangOfMonkeys, verbose: bool) -> None:

    divisors = [monkey.divisor for monkey in iter(gang)]
    lcm = math.lcm(*divisors)

    for round in range(10000):
        for monkey in iter(gang):
            while monkey.items != []:
                worry_level = monkey.tosses_item()
                new_level = monkey.causes_anxiety(worry_level) % lcm
                if monkey.checks_item(new_level):
                    catcher = gang[monkey.catcher_if_true]
                else:
                    catcher = gang[monkey.catcher_if_false]
                catcher.catches_item(new_level)

        if verbose and (round+1) % 1000 == 0:
            print(f"after round {round+1}, monkeys are holding items")
            gang.print_items()
            print()

            print(f"after round {round+1}, monkeys have inspected count")
            gang.print_inspection_count()
            print()

    # get top 2 monkeys with inspection count
    top2 = sorted(gang, key=(
        lambda monkey: monkey.inspect_count), reverse=True)[:2]
    monkey_business = top2[0].inspect_count * top2[1].inspect_count
    print(f"Part 2: {monkey_business}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, default="test.txt", nargs="?")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-p", "--part", type=int,
                        choices=[1, 2, 12, 21], default=12)
    args = parser.parse_args()

    data = parse_data(args.file)
    if args.part in [1, 12, 21]:
        part1(deepcopy(data), args.verbose)
    if args.part in [2, 12, 21]:
        part2(data, args.verbose)
