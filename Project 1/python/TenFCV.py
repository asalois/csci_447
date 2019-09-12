""" This is for performing 10-fold crossvalidation of the ML algorithm """
# This file brought to you by Ethan
import numpy
import random
import data_setup
import copy
import naive_bayes as nb

''' 
Takes a dataset, scrambles the values of 10% (rounded up) of the rows 
This feeds directly into the 10-fold cross-validation function for our second run of the learner
'''
def ten_percent_scrambler(samples):
    scrambled = []
    for i in range(int(numpy.ceil(len(samples)/10))): # takes the first 10% of the array (rounded up), scrambles data row by row, ignoring the class attribute
        temp = samples[i][:-1]
        random.shuffle(temp)
        samples[i][:-1] = temp
    return samples # returns list otherwise unharmed to be scrambled by the cross-validation function

'''
Splits the input list into 10 (mostly) equal-sized sublists to be fed into the 10-fold cross-validation function
also scrambles the list before splitting
'''
def splitter(samples):
    samples = numpy.asarray(samples) # temporarily converts the list to a numpy array so it can be run through the splitter
    OG = copy.copy(samples)
    random.shuffle(samples) # Scrambles the order of all rows in the sample array
    samples = numpy.array_split(samples, 10) # Splits the input array of samples into a list of 10 subarrays. Why does the function return a list when the input was an array? no idea, but it makes my job easier
    # print(type(samples))
    # array_printer(samples)
    return samples


'''
This doesn't need its own function, but we're lazy people here at 'Team'
Calls the data read function from data_setup.py
'''
def get_list(input, chara):
    base_data = data_setup.readInCom(input, chara)
    return base_data


''' Removes the class attribute from the input portion of the dataset to be used for validation of the model'''
def make_test_set(input):
    #to_return = [len(input)]
    if type(input) == numpy.ndarray:
        input = numpy.ndarray.tolist(input) # ensures that the soon-to-be test set is a basic python list so we can remove the class attribute with del
    for i in input:
        del i[-1]
    return input


def cross_validate(dataset, scramBool):
    backup_data = copy.copy(dataset)
    test_results = []
    if scramBool:
        dataset = ten_percent_scrambler(dataset)
    dataset = splitter(dataset)
    for i in range(10): # iterates through passing each of the 10 subsets of our now scrambled and split dataset
        to_learn = copy.copy(dataset) # Grabs a fresh copy of the dataset each time, since the to_learn list pops deletes a tenth of the data in each loop
        to_test = make_test_set(to_learn.pop(i))
        to_learn = flatten_list(to_learn)
        # print('tester')
        array_printer_2d(to_test)
        # print('learner')
        nb.train(to_learn)
        array_printer_3d(nb.freqTable)
        array_printer_2d(to_learn)
        # print(len(to_learn))
        # learn(temp) # this will call the learner algo
        # test_results.append(test(to_test, dataset[i])) # This tests our model with the current tenth of the dataset

'''
Efficiency is overrated, so I implemented this function to do what could instead be done with an 'if' statement
'''
def tenP_scrambled_cv(dataset):
    dataset = ten_percent_scrambler(dataset)
    cross_validate(dataset, True)

'''
This removes a dimension from an input list. This is used before sending data into Naive Bayes so the algorithm 
can read from a continuous 2d list, as opposed to the list of 2d lists created by the splitter() function
'''
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
    data = get_list('3', '?')
    unscrambled_data = copy.copy(data)
    # new_data = numpy.asarray(og_data)      This converts the list to an array so it can be properly
    # new_data = randomizer(new_data)
    # new_data = splitter(og_data)
    # print(new_data)
    # cross_validate(unscrambled_data, False) # does 10fold CV with the original dataset, no scrambled attributes
    tenP_scrambled_cv(unscrambled_data) # Does 10fold cv with 10% (rounded up) of the data scrambled within its row



work_it()