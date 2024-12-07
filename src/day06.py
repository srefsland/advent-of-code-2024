import pickle
from enum import Enum

from utils.read_data import read_data


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"


DIRECTIONS = [direction for direction in Direction]


def get_next_position(current_position, current_direction):
    i, j = current_position
    if current_direction == Direction.UP:
        return (i - 1, j)
    elif current_direction == Direction.RIGHT:
        return (i, j + 1)
    elif current_direction == Direction.DOWN:
        return (i + 1, j)
    elif current_direction == Direction.LEFT:
        return (i, j - 1)


def get_next_direction(current_direction):
    current_index = DIRECTIONS.index(current_direction)
    return DIRECTIONS[(current_index + 1) % len(DIRECTIONS)]


def out_of_bounds(data, position):
    i, j = position
    return i < 0 or j < 0 or i >= len(data) or j >= len(data[i])


def find_starting_point(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in [d.value for d in DIRECTIONS]:
                start_direction = Direction(data[i][j])
                start_position = (i, j)

    return start_position, start_direction


def get_next_clear_position_direction(data, current_position, current_direction):
    is_next_clear = False

    while not is_next_clear:
        next_position = get_next_position(current_position, current_direction)

        if out_of_bounds(data, next_position):
            current_position = None
            is_next_clear = True
        else:
            if data[next_position[0]][next_position[1]] == "#":
                current_direction = get_next_direction(current_direction)
            else:
                current_position = next_position
                is_next_clear = True

    return current_position, current_direction


def get_visited_positions(data):
    visited_positions = set()
    current_position, current_direction = find_starting_point(data)

    is_out_of_bounds = False

    while not is_out_of_bounds:
        visited_positions.add(current_position)

        current_position, current_direction = get_next_clear_position_direction(
            data, current_position, current_direction
        )

        if current_position is None:
            is_out_of_bounds = True

    return visited_positions


def does_create_guard_loop(data, start_position, start_direction):
    is_out_of_bounds = False
    current_position, current_direction = start_position, start_direction
    position_direction_history = set()

    while not is_out_of_bounds:
        current_position, current_direction = get_next_clear_position_direction(
            data, current_position, current_direction
        )

        if current_position is None:
            is_out_of_bounds = True
        elif (current_position, current_direction) in position_direction_history:
            return True

        position_direction_history.add((current_position, current_direction))

    return False


def part1(input_data):
    data = read_data(input_data)
    visited_positions = get_visited_positions(data)

    return len(visited_positions)


def part2(input_data):
    data = read_data(input_data)

    start_position, start_direction = find_starting_point(data)
    visited_positions = get_visited_positions(data)

    num_loop_creating_obstacles = 0

    for position in visited_positions:
        data_copy = [list(row) for row in data]
        i, j = position
        data_copy[i][j] = "#"

        if does_create_guard_loop(data_copy, start_position, start_direction):
            num_loop_creating_obstacles += 1

    return num_loop_creating_obstacles


def main():
    test_input = "data/day06/test_input.txt"
    input_data = "data/day06/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
