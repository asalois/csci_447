import KNN
import numpy as numpy
import random as rd
from DATAPOINT import data_point
from POINTMAP import point_map

class condensed_knn(KNN.k_nearest_neighbors):
    def __init__(self, in_k, dataset):
        KNN.k_nearest_neighbors.__init__(self,in_k,dataset)
        self.condense_set()


    def edited_class_remover(self,in_set):
        classless_data = []
        for point in in_set.points:
            classless_data.append(point.data[:])
        return classless_data


    def condense_set(self):
        old_points = self.d_map.points
        new_points = []
        first_point = rd.choice(old_points)
        old_points.remove(first_point)
        new_points.append(first_point)
        adding = True
        while adding:
            for i, point in enumerate(rd.shuffle(old_points))
            