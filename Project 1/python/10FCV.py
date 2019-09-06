""" This is for performing 10-fold crossvalidation of the ML algorithm """
import random


def randomizer(samples):



''' This function splits the dataset array into 10 roughly equal pieces to be
used as test sets in 10fold cross validation '''

'''how to do this step was aquired form https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length'''
def splitter(samples):
    OG = samples
    shuf_samples = random.shuffle(samples)
    average_len = len(samples) / 10
    split_array = []
    start = 0
    while start < len(shuf_samples)
        split_array.append(seq[first:(first + average_len)])
        