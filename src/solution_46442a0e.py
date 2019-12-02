from src import utils
import sys
import os

def solve(in_array):
    '''
    Given the input set, extend the size twice in both directions, with each new quadrant being a rotation of the input
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
            # other 3 quadrants are rotated
            prediction[x][opp_end-y] = val
            prediction[opp_end-y][opp_end-x] = val
            prediction[opp_end-x][y] = val

    return prediction


if __name__ == "__main__":
    training_data = utils.load_json_from_command_arg()
    utils.run_tests(training_data, solve)
