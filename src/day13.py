from utils.read_data import read_data
import re

BUTTON_A_COST = 3
BUTTON_B_COST = 1


def read_machine_data(data):
    machines = []
    num_pattern = r"\b\d+\b"

    machines_temp = [group.splitlines() for group in "\n".join(data).split("\n\n")]

    for machine in machines_temp:
        button_a, button_b, prize = machine
        machines.append(
            {
                "button_a": list(map(int, re.findall(num_pattern, button_a))),
                "button_b": list(map(int, re.findall(num_pattern, button_b))),
                "prize": list(map(int, re.findall(num_pattern, prize))),
            }
        )

    return machines


def solve_system_of_equations(machine):
    button_a_x, button_a_y = machine["button_a"]
    button_b_x, button_b_y = machine["button_b"]
    prize_x, prize_y = machine["prize"]

    # Systems of two equations solve for times to press button A and B
    button_presses_b = (prize_y * button_a_x - button_a_y * prize_x) / (
        button_b_y * button_a_x - button_b_x * button_a_y
    )
    button_presses_a = (prize_x - button_b_x * button_presses_b) / button_a_x

    return button_presses_a, button_presses_b


def part1(input_data):
    data = read_data(input_data)

    machines = read_machine_data(data)
    minimum_cost = 0

    for machine in machines:
        button_presses_a, button_presses_b = solve_system_of_equations(machine)

        buttons_within_range = (
            0 <= button_presses_a <= 100 and 0 <= button_presses_b <= 100
        )

        buttons_integer = (
            button_presses_a.is_integer() and button_presses_b.is_integer()
        )

        if buttons_within_range and buttons_integer:
            minimum_cost += (
                button_presses_a * BUTTON_A_COST + button_presses_b * BUTTON_B_COST
            )

    return int(minimum_cost)


def part2(input_data):
    data = read_data(input_data)

    machines = read_machine_data(data)
    minimum_cost = 0

    for machine in machines:
        machine["prize"] = list(map(lambda x: x + 10000000000000, machine["prize"]))

        button_presses_a, button_presses_b = solve_system_of_equations(machine)

        buttons_within_range = 0 <= button_presses_a and 0 <= button_presses_b
        buttons_integer = (
            button_presses_a.is_integer() and button_presses_b.is_integer()
        )

        if buttons_within_range and buttons_integer:
            minimum_cost += (
                button_presses_a * BUTTON_A_COST + button_presses_b * BUTTON_B_COST
            )

    return int(minimum_cost)


def main():
    test_input = "data/day13/test_input.txt"
    input_data = "data/day13/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
