from utils.read_data import read_data

import numpy as np
from PIL import Image

import time


def read_pos_vel(data):
    robots = []

    for line in data:
        pos = list(map(int, line.split(" ")[0].split("=")[1].split(",")))
        vel = list(map(int, line.split(" ")[1].split("=")[1].split(",")))

        robots.append(
            {"pos": {"x": pos[0], "y": pos[1]}, "vel": {"x": vel[0], "y": vel[1]}}
        )

    return robots


def correct_position(pos_x, pos_y, width, height):
    return pos_x % width, pos_y % height


def calculate_entropy(bitmap):
    flat_bitmap = np.ravel(bitmap)
    _, counts = np.unique(flat_bitmap, return_counts=True)

    probabilities = counts / len(flat_bitmap)
    entropy = -np.sum(probabilities * np.log2(probabilities))

    return entropy


def part1(input_data, width, height):
    data = read_data(input_data)

    robots = read_pos_vel(data)
    final_positions = {}

    for robot in robots:
        pos_x, pos_y = robot["pos"]["x"], robot["pos"]["y"]
        vel_x, vel_y = robot["vel"]["x"], robot["vel"]["y"]

        for _ in range(100):
            pos_x += vel_x
            pos_y += vel_y

            pos_x, pos_y = correct_position(pos_x, pos_y, width, height)

        final_positions[(pos_y, pos_x)] = final_positions.get((pos_y, pos_x), 0) + 1

    quadrants = {}

    for pos, num_robots in final_positions.items():
        if pos[0] < height // 2 and pos[1] < width // 2:
            quadrants["1"] = quadrants.get("1", 0) + num_robots
        elif pos[0] < height // 2 and pos[1] > width // 2:
            quadrants["2"] = quadrants.get("2", 0) + num_robots
        elif pos[0] > height // 2 and pos[1] < width // 2:
            quadrants["3"] = quadrants.get("3", 0) + num_robots
        elif pos[0] > height // 2 and pos[1] > width // 2:
            quadrants["4"] = quadrants.get("4", 0) + num_robots

    safety_factor = 1

    for num_robots in quadrants.values():
        safety_factor *= num_robots

    return safety_factor


def part2(input_data, width, height):
    data = read_data(input_data)

    robots = read_pos_vel(data)

    lowest_entropy = 1
    lowest_second = 0

    for second in range(width * height):
        bitmap = np.array(
            [[0 for _ in range(width)] for _ in range(height)], dtype=np.uint8
        )

        for i in range(len(robots)):
            pos_x, pos_y = robots[i]["pos"]["x"], robots[i]["pos"]["y"]
            vel_x, vel_y = robots[i]["vel"]["x"], robots[i]["vel"]["y"]

            pos_x += vel_x
            pos_y += vel_y

            pos_x, pos_y = correct_position(pos_x, pos_y, width, height)

            robots[i]["pos"]["x"], robots[i]["pos"]["y"] = pos_x, pos_y

            bitmap[pos_y][pos_x] += 1

        # Could have used safety factor from part 1 instead in retrospect
        entropy = calculate_entropy(bitmap)

        if entropy < lowest_entropy:
            print(f"Second: {second + 1}")
            print(f"Entropy: {entropy}")
            lowest_entropy = entropy
            lowest_second = second
            bw_image = Image.fromarray(bitmap * 255, mode="L").convert("1")
            bw_image.save("second.png")
            time.sleep(1)

    print(f"Lowest entropy: {lowest_entropy}")
    print(f"Second: {lowest_second + 1}")


def main():
    test_input = "data/day14/test_input.txt"
    input_data = "data/day14/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input, width=11, height=7)}")
    print(f"Input part 1: {part1(input_data, width=101, height=103)}")
    part2(input_data, width=101, height=103)


if __name__ == "__main__":
    main()
