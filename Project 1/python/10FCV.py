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
    OG = copy.copy(samples)
    random.shuffle(samples)
    samples = numpy.array_split(samples, 10)
    array_printer(samples)
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
    for i in range(len(input)):
        del input[i][len(input[i])-1]


''' Takes 10% of the columns in the dataset, and scrambles them '''
def single_column_scramble(input):
    total_cols = len(input[0]) - 1 # Total columns, minus the class attribute
    num_to_scramble = numpy.ceil(total_cols * 0.1) # Takes 10% of the columns, rounded up


def cross_validate(dataset):
    #backup = copy.copy(dataset)
    for i in range(10):
        temp = copy.copy(dataset)
        to_test = make_test_set(dataset[i])
        del temp[i]
        learn(temp) # this will call the learner algo
        test(to_test, dataset[i]) # This tests our model with previously known classes



def array_printer(ls):
    for i in ls:
        for j in i:
            print(j)
            #for k in j:
                # print(k)


def work_it():
    og_data = get_list('5', '?')
    new_data = numpy.asarray(og_data)       #<-this is messing up the array
#    new_data = randomizer(new_data)
    new_data = splitter(new_data)
    # print(new_data)
    # cross_validate(new_data) # does 10fold CV with the original dataset, no scrambled attributes
    array_printer(new_data)




work_it()