# programming challenge from https://adventofcode.com/2022/day/4


def parse_file(filename: str):
    try:
        with open(filename) as file:
            lines = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found")
    return lines


def part1():
    pairs = parse_file("input.txt")

    count = 0
    for pair in pairs:
        range1 = pair[0].split('-')
        range2 = pair[1].split('-')

        # method A (slower, but more explicit)
        # set1 = set(range(int(range1[0]), int(range1[1]) + 1))
        # set2 = set(range(int(range2[0]), int(range2[1]) + 1))
        # if len(set1.intersection(set2)) == min(len(set1), len(set2)):
        #     count += 1

        # method B
        lower1 = int(range1[0])
        upper1 = int(range1[1])

        lower2 = int(range2[0])
        upper2 = int(range2[1])

        if (lower1 <= lower2 <= upper1 and lower1 <= upper2 <= upper1) or \
           (lower2 <= lower1 <= upper2 and lower2 <= upper1 <= upper2):
            count += 1

    return count


def part2():
    pairs = parse_file("input.txt")

    count = 0
    for pair in pairs:
        range1 = pair[0].split('-')
        range2 = pair[1].split('-')

        # method A (slower, but more explicit)
        # set1 = set(range(int(range1[0]), int(range1[1]) + 1))
        # set2 = set(range(int(range2[0]), int(range2[1]) + 1))
        # if len(set1.intersection(set2)) > 0:
        #     count += 1

        # method B
        lower1 = int(range1[0])
        upper1 = int(range1[1])

        lower2 = int(range2[0])
        upper2 = int(range2[1])

        if (lower1 <= lower2 <= upper1) or \
           (lower2 <= lower1 <= upper2):
            count += 1

    return count


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())

    # time execution of part1 and part2
    # print("part 1:", timeit.timeit(part1, number=1000))
    # print("part 2:", timeit.timeit(part2, number=1000))