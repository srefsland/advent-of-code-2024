from utils.read_data import read_data
from functools import cmp_to_key


def find_correct_incorrect_updates(input_data):
    data = read_data(input_data)
    index = data.index("")

    rules = {}

    for rule in data[:index]:
        k, v = list(map(int, rule.split("|")))
        rules[k] = rules.get(k, []) + [v]

    page_updates = [list(map(int, pages.split(","))) for pages in data[index + 1 :]]

    def page_comparator_function(entry1, entry2):
        return -1 if entry2 in rules.get(entry1, []) else 0

    ordered_page_updates = [
        sorted(pages, key=cmp_to_key(page_comparator_function))
        for pages in page_updates
    ]

    return page_updates, ordered_page_updates


def part1(input_data):
    page_updates, correctly_ordered_updates = find_correct_incorrect_updates(input_data)

    correctly_ordered_updates = [
        page_updates[i]
        for i in range(len(page_updates))
        if page_updates[i] == correctly_ordered_updates[i]
    ]

    sum_middle = sum(
        correct_update[len(correct_update) // 2]
        for correct_update in correctly_ordered_updates
    )

    return sum_middle


def part2(input_data):
    page_updates, correctly_ordered_updates = find_correct_incorrect_updates(input_data)

    incorrectly_ordered_updates = [
        correctly_ordered_updates[i]
        for i in range(len(page_updates))
        if correctly_ordered_updates[i] != page_updates[i]
    ]

    sum_middle = sum(
        incorrect_update[len(incorrect_update) // 2]
        for incorrect_update in incorrectly_ordered_updates
    )

    return sum_middle


def main():
    test_input = "data/day05/test_input.txt"
    input_data = "data/day05/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
