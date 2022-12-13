class Heightmap:
    node_t = tuple[int, int]
    map_t = list[list[str]]

    def __init__(self, string: str) -> None:
        self.heightmap = [[char for char in line.strip()]
                          for line in string.splitlines()]
        self.length = len(self.heightmap)
        self.width = len(self.heightmap[0])

        self.start, self.end = None, None
        find_start, find_end = False, False
        for i in range(self.length):
            for j in range(self.width):
                if self.heightmap[i][j] == "S":
                    self.start = (i, j)
                    find_start = True
                if self.heightmap[i][j] == "E":
                    self.end = (i, j)
                    find_end = True
                if find_start and find_end:
                    break

        if self.start is None:
            raise ValueError("No start node found")
        if self.end is None:
            raise ValueError("No end node found")

    def __repr__(self) -> str:
        return "\n".join(["".join(line) for line in self.heightmap])

    def is_in_bounds(self, node: node_t) -> bool:
        return 0 <= node[0] < self.length and \
               0 <= node[1] < self.width

    def too_high(self, current: node_t, to_climb: node_t) -> bool:
        n1 = ord("a") if current == self.start else \
             ord(self.heightmap[current[0]][current[1]])
        n2 = ord("z") if to_climb == self.end else \
             ord(self.heightmap[to_climb[0]][to_climb[1]])
        return (n2 - n1 >= 2)

    def get_traversable_nodes(self, node: node_t) -> list[node_t]:
        indices = [
            (node[0] - 1, node[1]),  # up
            (node[0] + 1, node[1]),  # down
            (node[0], node[1] - 1),  # left
            (node[0], node[1] + 1)   # right
        ]
        nodes = [
            next for next in indices if
            self.is_in_bounds(next) and
            not self.too_high(node, next)
        ]
        return nodes

    def print_path(self, path: list[node_t]) -> None:
        str_buffer = [["." for _ in range(self.width)] for _ in range(self.length)]

        for i in range(len(path) - 1):
            node = path[i]
            next = path[i + 1]
            if   node[0] - next[0] ==  1: arrow = "^"
            elif node[0] - next[0] == -1: arrow = "v"
            elif node[1] - next[1] ==  1: arrow = "<"
            elif node[1] - next[1] == -1: arrow = ">"
            else:
                print(f"ERROR: {node} -> {next} is not a valid path, not printing")
                return
            str_buffer[node[0]][node[1]] = arrow

        end_i, end_j = self.end
        str_buffer[end_i][end_j] = "X"  # X marks the spot!

        print("\n".join(["".join(line) for line in str_buffer]))