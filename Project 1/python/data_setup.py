# """ This is for reading and preparing data for runs in through our ML algorithm """
import os
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, '../Datasets/')


def readInCom(input):
    arr = []

    files = ["breast-cancer-wisconsin.data","glass.data","iris.data","soybean-small.data","house-votes-84.data"]

    fileToOpen = filepath + files[int(input)-1]

    fileIn = open (fileToOpen,"r")
    for line in fileIn.readlines():
        if line != "":
            arr.append([])
            for z in line.split(","):
                z = z.rstrip()
                if z.isdigit():
                    arr[-1].append(int(z.rstrip()))
                else:
                    try:
                        arr[-1].append(float(z))
                    except ValueError:
                        if z != '':
                            arr[-1].append(z)
    arr = [z for z in arr if z != []]                           # removes last list in the array in case input has new line at the end 
    for z in range(0,len(arr[0])):
        strings = []
        for y in range(0,len(arr)):
            if isinstance(arr[y][z],str):
                repeat = False
                for x in range(0,len(strings)):
                    if arr[y][z] == strings[x]:
                        repeat = True
                if repeat == False:
                    strings.append(arr[y][z])
        

        if len(strings) > 0:
            for y in range(0,len(arr)):
                for x in range(0,len(strings)):
                    if arr[y][z] == strings[x]:
                        arr[y][z] = x
            print("column ", z + 1, "has been normalized")
            for y in range(0,len(strings)):
                print(y, " = ", strings[y])
    for z in range(len(arr)):
        print(arr[z])

    print("all Done")


def readInPerson():
    print("pls choose which file you would like\n 1: for Breast Cancer Data\n 2: for Glass Data\n 3: for Iris Data\n 4: for Soybean Data\n 5: for Vote Data ")

    readInCom(input("your choice: "))


# readInPerson()