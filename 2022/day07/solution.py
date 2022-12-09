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
            elif dir == ".." and "/" not in wd[1:]:
                # to handle "/a" -> "/" (see next elif)
                wd = "/"
            elif dir == "..":
                # "/a/b/c" -> "/a/b" -> "/a" -> ""
                wd = wd[:wd.rfind("/")]
            else:
                # append to wd and create file dict
                wd += ("/" + dir) if (wd != "/") else dir
                if wd not in file_tree:  # check to not overwrite
                    file_tree[wd] = dict()
        elif line.startswith("$ ls"):
            continue  # only does ls on working directory
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
    folder_sizes["/"] = 0  # initially, assume empty root folder

    for dir, files in file_tree.items():
        is_root = (dir == "/")
        size = sum(files.values())
        while dir != "":
            # add size to all parent folders
            folder_sizes[dir] = folder_sizes.get(dir, 0) + size
            dir = dir[:dir.rfind("/")]  # skips "/", i.e. "/a" -> ""
        # add size to root folder, since missed in loop
        if not is_root:
            folder_sizes["/"] += size

    return folder_sizes


def part1(folder_sizes: dict[str, int]) -> int:
    # sum of all folder sizes less than 100,000
    return sum(size for size in folder_sizes.values() if size <= 100_000)


def part2(folder_sizes: dict[str, int]) -> int:
    disk_space = 70_000_000
    required_space = 30_000_000

    available_space = disk_space - folder_sizes["/"]
    need_to_free = required_space - available_space

    if need_to_free <= 0:
        return 0

    # initialize to root folder, then find smaller folder
    dir_to_del = "/"
    space_freed = folder_sizes["/"]

    # find the smallest folder that can be deleted to free up enough space
    for dir in folder_sizes:
        if need_to_free < folder_sizes[dir] < space_freed:
            dir_to_del = dir
            space_freed = folder_sizes[dir]

    # print(f"delete {dir_to_del} to free {space_freed}")
    return space_freed


if __name__ == "__main__":
    file_tree = parse_file("input.txt")
    folder_sizes = get_folder_sizes(file_tree)
    print(f"Part 1: {part1(folder_sizes)}")
    print(f"Part 2: {part2(folder_sizes)}")
