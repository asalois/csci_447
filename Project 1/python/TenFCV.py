""" This is for performing 10-fold crossvalidation of the ML algorithm """
# This file brought to you by Ethan
import numpy
import random
import data_setup
import copy

''' We don't need a function to do just this, but we added one anyway '''
def randomizer(samples):
    return random.shuffle(samples)


def splitter(samples):
    samples = numpy.asarray(samples) # temporarily converts the list to a numpy array so it can be run through the splitter
    OG = copy.copy(samples)
    random.shuffle(samples) # Scrambles the order of all rows in the sample array
    samples = numpy.array_split(samples, 10) # Splits the input array of samples into a list of 10 subarrays. Why does the function return a list when the input was an array? no idea, but it makes my job easier
    # print(type(samples))
    # array_printer(samples)
    return samples


'''
This also doesn't need its own function, but we're lazy people
Calls the data read function from data_setup.py
'''
def get_list(input, chara):
    base_data = data_setup.readInCom(input, chara)
    return base_data


''' Removes the class attribute from the input portion of the dataset to be used for validation of the model'''
def make_test_set(input):
    #to_return = [len(input)]
    input = numpy.ndarray.tolist(input) # ensures that the soon-to-be test set is a basic python list so we can remove the class attribute with del
    for i in input:
        del i[-1]
    return input


''' Takes 10% of the columns in the dataset, and scrambles them '''
def single_column_scramble(input):
    total_cols = len(input[0]) - 1 # Total columns, minus the class attribute
    num_to_scramble = numpy.ceil(total_cols * 0.1) # Takes 10% of the columns, rounded up



def cross_validate(dataset):
    to_compare = []
    for i in range(10):
        to_learn = copy.copy(dataset)
        to_test = make_test_set(to_learn.pop(i))
        to_learn = flatten_list(to_learn)
        print('tester')
        array_printer_2d(to_test)
        print('learner')
        array_printer_2d(to_learn)
        print(len(to_learn))
        # learn(temp) # this will call the learner algo
        # test(to_test, dataset[i]) # This tests our model with previously known classes


def flatten_list(three_dim_list):
    flattened = []
    for two_dim_list in three_dim_list:
        for list in two_dim_list:
            flattened.append(list)
            # print(list)
    return flattened




def array_printer_3d(ls):
    for i in ls:
        for j in i:
            print(j)
            #for k in j:
                # print(k)

def array_printer_2d(ls):
    for i in ls:
        print(i)


def work_it():
    og_data = get_list('3', '?')
    #new_data = numpy.asarray(og_data)      This converts the list to an array so it can be properly
#    new_data = randomizer(new_data)
    new_data = splitter(og_data)
    # print(new_data)
    cross_validate(new_data) # does 10fold CV with the original dataset, no scrambled attributes
    # array_printer(new_data)




work_it()