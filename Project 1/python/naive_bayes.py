""" Filename says it all """
#--- add a description of this file eventually
#--- add resources/cited where needed


#This file was programmed by Sage Acteson

classTable = [] # the table of all classes and attributes in the training set
numExamples = 0 # the total number of examples/observations in the training set

def train(dataList):
    makeTable(dataList) # makes a table of all class data
    calculateQ() # calculates Q
    print("Table: ")
    print(classTable)
    calculateF() # calculates F

def makeTable(dataList):

    #initialize variables
    global numExamples, classTable 
    #clear any data from previous tests
    numExamples, classTable = 0, []
    #iterate through each row of the data
    for row in dataList:
        cType = row[len(row)-1] # class of current row
        cIndex = -1 # row in the classTable that matches the class

        for rowCT in range(len(classTable)): # find the matching row in the class table
            if classTable[rowCT][len(classTable[rowCT])-2] == cType: # if the class is already in the table
                cIndex = rowCT
        
        if cIndex == -1: # either no existing matching class or table is empty (make a new row)
            classTable.append(row) # add the row to the classTable as a new class
            classTable[len(classTable)-1].append(1) # add a new column in the new row for to total instances of the class
            numExamples += 1 # another observation/row used
            continue # this row is done

        for attr in range(len(row)-1): # go through all of the attributes
            classTable[cIndex][attr] += row[attr]

        classTable[cIndex][len(classTable[cIndex])-1] += 1 # increase the total value for the respective class
        numExamples += 1 # another observation/row used

def calculateQ(): # calculate Q: the number of examples of the particular class divided by the total number of examples
    global classTable, numExamples 
    for row in classTable:
        row.append(row[len(row)-1] / numExamples) # add another column for Q and store the value there

def calculateF():
    
    global classTable, numExamples

    for row in classTable:
        numAttr = len(row)-3
        for x in range(numAttr):
            row[x] = ( row[x] +1 ) / (numAttr + row[len(row)-2])

def classify(dataList):
    print("No classifying yet")
    x = argmax()
    return 5

def argmax():
    return 8


a = [[4, 0, 3], [1, 2, 4], [6,1,3], [0,3,4]]
b = [[5,2],[2,3]]

train(a)
print("Trained Table: ")
print(classTable)

done = classify(b)
