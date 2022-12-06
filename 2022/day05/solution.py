# programming challenge from https://adventofcode.com/2022/day/5


import os
import re
from typing import List, Tuple


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


class MoveInstruction:
    def __init__(self, quant: int, src: int, dst: int):
        self.quant = quant
        self.src = src
        self.dst = dst

    def __repr__(self) -> str:
        return f"move {self.quant} from {self.src} to {self.dst}"


def parse_data(filename: str) -> Tuple[List[List[str]], List[MoveInstruction]]:
    data = read_file(filename)

    try:
        stacks_text, procedure_text = data.split("\n\n")
    except ValueError:
        raise ValueError(
            f"Invalid input in {filename}. Ensure crate information and procedure is separated by '\\n\\n'.")
    stacks_text = stacks_text.split('\n')
    procedure_text = procedure_text.split('\n')

    # This is what stacks_text should look like
    # '    [D]    '
    # '[N] [C]    '
    # '[Z] [M] [P]'
    # ` 1   2   3`
    # alphabetical characters are at indices 1, 5, 9, etc. (starting at 0, of course)
    # NOTE: trailing spaces may be trimmed from editors, so consider such cases

    # extract last number from " 1   2   3\n"
    column_count = int(stacks_text[-1].strip()[-1])
    stacks_text = stacks_text[:-1]  # last line no longer necessary
    stacks_text = stacks_text[::-1]  # reverse
    row_count = len(stacks_text)  # get tallest column/stack

    # extract crate information from text
    stacks = [[] for i in range(column_count)]
    for i in range(row_count):
        for j, crates_i in zip(range(1, column_count*4 + 1, 4), range(column_count)):
            if j > len(stacks_text[i]):
                break
            if stacks_text[i][j] == ' ':
                continue
            stacks[crates_i].append(stacks_text[i][j])

    # get information from
    # 'move 1 from 2 to 1'
    regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

    # extract procedure/move information from text
    procedure = []
    for text in procedure_text:
        match = regex.match(text)
        if not match:
            continue
        quantity, src, dst = match.groups()
        procedure.append(MoveInstruction(int(quantity), int(src), int(dst)))

    return stacks, procedure


def part1() -> str:
    stacks, procedure = parse_data("input.txt")

    # NOTE: naive solution popping and appending
    # for move in procedure:
    #     for i in range(move.quant):
    #         if stacks[move.src - 1]:
    #             stacks[move.dst - 1].append(stacks[move.src - 1].pop())
    #         else:
    #             print("WARNING: Attempted to move from empty stack.")

    # faster solution using list slicing
    for move in procedure:
        stacks[move.dst-1] += stacks[move.src-1][-move.quant::][::-1]
        stacks[move.src-1] = stacks[move.src-1][:-move.quant]

    return "".join([crate[-1] for crate in stacks])


def part2() -> str:
    stacks, procedure = parse_data("input.txt")

    # NOTE: naive solution using temporary stack
    # for move in procedure:
    #     temp_stack = []  # not the most elegant solution, but it works
    #     for i in range(move.quant):
    #         if stacks[move.src - 1]:
    #             temp_stack.append(stacks[move.src - 1].pop())
    #     for i in range(move.quant):
    #         stacks[move.dst - 1].append(temp_stack.pop())

    # faster solution using list slicing
    for move in procedure:
        stacks[move.dst-1] += stacks[move.src-1][-move.quant:]
        stacks[move.src-1] = stacks[move.src-1][:-move.quant]

    return "".join([crate[-1] for crate in stacks])


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())
