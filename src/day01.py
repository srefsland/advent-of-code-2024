from utils.read_data import read_data


def part1(input_data):
    data = read_data(input_data)

    left_list, right_list = map(sorted, zip(*(map(int, line.split()) for line in data)))
    sum_differences = sum(abs(x - y) for x, y in zip(left_list, right_list))

    return sum_differences


def part2(input_data):
    data = read_data(input_data)

    left_list, right_list = zip(*(map(int, line.split()) for line in data))
    sim_score = sum(
        left_entry * right_list.count(left_entry) for left_entry in left_list
    )

    return sim_score


def main():
    test_input = "data/day01/test_input_part1.txt"
    input_data = "data/day01/input_part1.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
