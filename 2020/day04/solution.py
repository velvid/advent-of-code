# programming challenge from https://adventofcode.com/2020/day/4


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
    return [entry.split() for entry in data.split("\n\n")]


required_fields = set("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
match_criteria = { # dictionary of lambda functions
    "byr": lambda x: (1920 <= int(x) <= 2002),
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or \
                     (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: x.startswith("#") and len(x) == 7 and all(c in "0123456789abcdef" for c in x[1:]),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isdigit(),
    "cid": lambda x: True # always true, since it's an optional field
}


def part1() -> int:
    passports = parse_data("input.txt")

    valid_passports = 0

    for passport in passports:
        current_fields = set(field.split(":")[0] for field in passport)
        missing_fields = required_fields - current_fields
        if not missing_fields:
            valid_passports += 1

    return valid_passports


def part2() -> int:
    passports = parse_data("input.txt")

    valid_passports = 0

    for passport in passports:
        current_fields = set(field.split(":")[0] for field in passport)
        missing_fields = required_fields - current_fields
        if not missing_fields:
            for field in passport:
                key, value = field.split(":")
                if not match_criteria[key](value): # match_criteria[key] looks up a function
                    break
            else: # if no break
                valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())