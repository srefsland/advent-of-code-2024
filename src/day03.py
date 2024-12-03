from utils.read_data import read_data

import re


def part1(input_data):
    data = read_data(input_data)

    multiply_regex = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(multiply_regex, "".join(data))

    sum_multiplications = sum(int(match[0]) * int(match[1]) for match in matches)

    return sum_multiplications


def part2(input_data):
    data = read_data(input_data)

    multiply_do_dont_regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don't\(\))"

    matches = re.findall(multiply_do_dont_regex, "".join(data))

    do_enabled = True
    sum_multiplications = 0

    for match in matches:
        if match[-1] == "don't()":
            do_enabled = False
        elif match[-1] == "do()":
            do_enabled = True
        elif do_enabled:
            sum_multiplications += int(match[0]) * int(match[1])
            
    return sum_multiplications


def main():
    test_input = "data/day03/test_input.txt"
    input_data = "data/day03/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
