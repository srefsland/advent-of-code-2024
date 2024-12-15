from utils.read_data import read_data
from utils.bounds import out_of_bounds

directions = [
    lambda i, j: (i - 1, j),  # North
    lambda i, j: (i + 1, j),  # South
    lambda i, j: (i, j + 1),  # East
    lambda i, j: (i, j - 1),  # West
]


def expand(data, i, j):
    if out_of_bounds(data, (i, j)):
        return

    new_positions = []
    current_height = int(data[i][j])

    for direction in directions:
        new_position = direction(i, j)

        if not out_of_bounds(data, new_position):
            next_height = int(data[new_position[0]][new_position[1]])

            if next_height - current_height == 1:
                new_positions.append(direction(i, j))

    return new_positions


def find_trailheads_and_endpoints(data):
    trailheads = []
    endpoints = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "0":
                trailheads.append((i, j))
            elif data[i][j] == "9":
                endpoints.append((i, j))

    return trailheads, endpoints


def find_trailhead_scores(data, use_rating=False):
    trailheads, endpoints = find_trailheads_and_endpoints(data)

    sum_trailhead_scores = 0

    for trailhead in trailheads:
        positions_to_visit = [trailhead]
        endpoints_visited = []

        while positions_to_visit:
            i, j = positions_to_visit.pop()

            if (i, j) in endpoints:
                endpoints_visited.append((i, j))

            new_positions = expand(data, i, j)

            if new_positions:
                positions_to_visit.extend(new_positions)

        endpoints_visited = (
            set(endpoints_visited) if not use_rating else endpoints_visited
        )
        sum_trailhead_scores += len(endpoints_visited)

    return sum_trailhead_scores


def part1(input_data):
    data = read_data(input_data)
    sum_trailhead_scores = find_trailhead_scores(data)

    return sum_trailhead_scores


def part2(input_data):
    data = read_data(input_data)
    sum_trailhead_scores = find_trailhead_scores(data, use_rating=True)

    return sum_trailhead_scores


def main():
    test_input = "data/day10/test_input.txt"
    input_data = "data/day10/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
