""" Functions for performing statistical analysis of our data and results """
# make a function that checks from an orginal data set
# Programmed by Alex
import numpy
import data_setup
import copy
import random
from DATAPOINT import data_point
# calculates the error base upon a confusion matrix
# Note that when 'nan' is returned, this is due to a lack of either false positives or false negatives for that particular class
def calcError(filled):
    error =  numpy.full((5,len(filled) -1),0.0)
    print('error')
    for i in range(len(filled) -1):
        fp = filled[i][-1] -  filled[i][i]
        fn = filled[-1][i] -  filled[i][i]
        tp = filled[i][i]
        error[3][i] = tp # values that are right
        error[4][i] = fn + fp # values that are wrong
        if (fp + fn + 2*tp) != 0.0:
            error[0][i] =  (fp + fn)/(fp + fn + 2*tp) # error. This is the first row in printed for each call
        if (tp + fp)  != 0.0:
            error[1][i] = tp / (tp + fp) # precision. This is the second row printed for each call
        if (tp + fn)  != 0.0:
            error[2][i] = tp / (tp + fn) # recall. This is the final row printed for each call
    return error 


# make totals around the Confusion Matrix
def totals(confMatrix):
    # for row in confMatrix:
    #     print(row)
    classNum = len(confMatrix)
    totals = numpy.full((classNum + 1, classNum + 1),0)
    for i in range(classNum):
        for j in range(classNum):
            totals[i][j] = confMatrix[i][j]
            totals[i][-1] += confMatrix[i][j]
            totals[-1][i] += confMatrix[j][i]
        totals[-1][-1] += totals[-1][i]
    return totals


# simple confusion Matrix builder
def makeConfMatrix(actual, predicted, numClasses):
    conf = numpy.full((numClasses, numClasses),0)
    for i in range(len(actual)):
            conf[int(actual[i][-1])][int(predicted[i].class_type)] += 1 # This casts the class attribute to int, since some sets are float by default
    return conf


# functions to use with regression

def mse(actual, predicted): # mean sqaure errror
    print('mse')
    mse = 0
    for i in range(len(predicted)):
        mse += pow((float(actual[i][-1]) - float(predicted[i].class_type)),2)
    mse / len(predicted)
    return mse

def abs_error(actual, predicted): #  absoulute error
    print('abs')
    abs_error = 0
    for i in range(len(predicted)):
        abs_error += abs(float(actual[i][-1]) - float(predicted[i].class_type))
    return abs_error