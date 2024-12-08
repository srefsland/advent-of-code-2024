from utils.bounds import out_of_bounds
from utils.read_data import read_data


def find_stations(data):
    found_stations = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            location = data[i][j]
            if location != ".":
                found_stations[location] = found_stations.get(location, []) + [(i, j)]

    return found_stations


def part1(input_data):
    data = read_data(input_data)

    found_stations = find_stations(data)
    antinode_locations = set()

    for locations in found_stations.values():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                deltaX = locations[j][0] - locations[i][0]
                deltaY = locations[j][1] - locations[i][1]

                antinode1 = locations[i][0] - deltaX, locations[i][1] - deltaY
                antinode2 = locations[j][0] + deltaX, locations[j][1] + deltaY

                if not out_of_bounds(data, antinode1):
                    antinode_locations.add(antinode1)

                if not out_of_bounds(data, antinode2):
                    antinode_locations.add(antinode2)

    return len(antinode_locations)


def part2(input_data):
    data = read_data(input_data)

    found_station = find_stations(data)
    antinode_locations = set()

    for locations in found_station.values():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                deltaX = locations[j][0] - locations[i][0]
                deltaY = locations[j][1] - locations[i][1]

                antinode_locations.add(locations[i])
                antinode_locations.add(locations[j])
                antinode1 = locations[i][0] - deltaX, locations[i][1] - deltaY
                antinode2 = locations[j][0] + deltaX, locations[j][1] + deltaY

                while not out_of_bounds(data, antinode1):
                    antinode_locations.add(antinode1)
                    antinode1 = antinode1[0] - deltaX, antinode1[1] - deltaY

                while not out_of_bounds(data, antinode2):
                    antinode_locations.add(antinode2)
                    antinode2 = antinode2[0] + deltaX, antinode2[1] + deltaY
                    
    return len(antinode_locations)


def main():
    test_input = "data/day08/test_input.txt"
    input_data = "data/day08/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
