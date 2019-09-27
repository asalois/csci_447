from recycled_code import data_setup
from DataPoint import data_point
import math
import numpy

class d_map():

    '''Dataset is an intteger value sent into the data_setup file to retrieve a specific set'''
    def __init__(self, in_k, dataset):
        self.k = in_k
        self.d_set = dataset
        self.points = []


    def generate(self):
        # temp_data = data_setup.readInCom(dataset,'')
        for line in self.d_set:
            self.points.append(data_point(line[:-1], line[-1]))

    '''p_1  is the point to be classified, p_2 is the current point in the training set to find p_1s distance from'''
    def euclidian(self, p_1, p_2):
        dist = 0
        for i in range(len(p_1.data)):
            dist += pow((p_1.data[i] - p_2.data[i]),2)

        return math.sqrt(dist)

    def get_k_nearest(self, unclass_point):
        neighbors_and_distances = []
        k_nearest = []
        for point in self.points:
            neighbors_and_distances.append([self.euclidian(unclass_point,point),point.class_type])
        neighbors_and_distances = sorted(neighbors_and_distances, key= lambda l:l[0])
        k_nearest = neighbors_and_distances[:self.k]
        return k_nearest


    def classify(self, data_to_classify):
        points_to_classify = []
        nearest = []
        occurrence_counter = []
        for line in data_to_classify:
            points_to_classify.append(data_point(line[:], ''))

        for point in points_to_classify:
            nearest = self.get_k_nearest(point)
            nearest = sorted(nearest, key= lambda l:l[1], reverse=True)
            occurence_length = int(nearest[0][1])
            occurence_counter = [0 for i in range(occurence_length)]
            for i in range(self.k):
                occurence_counter[int(nearest[i][1] - 1)] += 1 # We cast htis particular index to int, since no classes in these sets are of float value
            max_occurrence = numpy.argmax(occurence_counter)
            point.class_type = max_occurrence

        return points_to_classify
