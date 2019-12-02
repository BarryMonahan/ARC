from src import utils

def solve(in_array):
    """
    Given an input data of numbers changing either horizontally or vertically,
    make a matching horizontal or vertical array with redundancies removed
    :param in_array: input array
    :return: expected output array
    """
    listed_numbers = []
    prediction = []

    # iterate through all values
    for y in range(len(in_array)):
        prediction_line = []
        for x in range(len(in_array[0])):
            val = in_array[y][x]
            if val not in listed_numbers:
                listed_numbers.append(val)
                prediction_line.append(val)
        if prediction_line:     # is not empty
            prediction.append(prediction_line)

    # the alternative solution is to look through only 1 horizontal line and 1 vertical line
    # and make an array to match. Either approach would work.

    return prediction


if __name__ == "__main__":
    training_data = utils.load_json_from_command_arg()
    utils.run_tests(training_data, solve)
