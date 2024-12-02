from utils.read_data import read_data


def check_safety_report(report):
    differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]

    # Must be strictly decreasing or increasing
    is_monotonic = all(difference > 0 for difference in differences) or all(
        difference < 0 for difference in differences
    )
    is_correct_rate = all(
        abs(difference) >= 1 and abs(difference) <= 3 for difference in differences
    )

    return is_monotonic and is_correct_rate


def check_safety_reports_remove_one(report):
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)

        if check_safety_report(new_report):
            return True


def part1(input_data):
    data = read_data(input_data)

    num_safe_reports = 0

    for line in data:
        report = list(map(int, line.split()))

        if check_safety_report(report):
            num_safe_reports += 1

    return num_safe_reports


def part2(input_data):
    data = read_data(input_data)

    num_safe_reports = 0

    for line in data:
        report = list(map(int, line.split()))

        if check_safety_report(report) or check_safety_reports_remove_one(report):
            num_safe_reports += 1

    return num_safe_reports


def main():
    test_input = "data/day02/test_input.txt"
    input_data = "data/day02/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
