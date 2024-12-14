from utils.read_data import read_data


def compute_checksum(file_blocks):
    checksum = 0
    not_free_indices = [i for i, x in enumerate(file_blocks) if x != "."]
    for i in not_free_indices:
        checksum += int(file_blocks[i]) * i

    return checksum


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def init_file_blocks(data):
    file_blocks = []
    file_id_indices = []
    free_space_indices = []
    id_ = 0

    for i, num in enumerate(data):
        if int(num) > 0:
            if i % 2 == 0:
                file_id_indices.append(
                    [i for i in range(len(file_blocks), len(file_blocks) + int(num))]
                )
                file_blocks.extend([str(id_) for _ in range(int(num)) if int(num) > 0])
                id_ += 1
            else:
                free_space_indices.append(
                    [i for i in range(len(file_blocks), len(file_blocks) + int(num))]
                )
                file_blocks.extend(["." for _ in range(int(num))])

    return file_blocks, file_id_indices, free_space_indices


def part1(input_data):
    data = read_data(input_data)[0]

    file_blocks, file_id_indices, free_space_indices = init_file_blocks(data)

    free_indices = [i for sublist in free_space_indices for i in sublist]
    file_indices = [i for sublist in file_id_indices for i in sublist]

    while free_indices[0] < file_indices[-1]:
        num_index = file_indices.pop()
        free_index = free_indices.pop(0)

        swap(file_blocks, num_index, free_index)

    checksum = compute_checksum(file_blocks)

    return checksum


def part2(input_data):
    data = read_data(input_data)[0]

    file_blocks, file_id_indices, free_space_indices = init_file_blocks(data)

    while file_id_indices:
        file_id_indice = file_id_indices.pop()

        i = 0
        swapped = False

        while (
            i < len(free_space_indices)
            and free_space_indices[i][-1] < file_id_indice[0]
            and not swapped
        ):
            free_space_indice = free_space_indices[i]

            if len(free_space_indice) >= len(file_id_indice):
                swapped = True

                for j in range(len(file_id_indice)):
                    swap(file_blocks, free_space_indice[j], file_id_indice[j])

                free_space_indices[i] = free_space_indices[i][len(file_id_indice) :]

                if len(free_space_indices[i]) == 0:
                    free_space_indices.pop(i)

            i += 1

    checksum = compute_checksum(file_blocks)

    return checksum


def main():
    test_input = "data/day09/test_input.txt"
    input_data = "data/day09/input.txt"

    # Tests
    print(f"Test input part 1: {part1(test_input)}")
    print(f"Input part 1: {part1(input_data)}")
    print(f"Test input part 2: {part2(test_input)}")
    print(f"Input part 2: {part2(input_data)}")


if __name__ == "__main__":
    main()
