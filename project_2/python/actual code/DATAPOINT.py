
'''This is the container for data. It consists of an array for all of the regular data in a point, and a separate variable to contain the class value for the point'''
class data_point():
    def __init__(self, data, class_type):
        self.data = data
        self.class_type = class_type