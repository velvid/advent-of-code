

def parse_file(filename):
    lines = []
    try:
        with open(filename) as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found")
    return lines


def part1():
    return


def part2():
    return


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())