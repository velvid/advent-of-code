# programming challenge from https://adventofcode.com/2020/day/5


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
    return lines


def part1() -> int:
    lines = parse_data("input.txt")

    max_seat_id = 0

    for seat in lines:
        rows = list(range(2**7))
        cols = list(range(2**3))
        for char in seat:
            match char:
                case "F":
                    rows = rows[ : len(rows)//2]
                case "B":
                    rows = rows[len(rows)//2 : ]
                case "L":
                    cols = cols[ : len(cols)//2]
                case "R":
                    cols = cols[len(cols)//2 : ]
                case _:
                    raise ValueError(f"invalid character {char}")
        if len(rows) != 1:
            raise ValueError("could not find single row")
        if len(cols) != 1:
            raise ValueError("could not find single column")

        seat_id = rows[0] * 8 + cols[0]
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


def part2() -> int:
    lines = parse_data("input.txt")

    taken_seats = set()

    for seat in lines:
        rows = list(range(2**7))
        cols = list(range(2**3))
        for char in seat:
            match char:
                case "F":
                    rows = rows[ : len(rows)//2]
                case "B":
                    rows = rows[len(rows)//2 : ]
                case "L":
                    cols = cols[ : len(cols)//2]
                case "R":
                    cols = cols[len(cols)//2 : ]
                case _:
                    raise ValueError(f"invalid character {char}")
        if len(rows) != 1:
            raise ValueError("could not find single row")
        if len(cols) != 1:
            raise ValueError("could not find single column")

        seat_id = rows[0] * 8 + cols[0]
        taken_seats.add(seat_id)

    all_seats = set(range(min(taken_seats), max(taken_seats)+1))
    vacant_seats = all_seats - taken_seats

    return vacant_seats.pop()


if __name__ == '__main__':
    print("part 1:", part1())
    print("part 2:", part2())