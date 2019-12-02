import numpy as np
import sys
import os
import json


def load_json_from_command_arg():
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
    training_set['train'].extend(training_set['test'])
    for case in training_set['train']:
        input = case['input']
        output = case['output']

        prediction = solving_function(input)

        if prediction == output:
            print("INPUT:")
            print(np.matrix(input))
            print("OUTPUT/SOLUTION:")
            print(np.matrix(prediction))
            print("Test passed.\n")
        else:
            print("ERROR: TEST FAILED")
