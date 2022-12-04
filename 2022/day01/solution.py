# programming challenge from https://adventofcode.com/2022/day/1


def parse_file(filename):
    try:
        with open(filename) as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found")

    data = []
    entry = []

    for line in lines:
        if line == "":
            data.append(entry)
            entry = []
            continue
        entry.append(int(line))
    data.append(entry) # trailing entry

    return data


def part1():
    data = parse_file("input.txt")

    max_calories = 0

    for entry in data:
        calories = sum(entry)
        if calories > max_calories:
            max_calories = calories

    return max_calories


def part2():
    data = parse_file("input.txt")

    max_calories = [0] * 3
    min_index = 0

    for entry in data:
        calories = sum(entry)
        if calories > max_calories[min_index]:
            max_calories[min_index] = calories
            min_index = max_calories.index(min(max_calories))

    return sum(max_calories)


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())