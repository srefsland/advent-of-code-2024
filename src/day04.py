from utils.read_data import read_data
import numpy as np


def part1(input_data):
    data = read_data(input_data)

    grid = np.array([[char for char in line] for line in data])
    rows, cols = grid.shape

    lr_diagonals = ["".join(grid[::-1, :].diagonal(i)) for i in range(-rows + 1, cols)]
    rl_diagonals = [
        "".join(grid[::-1, ::-1].diagonal(i)) for i in range(-cols + 1, rows)
    ]

    data_top_down = ["".join(row[i] for row in data) for i in range(len(data[0]))]

    words = data + data_top_down + lr_diagonals + rl_diagonals
    xmas_count = sum(word.count("XMAS") + word.count("SAMX") for word in words)

    return xmas_count


def part2(input_data):
    data = read_data(input_data)

    am_set = set(["S", "M"])
    xmas_count = 0

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            set_diagonal = set([data[i - 1][j - 1], data[i + 1][j + 1]])
            set_other_diagonal = set([data[i - 1][j + 1], data[i + 1][j - 1]])
            if (
                data[i][j] == "A"
                and set_diagonal == am_set
                and set_other_diagonal == am_set
            ):
                xmas_count += 1

    return xmas_count


def main():
    test_input = "data/day04/test_input.txt"
    input_data = "data/day04/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
