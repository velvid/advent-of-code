# programming challenge from https://adventofcode.com/2020/day/7


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


'''
bag_tree = {
    "parent1": {
        "child1": int,
        "child2": int,
        ...
        "childN": int
    },
    ...
    "parentN": {
        "child1": int,
        "child2": int,
        ...
        "childN": int
    }
}
'''
bag_tree_t = dict[str, dict[str, int]]


def print_bag_tree(bag_tree: bag_tree_t) -> None:
    for parent in bag_tree:
        print(parent, "bag contains", bag_tree[parent])


def parse_data(filename: str) -> bag_tree_t:
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]

    bag_tree = dict()

    regex_none = re.compile(r"(.+) bags contain no other bags.")
    regex_multi = re.compile(r"(.+) bags contain (.+)")
    regex_bag = re.compile(r"(\d+) (.+) bag")

    for line in lines:

        match_none = regex_none.match(line)
        if match_none:
            source_bag = match_none.group(1)
            bag_tree[source_bag] = dict()  # no children
            continue

        match_multi = regex_multi.match(line)
        if match_multi:
            source_bag = match_multi.group(1)
            child_bags = match_multi.group(2).split(", ")
            for bag in child_bags:
                match_bag = regex_bag.match(bag)
                if match_bag:
                    bag_count = int(match_bag.group(1))
                    bag_name = match_bag.group(2)
                    if source_bag in bag_tree:
                        bag_tree[source_bag][bag_name] = bag_count
                    else:
                        bag_tree[source_bag] = dict()
                        bag_tree[source_bag][bag_name] = bag_count
            continue

    # print_bag_tree(bag_tree)
    return bag_tree


# boolean function to check if a bag can contain a shiny gold bag
def contains_shiny_gold(bag_tree: bag_tree_t, bag_to_search: str) -> bool:
    if "shiny gold" in bag_tree[bag_to_search]:
        return True
    for child_bag in bag_tree[bag_to_search]:
        if contains_shiny_gold(bag_tree, child_bag):
            return True
    return False


# count all bags inside of a parent bag
def count_bags(bag_tree: bag_tree_t, bag_to_search: str) -> int:
    bag_count = 0
    for child_bag in bag_tree[bag_to_search]:
        bag_count += bag_tree[bag_to_search][child_bag] * \
            (1 + count_bags(bag_tree, child_bag))
    return bag_count


# count outermost bag colors that can contain a shiny gold bag
def part1(tree: bag_tree_t) -> int:
    shiny_count = 0
    for outer_bag in tree:
        if contains_shiny_gold(tree, outer_bag):
            shiny_count += 1
    return shiny_count


# count how many individual bags are required inside a single shiny gold bag
def part2(bag_tree: bag_tree_t) -> int:
    return count_bags(bag_tree, "shiny gold")


if __name__ == '__main__':
    data = parse_data("input.txt")
    print("part 1:", part1(data))
    print("part 2:", part2(data))
