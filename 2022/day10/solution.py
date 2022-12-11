# programming challenge from https://adventofcode.com/2022/day/10


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


class CPU:
    # type aliases
    opcode_t = str
    value_t = int | None
    instruction_t = tuple[opcode_t, value_t]
    program_t = list[instruction_t]

    def __init__(self, program: program_t):
        self.x = 1  # accumulator
        self.cc = 0  # clock cycle
        self.pc = 0  # program counter
        self.program = program
        self.signal_strengths = []
        self.frame_buffer = ""

    def write_to_frame_buffer(self) -> None:
        # Part 2: draw pixels if the sprite's horizontal position (X) puts its pixels
        beam_position = (self.cc - 1) % 40
        visible = beam_position in {self.x-1, self.x, self.x+1}
        self.frame_buffer += "#" if visible else "."

    def store_signal_strength(self) -> None:
        # Part 1: store signal strength at every 40th clock cycle
        if self.cc in range(20, 221, 40):
            self.signal_strengths.append(self.cc * self.x)

    def fetch_decode(self) -> None:
        # uses 0 clock cycles
        self.opcode, self.value = self.program[self.pc]

    def execute(self) -> None:
        # determine clock cycles for this instruction
        match self.opcode:
            case "noop":
                exec_cc = 1
            case "addx":
                exec_cc = 2
        # execute instruction (1 clock cycle per iteration)
        for _ in range(exec_cc):
            self.cc += 1
            self.write_to_frame_buffer()
            self.store_signal_strength()

    def writeback(self) -> None:
        # uses 0 clock cycles
        if self.opcode == "addx":
            self.x += self.value

    def run(self) -> None:
        while self.pc < len(self.program):
            self.fetch_decode()
            self.execute()
            self.writeback()
            self.pc += 1

        print(f"part 1: {sum(self.signal_strengths)}")
        print(f"part 2:")
        for i in range(0, 201, 40):
            print(self.frame_buffer[i: i + 40])


def parse_data(filename: str) -> CPU.program_t:
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
    CPU(program).run()
