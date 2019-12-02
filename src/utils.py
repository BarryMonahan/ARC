import numpy as np
import sys
import os
import json


def load_json_from_command_arg():
    """
    Reads the json training file, specified in the command line, into a Python dictionary
    :return: dictionary of training data
    """
    if len(sys.argv) < 2:
        print("ERROR: script requires the path to the training data as an argument - eg: data/training/46442a0e.json")
        sys.exit(-1)
    training_data_path = sys.argv[1]
    if not os.path.isfile(training_data_path):
        print("ERROR: training data argument is not an existing file.")
        sys.exit(-2)

    with open(training_data_path) as json_file:
        return json.load(json_file)


def run_tests(training_set, solving_function):
    """
    Shared testing function for all tests.
    :param training_set: .json file
    :param solving_function: function to do the test for
    :return: None
    """
    training_set['train'].extend(training_set['test'])
    for case in training_set['train']:
        training_input = case['input']
        training_output = case['output']

        prediction = solving_function(training_input)

        # not entirely clear what output is expected here. Assignment doesn't specify to print the Input grid,
        # but it'd make more sense that it does.
        if prediction == training_output:
            print("\nINPUT:")
            print(np.matrix(training_input))
            print("OUTPUT:")
            print(np.matrix(prediction))
        else:
            print("\nINPUT:")
            print(np.matrix(training_input))
            print("TRAINING OUTPUT:")
            print(np.matrix(training_output))
            print("SOLUTION'S OUTPUT:")
            print(np.matrix(prediction))
            print("ERROR: TEST FAILED")
