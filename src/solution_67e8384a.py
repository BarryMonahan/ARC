from src import utils


def solve(in_array):
    '''
    Similar to Training 1, but where new quadrants are flips of the original array rather than rotations
    :param in_array: input array
    :return: expected output array
    '''
    array_edgelength = len(in_array[0])   # input array edge length
    opp_end = array_edgelength*2-1    # used for getting opposite end of array
    prediction = [[-1]*array_edgelength*2 for i in range(array_edgelength*2)]  # init 2d array

    # iterate through all values
    for y in range(len(in_array)):
        for x in range(len(in_array[0])):
            val = in_array[y][x]

            prediction[y][x] = val
            # other 3 quadrants are flips
            prediction[y][opp_end-x] = val
            prediction[opp_end-y][opp_end-x] = val
            prediction[opp_end-y][x] = val

    return prediction


if __name__ == "__main__":
    training_data = utils.load_json_from_command_arg()
    utils.run_tests(training_data, solve)
