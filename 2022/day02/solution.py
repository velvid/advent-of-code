# programming challenge from https://adventofcode.com/2022/day/2


import os
import typing


def read_file(filename:str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    try:
        with open(file_path) as file:
            data = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not in same directory as solution.py")
    return data.strip() # remove leading/trailing whitespace


def parse_data(filename:str) -> typing.List[str]:
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]

    elf_sequence = []
    your_sequence = []

    for line in lines:
        entry = line.split(" ")
        elf_sequence.append(entry[0])
        your_sequence.append(entry[1])

    return elf_sequence, your_sequence


def part1():
    elf_sequence, your_sequence = parse_data("input.txt")

    score_table = [1, 2, 3] # indices indicate score for rock, paper, scissors
    total_score = 0

    for you, elf in zip(your_sequence, elf_sequence):

        score = 0
        elf_index = ord(elf) - ord("A")
        your_index = ord(you) - ord("X")

        score += score_table[your_index]

        if your_index == ((elf_index + 1) % 3):
            score += 6
        elif your_index == elf_index:
            score += 3

        total_score += score

    return total_score


def part2():
    elf_sequence, your_sequence = parse_data("input.txt")

    score_table = [1, 2, 3] # indices indicate score for rock, paper, scissors
    total_score = 0

    for you, elf in zip(your_sequence, elf_sequence):

        score = 0
        elf_index = ord(elf) - ord("A")

        if you == "X":
            score += 0 # lose
            score += score_table[(elf_index + 2) % 3]
        elif you == "Y":
            score += 3 # draw
            score += score_table[(elf_index + 0) % 3]
        elif you == "Z":
            score += 6 # win
            score += score_table[(elf_index + 1) % 3]

        total_score += score

    return total_score


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())