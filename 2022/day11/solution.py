# programming challenge from https://adventofcode.com/2022/day/11


import os
import re
import math
import argparse

from copy import deepcopy
from monkey import Monkey
from monkey import GangOfMonkeys
from monkey import Operation


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
    gang = GangOfMonkeys()

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
        # remove empty lines
        fields = [field.strip() for field in monkey.split("\n")]
        # extract data from each field using regex
        index = int(regex[0].match(fields[0]).group(1))
        items = [int(item) for item in regex[1].match(fields[1]).group(1).split(", ")]
        operation = Operation(regex[2].match(fields[2]).group(1))
        divisor = int(regex[3].match(fields[3]).group(1))
        catcher_if_true = int(regex[4].match(fields[4]).group(1))
        catcher_if_false = int(regex[5].match(fields[5]).group(1))
        # create monkey and add to the gang
        monkey = Monkey(index, items, operation, divisor,
                        catcher_if_true, catcher_if_false)
        gang.add(monkey)

    return gang


def top_two_product(gang: GangOfMonkeys) -> int:
    top2 = sorted(gang, key=(lambda monkey: monkey.inspect_count), reverse=True)[:2]
    return top2[0].inspect_count * top2[1].inspect_count


def part1(gang: GangOfMonkeys, verbose: bool) -> None:
    def relieve_worry(worry_level: int) -> int:
        return worry_level // 3

    gang.mess_around(verbose, 20, relieve_worry)
    monkey_business = top_two_product(gang)

    print(f"part 1: {monkey_business}")


def part2(gang: GangOfMonkeys, verbose: bool) -> None:
    divisors = [monkey.divisor for monkey in iter(gang)]
    lcm = math.lcm(*divisors)
    def relieve_worry(worry_level: int) -> int:
        return worry_level % lcm

    gang.mess_around(verbose, 10_000, relieve_worry)
    monkey_business = top_two_product(gang)

    print(f"Part 2: {monkey_business}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, default="test.txt", nargs="?")
    parser.add_argument("-p", "--part", type=int, default=0, nargs="?", choices=[0, 1, 2])
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    data = parse_data(args.filename)
    if args.verbose:
        print(data)

    if args.part == 1 or args.part == 0:
        d = deepcopy(data) if args.part == 0 else data
        part1(d, args.verbose)

    if args.part == 2 or args.part == 0:
        part2(data, args.verbose)
