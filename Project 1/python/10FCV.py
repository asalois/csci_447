""" This is for performing 10-fold crossvalidation of the ML algorithm """
# This file brought to you by Ethan
import numpy
import random
import data_setup
import copy

''' We don't need a function to do just this, but we added one anyway '''
def randomizer(samples):
    return random.shuffle(samples)


'''
This function splits the dataset array into 10 roughly equal pieces to be
used as test sets in 10fold cross validation

The general concept for this function was aquired from
https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
'''
'''def splitter(samples):
    OG = copy.copy(samples)
    random.shuffle(samples)
    average_len = len(samples) / 10
    split_array = []
    start = 0
    while start < len(samples):
        split_array.append(seq[start:(start + average_len)])
        start += average_len

    return split_array'''

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
def get_list(input):
    base_data = data_setup.readInCom(input,'?')
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
        ''' for j in range(len(ls[i])):
            for k in range(len(ls[i][j])):
                print(ls[i][j][k])
        print('\n') '''


def work_it():
    og_data = get_list('5')
    new_data = numpy.asarray(og_data)       #<-this is messing up the array
#    new_data = randomizer(new_data)
    new_data = splitter(new_data)
    # print(new_data)
    # cross_validate(new_data) # does 10fold CV with the original dataset, no scrambled attributes
    array_printer(new_data)




work_it()