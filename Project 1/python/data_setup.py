# """ This is for reading and preparing data for runs in through our ML algorithm """
# This file programmed by Zan Rost-Montieth
import os                                               # used to set filepaths dynamically
dirname = os.path.dirname(__file__)                     # finds current folder
filepath = os.path.join(dirname, '../Datasets/')        # navigate to datasets folder

def readInCom(fileNum, remove):
    arr = []                                            # list to hold all out data
    files = ["breast-cancer-wisconsin.data","glass.data","iris.data","soybean-small.data","house-votes-84.data"] # list of data files so they can be chosen dynamically

    fileToOpen = filepath + files[int(fileNum)-1]         # creates file path to numbered data file numbered naturally 1-5 

    fileIn = open (fileToOpen,"r")  
    numRemoved = 0

    for line in fileIn.readlines():                     
        if line != "":                                  # if line is not empty
            arr.append([])                              # start a new list for a new data entry
            for z in line.split(","):                   # split the data entries
                z = z.rstrip()                          # remove \n from the end of lines 
                if z == remove:
                    print("missing value replaced")
                    arr[-1].append("@")
                elif z.isdigit():                         # if data entry is a number convert it to an integer
                    arr[-1].append(int(z.rstrip()))     
                else:
                    try:
                        arr[-1].append(float(z))        # if it is a float add it as one
                    except ValueError:
                        if z != '':                     # otherwise as long as it is not empty add it as a string    
                            arr[-1].append(z)
    arr = [z for z in arr if z != []]                           # removes last list in the array in case input has new line at the end 
    for z in range(0,len(arr[0])):                  # go through the file to edit data
        strings = []                                # list to hold all unique strings in a column
        for y in range(0,len(arr)):
            if isinstance(arr[y][z],str) and arr[y][z]!="@":           
                repeat = False
                for x in range(0,len(strings)):
                    if arr[y][z] == strings[x]:
                        repeat = True
                if repeat == False:
                    strings.append(arr[y][z])       # if it is a new unique string add is to the reference list
        strings.sort()
        if len(strings) > 0:                        # if we have a list of strings this will assign numerical values
            for y in range(0,len(arr)):
                for x in range(0,len(strings)):
                    if arr[y][z] == strings[x]:
                        arr[y][z] = x
            print("column ", z + 1, "has been normalized")      # print out what numers represnt what
            for y in range(0,len(strings)):                     
                print(y, " = ", strings[y])

    print(fileNum)
    if fileNum == '1':
        for z in arr:
            del z[0]
    elif fileNum == '5':
        for z in arr:
            z.insert(17,z.pop(0))
    elif fileNum == '2':
        for z in arr:
            z[-1] = z[-1] -1 # subtracts the class attribute by 1, so there aren't any conflicts in the stat_analysis function
    for z in range(len(arr)):                       # print out the data set
        print(arr[z])

    print("removed ", numRemoved, "data points")

    return arr                      #return the data set


def readInPerson():
    print("pls choose which file you would like\n 1: for Breast Cancer Data\n 2: for Glass Data\n 3: for Iris Data\n 4: for Soybean Data\n 5: for Vote Data ")
    choice = input("your choice: ")

    remove = input("please input the value used to denote a missing value: ")  
    readInCom(choice, remove)

# readInPerson()