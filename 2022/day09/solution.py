# programming challenge from https://adventofcode.com/2022/day/9


import os
import argparse


def read_file(filename: str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"{filename} not in same directory as {os.path.basename(__file__)}")
    return data.strip()


def parse_data(filename: str) -> list[tuple[str, int]]:
    data = read_file(filename)
    return [(line.split()[0], int(line.split()[1])) for line in data.splitlines()]


class vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def copy(self) -> 'vec2':
        return vec2(self.x, self.y)

    def __eq__(self, point: 'vec2') -> bool:
        return self.x == point.x and self.y == point.y

    def __hash__(self) -> int:
        return hash((self.x, self.y)) # hash tuple of coordinates

    # operator for square bracket indexing
    def __getitem__(self, index: int) -> int:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")


def print_tail_positions(pos_list: list[vec2]) -> None:
    # minimum to rescale bottom left corner to (0, 0)
    min_x = min([point.x for point in pos_list])
    min_y = min([point.y for point in pos_list])
    # size of grid accounting for rescaled minimum
    size_x = max([point.x for point in pos_list]) - min_x + 1
    size_y = max([point.y for point in pos_list]) - min_y + 1
    # create and fill grid
    grid = [[None for _ in range(size_x)] for _ in range(size_y)]
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"  # chars to assign
    for i, point in zip(range(len(pos_list)), pos_list):
        row = point.y - min_y
        col = point.x - min_x
        grid[row][col] = chars[i % len(chars)]
    # print grid
    for i in reversed(range(len(grid))):
        for j in range(len(grid[i])):
            if i == (0 - min_y) and j == (0 - min_x):
                print("@", end="")  # starting position
            elif grid[i][j] is not None:
                print(f"{grid[i][j]}", end="")
            else:
                print(".", end="")
        print()


def tail_positions(moves: list[tuple[str, int]], knot_count: int, verbosity: int) -> list[vec2]:
    if (knot_count < 2):
        knot_count = 2
        print("WARNING: knot count must be at least 2, defaulting to 2")

    tail_pos_list = list()
    knots = [vec2(0, 0) for _ in range(knot_count)] # all stacked on top of each other

    for move in moves:
        direction, distance = move[0], move[1]
        for _ in range(distance):
            # move leading head position
            head = knots[0]
            if    direction == "U":  head.y += 1
            elif  direction == "D":  head.y -= 1
            elif  direction == "L":  head.x -= 1
            elif  direction == "R":  head.x += 1
            # move subsequent head/tail pairs
            for i in range(1, len(knots)):
                head = knots[i-1]
                tail = knots[i]
                if max(abs(head.x - tail.x), abs(head.y - tail.y)) > 1:
                    if    head.x > tail.x:  tail.x += 1
                    elif  head.x < tail.x:  tail.x -= 1
                    if    head.y > tail.y:  tail.y += 1
                    elif  head.y < tail.y:  tail.y -= 1
            # add last knot in rope to set of unique positions
            tail_pos_list.append(knots[-1].copy())

    if verbosity > 0:
        print_tail_positions(tail_pos_list)

    return tail_pos_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", default="test.txt")
    parser.add_argument("--verbose", "-v", action="count", default=0)
    parser.add_argument("--knot-count", "-n", type=int, default=2)
    args = parser.parse_args()

    data = parse_data(args.input)

    if args.verbose > 0:
        tail_positions(data, args.knot_count, args.verbose)
        print()

    part1 = len(set(tail_positions(data, 2, 0)))
    print(f"part 1: {part1}")

    part2 = len(set(tail_positions(data, 10, 0)))
    print(f"part 2: {part2}")