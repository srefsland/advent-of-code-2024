from enum import Enum
from itertools import product

from utils.bounds import out_of_bounds
from utils.read_data import read_data


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def __call__(self, i, j):
        return (i + self.value[0], j + self.value[1])


def bfs(data, start):
    queue = [start]
    start_value = data[start[0]][start[1]]
    visited = set()
    while queue:
        i, j = queue.pop(0)
        visited.add((i, j))
        for direction in Direction:
            new_i, new_j = direction(i, j)
            if (
                not out_of_bounds(data, (new_i, new_j))
                and data[new_i][new_j] == start_value
                and not (new_i, new_j) in visited
                and not (new_i, new_j) in queue
            ):
                queue.append((new_i, new_j))

    return visited


def part1(input_data):
    data = read_data(input_data)

    plots = [(i, j) for i in range(len(data)) for j in range(len(data[0]))]

    total_price = 0

    while plots:
        i, j = plots.pop(0)
        visited = bfs(data, (i, j))

        num_connected_edges = 0

        for plot in visited:
            for direction in Direction:
                new_i, new_j = direction(*plot)
                if (new_i, new_j) in visited:
                    num_connected_edges += 1

            if plot in plots:
                plots.remove(plot)

        num_plots_region = len(visited)
        perimeter = num_plots_region * 4 - num_connected_edges
        total_price += perimeter * num_plots_region

    return total_price


def part2(input_data):
    data = read_data(input_data)

    plots = [(i, j) for i in range(len(data)) for j in range(len(data[0]))]

    total_price = 0

    while plots:
        i, j = plots.pop(0)
        visited = bfs(data, (i, j))

        num_corners = 0

        for plot in visited:
            num_corners += count_corners(*plot, visited)

            if plot in plots:
                plots.remove(plot)

        num_plots_region = len(visited)
        total_price += num_corners * num_plots_region

    return total_price


def count_corners(i, j, visited):
    num_corners = 0

    for i_direction, j_direction in product([-1, 1], repeat=2):
        neighbor_i = (i + i_direction, j)
        neighbor_j = (i, j + j_direction)

        neighbor_diag = (i + i_direction, j + j_direction)

        if not neighbor_i in visited and not neighbor_j in visited:
            num_corners += 1

        if (
            not neighbor_diag in visited
            and neighbor_i in visited
            and neighbor_j in visited
        ):
            num_corners += 1

    return num_corners


def main():
    test_input = "data/day12/test_input.txt"
    input_data = "data/day12/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
