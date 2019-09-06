""" Functions for performing statistical analysis of our data and results """
# make a function that checks from an orginal data set
def difference(class_o, class_m):
    if len(class_o) == len(class_m):
        diff = []
        for i in range(len(class_o)):
            diff.append(class_o[i] - class_m[i])
        print(diff)
    else:
        print("somethings wrong")

x = [100, 10, 50]
y = [100, 5, 25]
difference(x, y)

