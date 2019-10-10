import numpy as np 
import random as rd 
import math
from POINTMAP import point_map
from DATAPOINT import data_point

class k_nearest_neighbors():
    def __init__(self, in_k, dataset,alg):
        self.alg = alg # This is only used for clustering, but we declare it everywhere so the driver can handle everything
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
        # if (len(p_1.data) != len(p_2.data)):
        #     print("Different lengths",len(p_1.data),len(p_2.data))
        for i in range(len(p_1.data)):
            #print(p_1.data[i],p_2.data[i])
            dist += pow((p_1.data[i] - p_2.data[i]),2)

        return dist

    def get_k_nearest(self, unclass_point):
        neighbors_and_distances = []
        for point in self.d_map.points:
            neighbors_and_distances.append([self.euclidian(unclass_point,point),point.class_type])
        neighbors_and_distances = sorted(neighbors_and_distances, key= lambda l:l[0])
        return neighbors_and_distances


    def classify(self, data_to_classify):
        points_to_classify = []
        nearest = []
        count = 0
        for line in data_to_classify:
            points_to_classify.append(data_point(line[:], ''))

        for point in points_to_classify:
            count += 1
            nearest = self.get_k_nearest(point)
            #nearest = sorted(nearest, key= lambda l:l[1], reverse=True)
            #occurence_length = int(nearest[0][1])
            #occurence_counter = [0 for i in range(occurence_length)]
            occurrence_counter = np.full(2000,0) # This is declared ahead of time to avoid any potential issues with out of bounds errors that might occur if dynamically declaring. It's huge because of the machine dataset
            for i in range(self.k):
                occurrence_counter[int(nearest[i][-1])] += 1 # We cast this particular index to int, since no classes in these sets are of float value
            max_occurrence = np.argmax(occurrence_counter)
            point.class_type = max_occurrence
            # print("point " + str(count) + " classified")

        return points_to_classify


    def regression(self, data_to_regress):
        points_to_regress = []
        nearest = []
        for line in data_to_regress:
            points_to_regress.append(data_point(line[:], ''))

        for point in points_to_regress:
            nearest = self.get_k_nearest(point)
            nearest = sorted(nearest, key= lambda l:l[1], reverse=True)
            average =  0
            for i in range(self.k):
                average +=  nearest[i][-1]
            average = average / self.k
            point.class_type = int(round(average))

        return points_to_regress
