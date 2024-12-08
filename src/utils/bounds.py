def out_of_bounds(data, position):
    i, j = position
    return i < 0 or j < 0 or i >= len(data) or j >= len(data[i])
