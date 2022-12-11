# programming challenge from https://adventofcode.com/2022/day/10


import os
from processor import XPU


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


def parse_data(filename: str) -> XPU.program_t:
    raw_lines = read_file(filename).splitlines()
    instructions = []
    for line in raw_lines:
        instruction = line.strip().split()
        opcode = instruction[0]
        value = int(instruction[1]) if len(instruction) > 1 else None
        instructions.append((opcode, value))
    return instructions


if __name__ == '__main__':
    program = parse_data("input.txt")
    xpu = XPU(program)
    xpu.run()
    print(f"part 1: {sum(xpu.signal_strengths)}")
    print(f"part 2: \n{xpu.frame_buffer}")
