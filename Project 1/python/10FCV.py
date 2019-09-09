""" This is for performing 10-fold crossvalidation of the ML algorithm """
# This file brought to you by Ethan

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
def splitter(samples):
    OG = samples
    shuf_samples = random.shuffle(samples)
    average_len = len(samples) / 10
    split_array = []
    start = 0
    while start < len(shuf_samples):
        split_array.append(seq[first:(first + average_len)])
        start += average_len

    return split_array


'''
This also doesn't need its own function, but we're lazy people
Calls the data read function from data_setup.py
'''
def get_list(input):
    base_data = data_setup.readInCom(input)
    return base_data


def list_printer(ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            print(ls[i][j])


def work_it():
    og_data = get_list(1)
    new_data = copy.copy(og_data)
    new_data = randomizer(new_data)
    new_data = splitter(new_data)
    list_printer(new_data)