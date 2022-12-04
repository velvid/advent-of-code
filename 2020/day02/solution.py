# programming challenge from https://adventofcode.com/2020/day/2


import os
import typing
import re


def read_file(filename:str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not in same directory as solution.py")
    return data.strip() # remove leading/trailing whitespace


class PasswordEntry:
    def __init__(self, num1:int, num2:int, letter:str, password:str):
        self.num1 = num1
        self.num2 = num2
        self.letter = letter
        self.password = password


def parse_data(filename:str) -> typing.List[PasswordEntry]:
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]

    # regex to get num1, num2, letter, and password
    regex = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

    entries = []
    for line in lines:
        match = regex.match(line)
        if match:
            num1, num2, letter, password = match.groups()
            entries.append(PasswordEntry(int(num1), int(num2), letter, password))
        else:
            print(f"WARNING: No match for {line}")

    return entries


def part1() -> int:
    entries = parse_data("input.txt")
    valid_count = 0
    for entry in entries:
        count = entry.password.count(entry.letter)
        if entry.num1 <= count <= entry.num2:
            valid_count += 1
    return valid_count


def part2() -> int:
    entries = parse_data("input.txt")
    valid_count = 0
    for entry in entries:
        if (entry.password[entry.num1-1] == entry.letter) != \
           (entry.password[entry.num2-1] == entry.letter):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())