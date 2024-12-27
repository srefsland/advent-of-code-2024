from utils.read_data import read_data

stone_lookup_table = {}


def blink(stone, num_blinks):
    if num_blinks == 0:
        return 1

    if (stone, num_blinks) in stone_lookup_table:
        # Use lookup table to avoid recalculating the same stone given the same number of blinks
        return stone_lookup_table[(stone, num_blinks)]

    if stone == 0:
        new_stone = 1
        num_stones = blink(new_stone, num_blinks - 1)
    elif len(str(stone)) % 2 == 0:
        left_stone = int(str(stone)[: len(str(stone)) // 2])
        right_stone = int(str(stone)[len(str(stone)) // 2 :])

        num_stones = blink(left_stone, num_blinks - 1) + blink(
            right_stone, num_blinks - 1
        )
    else:
        new_stone = stone * 2024

        num_stones = blink(new_stone, num_blinks - 1)

    if (stone, num_blinks) not in stone_lookup_table:
        stone_lookup_table[(stone, num_blinks)] = num_stones

    return num_stones


def part1(input_data):
    data = read_data(input_data)
    stones = map(int, data[0].split())

    num_blinks = 25

    return sum([blink(stone, num_blinks) for stone in stones])


def part2(input_data):
    data = read_data(input_data)
    stones = map(int, data[0].split())

    num_blinks = 75

    return sum([blink(stone, num_blinks) for stone in stones])


def main():
    test_input = "data/day11/test_input.txt"
    input_data = "data/day11/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
