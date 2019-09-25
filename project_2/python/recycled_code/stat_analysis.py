""" Functions for performing statistical analysis of our data and results """
# make a function that checks from an orginal data set
# Programmed by Alex, cleared up by Ethan
import numpy
import data_setup
import copy
import random
# calculates the error base upon a confusion matrix
# Note that when 'nan' is returned, this is due to a lack of either false positives or false negatives for that particular class
def calcError(filled):
    error =  numpy.full((3,len(filled)),0.0)
    for i in range(len(filled) -1):
        fp = filled[i][-1] -  filled[i][i]
        fn = filled[-1][i] -  filled[i][i]
        tp = filled[i][i]
        error[0][i] =  (fp + fn)/(fp + fn + 2*tp) # error. This is the first row in printed for each call
        error[1][i] = tp / (tp + fp) # precision. This is the second row printed for each call
        error[2][i] = tp / (tp + fn) # recall. This is the final row printed for each call
    return error 


# make totals around the Confusion Matrix
def totals(confMatrix):
    classNum = len(confMatrix)
    totals = numpy.full((classNum + 1, classNum + 1),0)
    for i in range(classNum):
        for j in range(classNum):
            totals[i][j] = confMatrix[i][j]
            totals[i][-1] += confMatrix[i][j]
            totals[-1][i] += confMatrix[j][i]
        totals[-1][-1] += totals[-1][i]
    return totals


# simple binary confusion Matrix builder
def makeConfMatrix(actual, predicted, numClasses):
    conf = numpy.full((numClasses, numClasses),0)
    for i in range(len(actual)):
            conf[int(actual[i][-1])][int(predicted[i][-1])] += 1 # This casts the class attribute to int, since some sets are float by default
    return conf


'''
irisData0 = data_setup.readInCom('3', '?')
irisData1 = data_setup.readInCom('3', '?')
irisData2 = copy.copy(irisData1)
irisData2.reverse()
irisData3 = copy.copy(irisData2)
random.shuffle(irisData3)
x = [[0],[0],[0],[0],[0],[1],[1],[1],[1],[0]]
y = [[0],[1],[0],[1],[0],[1],[0],[1],[1],[0]]
matrix0 = makeConfMatrix(irisData0, irisData1, 3)
matrix1 = makeConfMatrix(irisData0, irisData2, 3)
matrix2 = makeConfMatrix(irisData0, irisData3, 3)
matrix3 = makeConfMatrix(x, y, 2)
totals0 = totals(matrix0)
totals1 = totals(matrix1)
totals2 = totals(matrix2)
totals3 = totals(matrix3)
print('The Confusion  Matrix is ')
print(totals0)
print(totals1)
print(totals2)
print(totals3)
print(clacError(totals0))
print(clacError(totals1))
print(clacError(totals2))
print(clacError(totals3))
'''