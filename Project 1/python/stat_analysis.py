""" Functions for performing statistical analysis of our data and results """
# make a function that checks from an orginal data set

# clalculates the error base upon a confusion matrix
def errorCalc(tp,fp,fn,tn):# True+, False+, False-, True-
    err =  (fp + fn) / (tp + fp + fn + tp)
    precision = tp / (tp + fp)
    recall = tp / ( tp + fn)
    error = [err, precision, recall]
    return error


# simple binary confusion Matrix builder
def makeConfMatrix(classO, classM):
    conf = [0,0,0,0] # [True+ False+ False- True-]
    if len(classO) == len(classM):
        for i in range(len(classO)):
            if classO[i] == classM[i]:
                if classO[i] == 1:
                    conf[0] += 1
                else:
                    conf[3] += 1
            else:
                if classO[i] == 1:
                    conf[2] += 1
                else:
                    conf[1] += 1
    else:
        print("Not going to work")

    return conf


def difference(classO, classM):
    if len(classO) == len(classM):
        diff = []
        for i in range(len(classO)):
            diff.append(classO[i] - classM[i])
        print(diff)
    else:
        print("somethings wrong")


x = [0,0,0,0,1,1,1,1]
y = [0,1,0,1,0,1,0,1]
print(makeConfMatrix(x, y))

