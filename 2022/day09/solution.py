# programming challenge from https://adventofcode.com/2022/day/9


import os


def read_file(filename: str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"{filename} not in same directory as solution.py")
    return data.strip()


def parse_data(filename: str) -> list[tuple[str, int]]:
    data = read_file(filename)
    lines = [line for line in data.splitlines()]
    moves = []
    for line in lines:
        dir = line.split()[0]
        dist = line.split()[1]
        moves.append((dir, int(dist)))
    return moves


class vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def print_tail_positions(tail_list: set[tuple[int, int]]) -> None:
    # minimum to rescale to 0,0 in bottom left corner
    start_x = min([point[0] for point in tail_list])
    start_y = min([point[1] for point in tail_list])
    # size of grid accounting for rescaled minimum
    size_x = max([point[0] for point in tail_list]) - start_x + 1
    size_y = max([point[1] for point in tail_list]) - start_y + 1
    # create and fill grid
    grid = [[False for _ in range(size_x)] for _ in range(size_y)]
    for point in tail_list:
        point_x = point[0] - start_x
        point_y = point[1] - start_y
        grid[point_y][point_x] = True
    # print grid
    for i in range(len(grid)-1, -1, -1):  # 0,0 is bottom left
        for j in range(len(grid[i])):
            if i == -start_y and j == -start_x:
                print("o", end="")
            elif grid[i][j]:
                print("x", end="")
            else:
                print(".", end="")
        print()


def get_tail_positions(moves: list[tuple[str, int]], knot_count: int) -> int:
    if (knot_count < 2):
        raise ValueError(f"knot_count must be at least 2, not {knot_count}")

    tail_list = set()
    knots = [vec2(0, 0) for _ in range(knot_count)]

    for move in moves:
        direction, distance = move[0], move[1]
        for _ in range(distance):
            # move leading head position
            head = knots[0]
            if direction == "U":
                head.y += 1
            elif direction == "D":
                head.y -= 1
            elif direction == "L":
                head.x -= 1
            elif direction == "R":
                head.x += 1
            # move subsequent head/tail pairs
            for i in range(1, len(knots)):
                head = knots[i-1]
                tail = knots[i]
                if max(abs(head.x - tail.x), abs(head.y - tail.y)) > 1:
                    if head.x > tail.x:
                        tail.x += 1
                    elif head.x < tail.x:
                        tail.x -= 1
                    if head.y > tail.y:
                        tail.y += 1
                    elif head.y < tail.y:
                        tail.y -= 1
            # add last knot in rope to set of unique positions
            tail_list.add((knots[-1].x, knots[-1].y))  # (x, y) tuple

    print_tail_positions(tail_list)
    return len(tail_list)


def part1(moves: list[tuple[str, int]]) -> int:
    return get_tail_positions(moves, 2)


def part2(moves: list[tuple[str, int]]) -> int:
    return get_tail_positions(moves, 10)


if __name__ == '__main__':
    data = parse_data("test2.txt")
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")
