""" Functions for performing statistical analysis of our data and results """
# make a function that checks from an orginal data set
import numpy
import data_setup
import copy
import random
# clalculates the error base upon a confusion matrix
def clacError():
    top = a


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
            conf[actual[i][-1]][predicted[i][-1]] += 1
    return conf


def difference(classO, classM):
    if len(classO) == len(classM):
        diff = []
        for i in range(len(classO)):
            diff.append(classO[i] - classM[i])
        print(diff)
    else:
        print("somethings wrong")

irisData0 = data_setup.readInCom('3', '?')
irisData1 = data_setup.readInCom('3', '?')
irisData2 = copy.copy(irisData1)
irisData2.reverse()
irisData3 = copy.copy(irisData2)
random.shuffle(irisData3)
x = [0,0,0,0,1,1,1,1]
y = [0,1,0,1,0,1,0,1]
matrix0 = makeConfMatrix(irisData0, irisData1, 3)
matrix1 = makeConfMatrix(irisData0, irisData2, 3)
matrix2 = makeConfMatrix(irisData0, irisData3, 3)
totals0 = totals(matrix0)
totals1 = totals(matrix1)
totals2 = totals(matrix2)
print('The Confusion  Matrix is ')
print(totals0)
print(totals1)
print(totals2)
