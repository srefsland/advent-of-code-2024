def read_data(path):
    with open(path, "r") as f:
        data = f.read()

    # Return array of lines
    return data.split("\n")


def print_data(data):
    for line in data:
        print(line)
