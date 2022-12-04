# programming challenge from https://adventofcode.com/2022/day/2


def parse_file(filename):
    try:
        with open(filename) as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found")

    elf_sequence = []
    your_sequence = []

    for line in lines:
        entry = line.split(" ")
        elf_sequence.append(entry[0])
        your_sequence.append(entry[1])

    return elf_sequence, your_sequence


def part1():
    elf_sequence, your_sequence = parse_file("input.txt")

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
    elf_sequence, your_sequence = parse_file("input.txt")

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