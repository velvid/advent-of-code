# programming challenge from https://adventofcode.com/2022/day/7


import os
import re


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


file_tree_t = dict[dict[str, int]]


def parse_file(filename: str) -> file_tree_t:
    lines = read_file(filename).splitlines()

    wd = "/"  # working directory
    file_tree = dict()
    file_tree[wd] = dict()

    for line in lines:
        if line.startswith("$ cd"):
            dir = line.split()[-1]
            if dir == "/":
                wd = "/"
            elif dir == "..":
                wd = wd[:wd.rfind("/")]  # "/a/b/c" -> "/a/b" -> "/a" -> ""
            else:
                wd += ("/" + dir) if (wd != "/") else dir
                if wd not in file_tree:  # check to not overwrite
                    file_tree[wd] = dict()
        elif line.startswith("$ ls"):
            continue # only does ls on working directory
        elif line.startswith("dir"):
            continue
        else:
            file_size, file_name = re.findall(r"(\d+) (.+)", line)[0]
            file_tree[wd][file_name] = int(file_size)

    return file_tree


def print_file_tree(file_tree: file_tree_t):
    for dir in file_tree:
        print(dir)
        for file in file_tree[dir]:
            print(f"\t{file} (size = {file_tree[dir][file]})")


def get_folder_sizes(file_tree: file_tree_t) -> dict[str, int]:
    folder_sizes = dict()
    folder_sizes["/"] = 0  # empty root folder

    for dir in file_tree:
        is_root = (dir == "/")
        size = sum(file_tree[dir].values())
        while dir != "":
            # add size to all parent folders
            folder_sizes[dir] = folder_sizes.get(dir, 0) + size
            dir = dir[:dir.rfind("/")]
        # add size to root folder, since missed in loop
        if not is_root:
            folder_sizes["/"] += size

    return folder_sizes


def part1() -> int:
    file_tree = parse_file("input.txt")
    folder_sizes = get_folder_sizes(file_tree)
    # sum of all folder sizes less than 100,000
    return sum(size for size in folder_sizes.values() if size <= 100_000)


def part2() -> int:
    file_tree = parse_file("input.txt")
    folder_sizes = get_folder_sizes(file_tree)

    disk_size = 70_000_000
    required_size = 30_000_000

    currently_used = folder_sizes["/"]
    available_size = disk_size - currently_used
    need_to_free = required_size - available_size

    # initialize
    dir_to_del = "/"
    size_freed = folder_sizes["/"]

    # find the smallest folder that can be deleted to free up enough space
    for dir in folder_sizes:
        if need_to_free < folder_sizes[dir] < size_freed:
            dir_to_del = dir
            size_freed = folder_sizes[dir]

    print(f"delete {dir_to_del} to free {size_freed}")

    return size_freed


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
