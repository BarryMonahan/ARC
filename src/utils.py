def run_tests(training_set, solving_function):
    training_set['train'].extend(training_set['test'])
    for case in training_set['train']:
        input = case['input']
        output = case['output']

        prediction = solving_function(input)

        if prediction == output:
            print("Test passed.")
        else:
            print("ERROR: TEST FAILED")
