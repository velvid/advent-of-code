class Monkey:

    def __init__(
        self,
        index: int,
        items: list[int],
        worry_eq: str,
        divisor: int,
        catcher_if_true: int,
        catcher_if_false: int
    ) -> None:

        self.index = index
        self.items = items
        self.worry_eq = worry_eq
        self.divisor = divisor
        self.catcher_if_true = catcher_if_true
        self.catcher_if_false = catcher_if_false
        self.inspect_count = 0

    def __str__(self) -> str:
        items_str = ", ".join([str(item) for item in self.items])
        return \
            f"monkey {self.index}:\n" \
            f"  starting items: {items_str}\n" \
            f"  operation: new = {self.worry_eq}\n" \
            f"  test: divisible by {self.divisor}\n" \
            f"    if true:  throw to monkey {self.catcher_if_true}\n" \
            f"    if false: throw to monkey {self.catcher_if_false}"

    def __repr__(self) -> str:
        return str(self)

    def causes_anxiety(self, old: int) -> int:
        try:
            worry = eval(self.worry_eq)
        except Exception as e:
            worry = 0
            print(f"WARNING: exception {e} with {self.worry_eq=}")
        return worry

    def checks_item(self, worry_level: int) -> bool:
        self.inspect_count += 1
        return worry_level % self.divisor == 0

    def tosses_item(self) -> int | None:
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def catches_item(self, item: int) -> None:
        self.items.append(item)


class GangOfMonkeys:

    gang: dict[int, Monkey]

    def __init__(self, gang: dict[int, Monkey]) -> None:
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
