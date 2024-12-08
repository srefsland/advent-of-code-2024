from functools import reduce
from itertools import product

from utils.read_data import read_data


def get_calibrated_sum(data, math_functions):
    sum_calibrated = 0

    sums, number_lists = zip(*[line.split(":") for line in data])
    sums = [int(sum_) for sum_ in sums]
    number_lists = [list(map(int, number_list.split())) for number_list in number_lists]

    for sum_, number_list in zip(sums, number_lists):
        num_combinations_operations = len(number_list) - 1

        for operations in product(math_functions, repeat=num_combinations_operations):
            operations = list(operations)
            result = reduce(
                lambda num1, num2: operations.pop(0)(num1, num2),
                number_list,
            )

            if result == sum_:
                sum_calibrated += sum_
                break

    return sum_calibrated


def part1(input_data):
    data = read_data(input_data)

    math_functions = [lambda x, y: x + y, lambda x, y: x * y]
    calibrated_sum = get_calibrated_sum(data, math_functions)

    return calibrated_sum


def part2(input_data):
    data = read_data(input_data)

    math_functions = [
        lambda x, y: x + y,
        lambda x, y: x * y,
        lambda x, y: int(str(x) + str(y)),
    ]

    calibrated_sum = get_calibrated_sum(data, math_functions)

    return calibrated_sum


def main():
    test_input = "data/day07/test_input.txt"
    input_data = "data/day07/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
