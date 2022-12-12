from typing import Callable
import re


class Operation:
    def __init__(self, operation_str: str) -> None:
        self.operation_str = operation_str
        self.operation = self.parse_operation(operation_str)

    def __call__(self, x: int) -> int:
        return self.operation(x)

    def __str__(self) -> str:
        return self.operation_str

    def __repr__(self) -> str:
        return self.operation_str

    @staticmethod
    def parse_operation(str_op: str) -> Callable[[int], int]:
        pattern = r"([\d]+|[\w]+) ([\+\-\*\/]) ([\d]+|[\w]+)"
        match = re.match(pattern, str_op)

        if match is None:
            raise ValueError(f"invalid operation: {str_op=}")

        operand_a = match.group(1)
        operand_b = match.group(3)

        operator_set = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }
        operator_char = match.group(2)
        operator = operator_set.get(operator_char)

        if operator is None:
            raise ValueError(f"invalid operator: {operator_char=}")

        def operation(x: int) -> int:
            a = int(operand_a) if operand_a.isnumeric() else x
            b = int(operand_b) if operand_b.isnumeric() else x
            return operator(a, b)

        return operation


class Monkey:
    def __init__(
        self, index: int, items: list[int], operation: Operation, divisor: int,
        catcher_if_true: int, catcher_if_false: int
    ) -> None:
        self.index = index
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.catcher_if_true = catcher_if_true
        self.catcher_if_false = catcher_if_false
        self.inspect_count = 0

    def __str__(self) -> str:
        items_str = ", ".join([str(item) for item in self.items])
        return \
            f"monkey {self.index}:\n" \
            f"  starting items: {items_str}\n" \
            f"  operation: new = {self.operation}\n" \
            f"  test: divisible by {self.divisor}\n" \
            f"    if true:  throw to monkey {self.catcher_if_true}\n" \
            f"    if false: throw to monkey {self.catcher_if_false}"

    def __repr__(self) -> str:
        return str(self)

    def creates_worry(self, old_worry: int) -> int:
        return self.operation(old_worry)

    def checks_item(self, worry_level: int) -> bool:
        self.inspect_count += 1
        return worry_level % self.divisor == 0

    def tosses_item(self) -> int | None:
        if len(self.items) == 0:
            print(f"WARNING: monkey {self.index} has no items to toss")
            return None
        return self.items.pop(0)

    def catches_item(self, item: int) -> None:
        self.items.append(item)


class GangOfMonkeys:

    gang: dict[int, Monkey]

    def __init__(self, gang: dict[int, Monkey] = dict()) -> None:
        self.gang = gang

    def __str__(self) -> str:
        return "\n\n".join([str(monkey) for monkey in self.gang.values()])

    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, index: int) -> Monkey | None:
        return self.gang.get(index)

    def __contains__(self, monkey: Monkey) -> bool:
        return monkey in self.gang.values()

    def __iter__(self) -> Monkey:
        return iter(self.gang.values())

    def __len__(self) -> int:
        return len(self.gang)

    def add(self, monkey: Monkey) -> None:
        self.gang[monkey.index] = monkey

    def print_inspection_count(self) -> None:
        for monkey in self.gang.values():
            print(
                f"monkey {monkey.index} inspected items {monkey.inspect_count} times")

    def print_items(self) -> None:
        for monkey in self.gang.values():
            items_str = ", ".join([str(item) for item in monkey.items])
            print(f"monkey {monkey.index}: {items_str}")

    def mess_around(self, verbose: bool, rounds: int, relief_function: Callable | None = None) -> None:
        for round in range(rounds):
            for monkey in self.gang.values():
                # each monkey throws all items in their possession when its their turn
                while monkey.items != []:
                    worry_level = monkey.tosses_item()
                    new_level = monkey.creates_worry(worry_level)
                    # if a relief function is provided, apply it to the worry level
                    if relief_function is not None:
                        new_level = relief_function(new_level)
                    # determine which monkey will catch the item
                    if monkey.checks_item(new_level):
                        catcher = self.gang[monkey.catcher_if_true]
                    else:
                        catcher = self.gang[monkey.catcher_if_false]
                    # the catcher catches the item and adds it to their possession
                    catcher.catches_item(new_level)

            # print the monkeys' items after each round
            if verbose:
                print(f"after round {round+1}, monkeys are holding items")
                for monkey in self.gang.values():
                    items_str = ", ".join([str(item) for item in monkey.items])
                    print(f"monkey {monkey.index}: {items_str}")
                print()
                print(f"after round {round+1}, monkeys have inspected count")
                for monkey in self.gang.values():
                    print(f"monkey {monkey.index} inspected items {monkey.inspect_count} times")
                print()
