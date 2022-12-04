# programming challenge from https://adventofcode.com/2022/day/3


def parse_file(filename):
    try:
        with open(filename) as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found")
    return lines


def part1():
    rucksacks = parse_file("input.txt")

    sum = 0

    for rucksack in rucksacks:

        compartment1 = rucksack[:(len(rucksack) // 2)]
        compartment2 = rucksack[(len(rucksack) // 2):]

        common = set(compartment1).intersection(set(compartment2))
        common = list(common)[0]

        if ord(common) >= ord("a") and ord(common) <= ord("z"):
            priority = ord(common) - ord("a") + 1
        elif ord(common) >= ord("A") and ord(common) <= ord("Z"):
            priority = ord(common) - ord("A") + 27

        sum += priority

    return sum


def part2():
    rucksacks = parse_file("input.txt")

    sum = 0

    for i in range(0, len(rucksacks), 3):

        group = rucksacks[i : i+3]
        common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        common = list(common)[0] # extract element from set

        if ord(common) >= ord("a") and ord(common) <= ord("z"):
            priority = ord(common) - ord("a") + 1
        elif ord(common) >= ord("A") and ord(common) <= ord("Z"):
            priority = ord(common) - ord("A") + 27

        sum += priority

    return sum


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())