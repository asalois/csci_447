import numpy as np 
import random as rd 
import math
from POINTMAP import point_map
from DATAPOINT import data_point

class k_nearest_neighbors():
    def __init__(self, in_k, dataset):
        self.k = in_k
        self.d_set = dataset
        self.d_map = ''
        self.generate()


    def generate(self):
        point_list = []
        for line in self.d_set:
            point_list.append(data_point(line[:-1], line[-1]))
        self.d_map = point_map(point_list)

    '''p_1  is the point to be classified, p_2 is the current point in the training set to find p_1s distance from'''
    def euclidian(self, p_1, p_2):
        dist = 0
        for i in range(len(p_1.data)):
            dist += pow((p_1.data[i] - p_2.data[i]),2)

        return math.sqrt(dist)

    def get_k_nearest(self, unclass_point):
        neighbors_and_distances = []
        k_nearest = []
        for point in self.d_map.points:
            neighbors_and_distances.append([self.euclidian(unclass_point,point),point.class_num])
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
                occurence_counter[int(nearest[i][1] - 1)] += 1 # We cast this particular index to int, since no classes in these sets are of float value
            max_occurrence = np.argmax(occurence_counter)
            point.class_type = max_occurrence

        return points_to_classify


    def regression(self, data_to_regress):
        points_to_regress = []
        nearest = []
        occurrence_counter = []
        for line in data_to_regress:
            points_to_regress.append(data_point(line[:], ''))

        for point in points_to_regress:
            nearest = self.get_k_nearest(point)
            nearest = sorted(nearest, key= lambda l:l[1], reverse=True)
            average =  0
            for i in range(self.k):
                average +=  nearest[i][-1]
            average = average / self.k
            point.class_type = average

        return points_to_regress
