# programming challenge from https://adventofcode.com/2020/day/8


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
    return data


def parse_data(filename: str) -> list[tuple[str, int]]:
    data = read_file(filename)
    lines = [line.strip() for line in data.splitlines()]
    program = []
    for line in lines:
        opcode, value = line.split()
        program.append((opcode, int(value)))
    return program


class ProgramInfo():
    def __init__(self, pc: int, acc: int):
        self.pc = pc
        self.acc = acc


def run_program(program: list[tuple[str, int]]) -> ProgramInfo:
    pc = 0  # program counter
    acc = 0  # accumulator

    visited = set()  # needed to detect infinite loops

    while pc not in visited and pc < len(program):
        visited.add(pc)
        opcode, value = program[pc]
        match opcode:
            case "nop":
                pc += 1
            case "acc":
                acc += value
                pc += 1
            case "jmp":
                pc += value
            case _:
                raise ValueError(f"unknown opcode {opcode}")
        if pc > len(program):
            raise ValueError("pc out of range")

    return ProgramInfo(pc, acc)


def part1(program: list[tuple[str, int]]) -> int:
    return run_program(program).acc


def part2(program: list[tuple[str, int]]) -> int:
    # list of pc values for jmp and nop instructions
    jmp_nop = [pc for pc, (opcode, _) in enumerate(program)
               if opcode in ("jmp", "nop")]
    # try switching each jmp and nop instruction until program terminates
    for pc in jmp_nop:
        opcode, value = program[pc]
        match opcode:
            case "jmp":
                # switch jmp to nop
                program[pc] = ("nop", value)
            case "nop":
                # switch nop to jmp
                program[pc] = ("jmp", value)
            case _:
                # should never happen
                raise ValueError(f"unknown opcode {opcode}")
        # get program info after switching instruction
        info = run_program(program)
        # check if program terminated
        if info.pc == len(program):
            return info.acc
        # switch back to original instruction
        program[pc] = (opcode, value)

    print("no solution found")
    return -1


if __name__ == '__main__':
    data = parse_data("input.txt")
    print("part 1:", part1(data))
    print("part 2:", part2(data))
