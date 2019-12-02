from src import utils


def solve(in_array):
    '''
    This set matches up the three-point triangles present in the image into a 4-4 grid,
    with the triangles in the corners, so that the center is empty
    :param in_array: input array
    :return: expected output array
    '''
    prediction = list()
    corners = [-1,-1,-1,-1]     # top-left, top-right, bottom-left, bottom-right values

    # iterate through all values
    for y in range(len(in_array)):
        for x in range(len(in_array[0])):
            if in_array[y][x] != 0:
                # check that it has two neighbours
                if (in_array[y - 1][x] != 0 or in_array[y + 1][x] != 0) \
                        and (in_array[y][x - 1] != 0 or in_array[y][x + 1] != 0):
                    # determine which corner it belongs to:
                    corner = 0
                    if in_array[y - 1][x] != 0:
                        corner += 2  # is on the bottom
                    if in_array[y][x - 1] != 0:
                        corner += 1  # is on the right
                    corners[corner] = in_array[y][x]

    prediction = [[corners[0], corners[0], corners[1], corners[1]],
                  [corners[0], 0, 0, corners[1]],
                  [corners[2], 0, 0, corners[3]],
                  [corners[2], corners[2], corners[3], corners[3]]]

    return prediction


if __name__ == "__main__":
    training_data = utils.load_json_from_command_arg()
    utils.run_tests(training_data, solve)
