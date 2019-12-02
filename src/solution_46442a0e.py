from src import utils

def solve(in_array):
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


training_1 = {"train": [{"input": [[8, 6], [6, 8]], "output": [[8, 6, 6, 8], [6, 8, 8, 6], [6, 8, 8, 6], [8, 6, 6, 8]]}, {"input": [[7, 7, 8], [7, 7, 8], [8, 8, 8]], "output": [[7, 7, 8, 8, 7, 7], [7, 7, 8, 8, 7, 7], [8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8], [7, 7, 8, 8, 7, 7], [7, 7, 8, 8, 7, 7]]}, {"input": [[6, 9, 9], [6, 4, 4], [6, 4, 4]], "output": [[6, 9, 9, 6, 6, 6], [6, 4, 4, 4, 4, 9], [6, 4, 4, 4, 4, 9], [9, 4, 4, 4, 4, 6], [9, 4, 4, 4, 4, 6], [6, 6, 6, 9, 9, 6]]}], "test": [{"input": [[1, 4, 1], [4, 9, 4], [9, 1, 9]], "output": [[1, 4, 1, 9, 4, 1], [4, 9, 4, 1, 9, 4], [9, 1, 9, 9, 4, 1], [1, 4, 9, 9, 1, 9], [4, 9, 1, 4, 9, 4], [1, 4, 9, 1, 4, 1]]}]}

utils.run_tests(training_1, solve)
