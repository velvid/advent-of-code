# programming challenge from https://adventofcode.com/2022/day/12


import os
import argparse

from heightmap import Heightmap


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


def part1(heightmap: Heightmap, verbose: bool) -> int:
    traversed_path = []  # list of traversed from start to end
    paths = [[heightmap.start]]  # list of paths
    visited = set()

    # traverse heightmap until end is reached
    while paths:
        path = paths.pop(0)  # get first path
        node = path[-1]      # get last node in path
        # already visited, skip
        if node in visited:
            continue
        # reached end, save path and break
        if node == heightmap.end:
            traversed_path = path
            break
        # mark node as visited
        visited.add(node)
        # add potential new paths to traverse
        for next in heightmap.get_traversable_nodes(node):
            paths.append(path + [next])

    if verbose:
        heightmap.print_path(traversed_path)

    return len(traversed_path) - 1  # subtract 1 for start node


def part2(heightmap: Heightmap, verbose: bool) -> int:
    traversed_path = [] # list of traversed from start to end

    # append all levels at 'a' to potential paths
    paths = [[heightmap.start]]
    for i in range(heightmap.length):
        for j in range(heightmap.width):
            if heightmap.heightmap[i][j] == "a":
                paths.append([(i, j)])

    # set of visited nodes
    visited = set()

    # traverse heightmap until end is reached
    while paths:
        path = paths.pop(0)  # get first path
        node = path[-1]      # get last node in path
        # already visited, skip
        if node in visited:
            continue
        # reached end, save path and break
        if node == heightmap.end:
            traversed_path = path
            break
        # mark node as visited
        visited.add(node)
        # add potential new paths to traverse
        for next in heightmap.get_traversable_nodes(node):
            paths.append(path + [next])

    if verbose:
        heightmap.print_path(traversed_path)

    return len(traversed_path) - 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", default="test.txt", nargs="?")
    parser.add_argument("-p", "--part", type=int, default=0, nargs="?", choices=[0, 1, 2])
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    text = read_file(args.filename)
    data = Heightmap(text)

    if args.part == 1 or args.part == 0:
        print("part 1:", part1(data, args.verbose))
    if args.part == 2 or args.part == 0:
        print("part 2:", part2(data, args.verbose))
