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


training_3 = {"test": [{"input": [[1, 6, 6], [5, 2, 2], [2, 2, 2]], "output": [[1, 6, 6, 6, 6, 1], [5, 2, 2, 2, 2, 5], [2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2], [5, 2, 2, 2, 2, 5], [1, 6, 6, 6, 6, 1]]}], "train": [{"input": [[5, 3, 4], [3, 4, 5], [3, 4, 4]], "output": [[5, 3, 4, 4, 3, 5], [3, 4, 5, 5, 4, 3], [3, 4, 4, 4, 4, 3], [3, 4, 4, 4, 4, 3], [3, 4, 5, 5, 4, 3], [5, 3, 4, 4, 3, 5]]}, {"input": [[7, 1, 5], [7, 7, 1], [5, 3, 1]], "output": [[7, 1, 5, 5, 1, 7], [7, 7, 1, 1, 7, 7], [5, 3, 1, 1, 3, 5], [5, 3, 1, 1, 3, 5], [7, 7, 1, 1, 7, 7], [7, 1, 5, 5, 1, 7]]}, {"input": [[2, 5, 2], [2, 6, 4], [2, 2, 2]], "output": [[2, 5, 2, 2, 5, 2], [2, 6, 4, 4, 6, 2], [2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2], [2, 6, 4, 4, 6, 2], [2, 5, 2, 2, 5, 2]]}, {"input": [[1, 2, 1], [2, 8, 1], [8, 1, 6]], "output": [[1, 2, 1, 1, 2, 1], [2, 8, 1, 1, 8, 2], [8, 1, 6, 6, 1, 8], [8, 1, 6, 6, 1, 8], [2, 8, 1, 1, 8, 2], [1, 2, 1, 1, 2, 1]]}]}

utils.run_tests(training_3, solve)