'''
This file performs all non-instanced functions within the code, i.e. performing tenfold 
cross validation of our model on each dataset, instancing maps for each dataset,
running statistical analysis on runs from each model, and so on
'''
import sys
import numpy as np
import random as rd
import data_setup  # This package is a set of code we are reusing from project 1, such as data setup and stat analysis, with modifications as needed
import copy
from POINTMAP import point_map
from KNN import k_nearest_neighbors
from EKNN import edited_knn
from PAM import pam
import STATANALYSIS as sa
from CKNN import condensed_knn
from CMEANS import c_means


'''
Splits the input list into 10 (mostly) equal-sized sublists to be fed into the 10-fold cross-validation function
also scrambles the list before splitting
'''
def splitter(samples):
    
    OG = copy.copy(samples)
    rd.shuffle(samples) # Scrambles the order of all rows in the sample array
    samples = np.asarray(samples) # temporarily converts the list to a numpy array so it can be run through the splitter
    samples = np.array_split(samples, 10) # Splits the input array of samples into a list of 10 subarrays. Why does the function return a list when the input was an array? no idea, but it makes my job easier
    # print(type(samples))
    # array_printer(samples)
    return samples


'''
This doesn't need its own function, but we're lazy people here at 'Team'
Calls the data read function from data_setup.py
'''
def get_list(input):
    if input == 6:
        partOne = data_setup.readInCom(input)
        partTwo = data_setup.readInCom(7)
        base_data = partOne + partTwo
    else:
        base_data = data_setup.readInCom(input)
    return base_data



''' Removes the class attribute from the input portion of the dataset to be used for validation of the model'''
def make_test_set(input):
    #to_return = [len(input)]
    if type(input) == np.ndarray:
        input = np.ndarray.tolist(input) # ensures that the soon-to-be test set is a basic python list so we can remove the class attribute with del
    for i in input:
        del i[-1]
    return input


'''This performs tenfold cross-validation on a given classification dataset, then performs statistical analysis on the results'''
def cross_validate_classify(dataset, variant, in_k):
    methods = {1: k_nearest_neighbors, 2: edited_knn, 3: condensed_knn, 4: c_means, 5: pam}
    # global num_classes
    backup_data = copy.copy(dataset)
    test_results = []
    stats = []
    full_set_stats = []
    backup_data = splitter(backup_data)
    algo = ''
    for i in range(10): # iterates through passing each of the 10 subsets of our now scrambled and split dataset
        p_map = ''
        to_learn = copy.copy(backup_data) # Grabs a fresh copy of the dataset each time, since the to_learn list deletes a tenth of the data in each loop
        to_test = make_test_set(to_learn.pop(i))
        to_learn = flatten_list(to_learn)
        algo = methods[variant](in_k,to_learn,0)
        # algo.generate()
        test_results = algo.classify(to_test)
        full_set_stats.append(test_results)
        analyze(backup_data[i],test_results,30)
       
    backup_data = flatten_list(backup_data)
    full_set_stats = flatten_list(full_set_stats)
    print("full set")
    analyze(backup_data, full_set_stats, 30)
    print('done!')
    #array_printer_3d(test_results)

'''This performs effectively the same thing as the classification cross-validation function, but instead for the regression sets'''
def cross_validate_regression(dataset, variant, in_k):
    methods = {1: k_nearest_neighbors, 2: edited_knn, 3: condensed_knn, 4: c_means, 5: pam}
    # global num_classes
    backup_data = copy.copy(dataset)
    test_results = []
    stats = []
    full_set_stats = []
    #backup_data = normalize_data(backup_data)
    backup_data = splitter(backup_data)
    algo = ''
    for i in range(10): # iterates through passing each of the 10 subsets of our now scrambled and split dataset
        p_map = ''
        to_learn = copy.copy(backup_data) # Grabs a fresh copy of the dataset each time, since the to_learn list deletes a tenth of the data in each loop
        to_test = make_test_set(to_learn.pop(i))
        to_learn = flatten_list(to_learn)
        algo = methods[variant](in_k,to_learn,1)
        # algo.generate()
        test_results = algo.regression(to_test)
        full_set_stats.append(test_results)
        print(sa.mse(backup_data[i],test_results))
        print(sa.abs_error(backup_data[i],test_results))
        
    backup_data = flatten_list(backup_data)
    full_set_stats = flatten_list(full_set_stats)
    print(sa.mse(backup_data,full_set_stats))
    print('done!')
    #array_printer_3d(test_results)


'''
This removes a dimension from an input three-dimensional (or greater) list. This is used before sending data into Naive Bayes so the algorithm 
can read from a continuous 2d list, as opposed to the list of 2d lists created by the splitter() function
'''
def flatten_list(three_dim_list):
    flattened = []
    for two_dim_list in three_dim_list: # the list being iterated through here is the one being removed
        for list in two_dim_list: # this list is appended to the 'flattened' list, thus removing a layer of lists
            flattened.append(list)
            # print(list)
    return flattened


'''Pretty simple function to make calls to our stat analysis functions. This is only used for classification sets'''
def analyze(dat_old, dat_learned, num_classes):
    confusion = sa.makeConfMatrix(dat_old, dat_learned, num_classes)
    # print(confusion)
    conf_with_totals = sa.totals(confusion)
    # print(conf_with_totals)
    stats = sa.calcError(conf_with_totals)
    print("Error:")
    print(stats[0])
    print("Precision:")
    print(stats[1])
    print("Recall:")
    print(stats[2])
    print("Correct classifications by class:")
    print(stats[3])
    print("Incorrect classifications by class")
    print(stats[4])
    #print(sa.clacError(conf_with_totals))




def retrieve_data(set_number):
    return data_setup.readInCom(set_number)


'''Primarily used for debugging. Runs one set on one algorithm with a user-defined k from command line args'''
def work_it():
    # global num_classes
    # sets = ['1','2','3','4','5'] # List of sets for easy iteration when running tests.
    # methods = {'1': k_nearest_neighbors, '2': edited_knn, '3': "put cknn here", '4': "put cmeans here", '5': "put pam here"}
    
    set_to_test = int(input("Which set do you want to test?\n1 for Abalone (Classification)\n2 for Car Evaluation (Classification)\n3 for Image Segmentation (Classification)\n4 for Computer Hardware (Regression)\n5 for Forest Fires (Regression)\n6 for Wine Quality (Regression)\n"))
    method_to_use = int(input("Which method do you want to use for testing these sets?\n1 for base KNN\n2 for edited KNN (Note: not available for regression datasets)\n3 for condensed KNN (Note: not available for regression datasets)\n4 for edited KNN using K Means Clustering\n5 for edited KNN using PAM Clustering\n"))
    k_to_use = int(input("Pick a k, any k\n"))
    '''
    set_to_test = int(sys.argv[1])
    method_to_use = int(sys.argv[2])
    k_to_use = int(sys.argv[3])'''
    unscrambled_data = get_list(set_to_test)
    if set_to_test < 4:
        cross_validate_classify(unscrambled_data,method_to_use,k_to_use)
    else:
        cross_validate_regression(unscrambled_data, method_to_use,k_to_use)
    
    

'''
I reuse a couple snippets of code in here so I can either run indivisual algorithms with the above function, or run everything sequentially for comparisons with the below
Not gonna lie, this turned out to be a lot messier than I intended it to be, but it gets the job done, and in the end that's all I was really aiming for.
'''
def run_all_algs():
    # variant = int(sys.argv[1])
    #print(variant)
    classification = {0:"Base KNN:",1:"Edited KNN:",2:"Condensed KNN:",3:"C Means:",4:"PAM:"}
    regresssion = {0:"Base KNN:", 1: "C Means:",2:"PAM"}
    files = ["Abalone","Cars","Image Segmentation","Computer Hardware","Forest Fires","Wine Quality"] 
    i = int(sys.argv[1])
    ks = [1,1,1,3,3,3] 
    print("Classification Datasets:")
    print(files[i-1])
    dataset = get_list(i)
    split_data = splitter(dataset)
    base_results = []
    e_results = []
    c_results = []
    mean_results = []
    pam_results = []
    for j in range(10):
        to_learn = copy.copy(split_data) # Grabs a fresh copy of the dataset each time, since the to_learn list deletes a tenth of the data in each loop
        to_test = make_test_set(to_learn.pop(j))
        to_learn = flatten_list(to_learn)
        spare_test = to_test
        knn = k_nearest_neighbors(ks[i-1],to_learn,0)
        eknn = edited_knn(ks[i-1],to_learn,0)
        cknn = condensed_knn(ks[i-1],to_learn,0)
        cmean = c_means(ks[i-1],to_learn,0)
        alg_pam = pam(ks[i-1],to_learn,0)
        base_results.append(knn.classify(to_test))
        to_test = spare_test
        e_results.append(eknn.classify(to_test))
        to_test = spare_test
        c_results.append(cknn.classify(to_test))
        to_test = spare_test
        mean_results.append(cmean.classify(to_test))
        to_test = spare_test
        pam_results.append(alg_pam.classify(to_test))
    unsplit_data = flatten_list(split_data)    
    print(classification[0]) # I was too tired to figure out how lists work, so I ended up making this hardcoded mess. Sorry. 
    temp = flatten_list(base_results)
    print(analyze(unsplit_data,temp,30))
    print(classification[1])
    temp = flatten_list(e_results)
    print(analyze(unsplit_data,temp,30))
    print(classification[2])
    temp = flatten_list(c_results)
    print(analyze(unsplit_data,temp,30))
    print(classification[3])
    temp = flatten_list(mean_results)
    print(analyze(unsplit_data,temp,30))
    print(classification[4])
    temp = flatten_list(pam_results)
    print(analyze(unsplit_data,temp,30))
    '''
    print(files[i-1])
    dataset = get_list(i)
    split_data = splitter(dataset)
    base_results = []
    mean_results = []
    pam_results = []
    for j in range(10):
        to_learn = copy.copy(split_data) # Grabs a fresh copy of the dataset each time, since the to_learn list deletes a tenth of the data in each loop
        to_test = make_test_set(to_learn.pop(j))
        to_learn = flatten_list(to_learn)
        spare_test = to_test
        knn = k_nearest_neighbors(ks[i-1],to_learn,1)
        cmean = c_means(ks[i-1],to_learn,1)
        alg_pam = pam(ks[i-1],to_learn,1)
        base_results.append(knn.regression(to_test))
        to_test = spare_test
        mean_results.append(cmean.regression(to_test))
        to_test = spare_test
        pam_results.append(alg_pam.regression(to_test))
    unsplit_data = flatten_list(split_data)
    print(regresssion[0])
    temp  = flatten_list(base_results)
    print(sa.mse(unsplit_data,temp))
    print(sa.abs_error(unsplit_data,temp))
    print(regresssion[1])
    temp  = flatten_list(mean_results)
    print(sa.mse(unsplit_data,temp))
    print(sa.abs_error(unsplit_data,temp))
    print(regresssion[2])
    temp  = flatten_list(pam_results)
    print(sa.mse(unsplit_data,temp))
    print(sa.abs_error(unsplit_data,temp))
    '''




#work_it()
run_all_algs()

