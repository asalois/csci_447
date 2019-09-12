""" Filename says it all """
#--- add a description of this file
#--- add resources/cited where needed
#This file was programmed by Sage Acteson

numExamples = 0 # the total number of examples/observations in the training set
freqTable = [] # a table of all classes and the frequencies of all possible values of their attributes

def train(dataList):
    """
    This training is done using a 4d list. The levels are as follows, from the outermost inward:
    - Class : separated by class, with the class listed as the second to last element (last is the total instances of the class)
    - Attribute : essentially separated by their position in the data
    - Attribute value : the possible values an attribute can take on (works for non-binary)
    - Total : a list with two elements. The first element is the number of instances of the value, and the second is its probability

    """
    makeTable(dataList) # makes a table of all class data
    calculateQ() # calculates Q - distribution within each class (proportion of the overall amount)
    calculateF() # calculates F

def makeTable(dataList):
    global freqTable, numExamples # get global variables

    for row in range(len(dataList)): # iterate through all of the rows in the input data

        cType = dataList[row][len(dataList[row])-1] # get the class of the current row
        cIndex = -1 # the index of the class data in the frequency table

        for rowFT in range(len(freqTable)): # look for an existing class that matches
            if cType == freqTable[rowFT][len(freqTable[rowFT])-2]: # if the class is in the table
                cIndex = rowFT # then log the position

        if cIndex == -1: # either no existing matching class or table is empty (make a new row)
            freqTable.append([]) # create a new row to add the class data
            for elem in range(len(dataList[row])-1): # for all the attributes in the row of data
                freqTable[len(freqTable)-1].append([[dataList[row][elem],1]]) # add the attribute and set the number of instances to 1
            freqTable[len(freqTable)-1].append(dataList[row][len(dataList[row])-1]) # add the class to the list 
            freqTable[len(freqTable)-1].append([1]) # add another list to hold the total number of class instances and later, Q
            numExamples += 1 # another observation/row used/completed
            continue # this input row is done

        # reaching this point means a matching class was found in the frequency table
        for attr in range(len(dataList[row])-1): # go through each attribute in this line of the data
            attribute = dataList[row][attr] # store the attribute
            aIndex = -1 # used to determine if an a matching value exists
            for a in range(len(freqTable[cIndex][attr])): # go through existing values for this attribute
                if attribute == freqTable[cIndex][attr][a][0]: # if a matching value is found
                    freqTable[cIndex][attr][a][1] += 1 # then increment the counter for that value
                    aIndex = a # and log the position
                    #--- break or continue? to save time
            if aIndex == -1 : # there was no matching value for the attribute
                freqTable[cIndex][attr].append([attribute,1]) # add a new value for the attribute
            
        freqTable[cIndex][len(freqTable[cIndex])-1][0] += 1 # increment the total number of class instances
        numExamples += 1 # another observation/row used/completed

def calculateQ(): # calculate Q: the number of examples of the particular class divided by the total number of examples
    
    global freqTable

    for row in range(len(freqTable)): # for each row (class)
        freqTable[row][len(freqTable[row])-1].append(freqTable[row][len(freqTable[row])-1][0]/numExamples) # append Q to the class total

def calculateF(): # calculates the relative percentages for each attribute
    
    global freqTable

    for row in range(len(freqTable)): # for each row (class)
        numAttr = len(freqTable[row])-2 # store number of attributes 
        for attr in range(numAttr) : # for each row (attribute)
            for aVal in range(len(freqTable[row][attr])) : # for each row (attribute value)
                numerator = 1 + freqTable[row][attr][aVal][1] # the number of examples that match the attribute value + 1
                denominator = numAttr + freqTable[row][len(freqTable[row])-1][0] # number of attributes + number of examples in the class
                freqTable[row][attr][aVal].append(numerator/denominator) # append the relative probability
                


def classify(dataList): # classifies data which is passed in without classes, likely class appended, data returned
    print("No classifying yet")


a = [[4, 0, 3], [1, 2, 4], [6,1,3], [0,3,4]]
b = [[5,2],[2,3]]
c = [[[[2.5,1]],"c1"]]
d = 90

e=[[1,8,3,50],[1,9,1,50],[3,6,9,49],[2,6,9,49]]
train(e)
print(freqTable)
#print(numExamples)
