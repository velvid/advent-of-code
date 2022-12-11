CRT_WIDTH = 40
CRT_HEIGHT = 6
CRT_PIXELS = CRT_WIDTH * CRT_HEIGHT


class XPU:
    # type aliases
    opcode_t = str
    value_t = int | None
    instruction_t = tuple[opcode_t, value_t]
    program_t = list[instruction_t]

    def __init__(this, program: program_t):
        this.x = 1   # accumulator (discovered to be horizontal position of sprite)
        this.cc = 0  # clock cycle
        this.pc = 0  # program counter
        this.program = program
        this.signal_strengths = []
        this.frame_buffer = ""

    def store_signal_strength(this) -> None:
        # Part 1: store signal strength at 20th, 60th, ..., 220th clock cycle
        if this.cc in range(20, 221, 40):
            this.signal_strengths.append(this.cc * this.x)

    def write_to_frame_buffer(this) -> None:
        # Part 2: draw pixels if the sprite's horizontal position (x) puts its pixels
        beam_position = (this.cc - 1) % CRT_WIDTH
        sprite_region = {this.x-1, this.x, this.x+1}  # 3 pixels wide
        sprite_visible = beam_position in sprite_region
        this.frame_buffer += "#" if sprite_visible else "."
        if beam_position == CRT_WIDTH - 1 and this.cc != CRT_PIXELS:
            this.frame_buffer += "\n"

    def clock_tick(this) -> None:
        this.cc += 1
        this.write_to_frame_buffer()
        this.store_signal_strength()

    def fetch_decode(this) -> None:
        # uses 0 clock cycles
        this.opcode, this.value = this.program[this.pc]

    def execute(this) -> None:
        # determine clock cycles for this instruction
        # assume 1 clock cycle for all other instructions except "addx"
        exec_cc = 2 if this.opcode == "addx" else 1
        # simulate executing instruction (1 clock cycle per iteration)
        for _ in range(exec_cc):
            this.clock_tick()

    def writeback(this) -> None:
        # uses 0 clock cycles
        if this.opcode == "addx":
            this.x += this.value

    def run(this) -> None:
        while this.pc < len(this.program):
            this.fetch_decode()
            this.execute()
            this.writeback()
            this.pc += 1
