# programming challenge from https://adventofcode.com/2022/day/8


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
    return data.strip()  # remove leading/trailing whitespace


def parse_data(filename: str) -> list[list[int]]:
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]
    grid = [[int(c) for c in line] for line in lines]
    return grid


def part1(grid: list[list[int]]) -> int:
    row_size = len(grid[0])
    col_size = len(grid)

    # initialised to perimeter of grid (since it's always visible)
    visible_count = 2*row_size + 2*col_size - 4

    # iterate over each cell, ignoring perimeter
    for row in range(1, row_size-1):
        for col in range(1, col_size-1):
            # highest value in each direction
            highest = [0, 0, 0, 0]
            # column by column from left to right along row
            highest[0] = grid[row][0]  # initialise to edge
            for i in range(1, col):
                if grid[row][i] > highest[0]:
                    highest[0] = grid[row][i]
            # column by column from right to left along row
            highest[1] = grid[row][-1]
            for i in range(row_size-2, col, -1):
                if grid[row][i] > highest[1]:
                    highest[1] = grid[row][i]
            # row by row from top to bottom along column
            highest[2] = grid[0][col]
            for i in range(1, row):
                if grid[i][col] > highest[2]:
                    highest[2] = grid[i][col]
            # row by row from bottom to top along column
            highest[3] = grid[-1][col]
            for i in range(col_size-2, row, -1):
                if grid[i][col] > highest[3]:
                    highest[3] = grid[i][col]
            # if current cell is visible from AT LEAST ONE direction
            # i.e. if it's greater than the highest value in at least one direction
            if grid[row][col] > min(highest):
                visible_count += 1
                continue

    return visible_count


def part2(grid: list[list[int]]) -> int:
    row_size = len(grid[0])
    col_size = len(grid)

    highest_score = 0

    # iterate over each cell, ignoring perimeter
    # since perimeter will always yield score of 0
    for row in range(1, row_size-1):
        for col in range(1, col_size-1):
            # score in each direction (up, down, left, right)
            scores = [0, 0, 0, 0]
            # scan from current cell to top
            for i in range(row-1, -1, -1):
                scores[0] += 1
                if grid[row][col] <= grid[i][col]:
                    break
            # scan from current cell to bottom
            for i in range(row+1, col_size):
                scores[1] += 1
                if grid[row][col] <= grid[i][col]:
                    break
            # scan from current cell to left
            for i in range(col-1, -1, -1):
                scores[2] += 1
                if grid[row][col] <= grid[row][i]:
                    break
            # scan from current cell to right
            for i in range(col+1, row_size):
                scores[3] += 1
                if grid[row][col] <= grid[row][i]:
                    break
            # calculate final score and update highest score
            final_score = 1
            for score in scores:
                final_score *= score
            if final_score > highest_score:
                highest_score = final_score

    return highest_score


if __name__ == '__main__':
    grid = parse_data("input.txt")
    print("part 1:", part1(grid))
    print("part 2:", part2(grid))
