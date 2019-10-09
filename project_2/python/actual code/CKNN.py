import KNN
import numpy as numpy
import random as rd
from DATAPOINT import data_point
from POINTMAP import point_map

class condensed_knn(KNN.k_nearest_neighbors):
    def __init__(self, in_k, dataset, alg):
        KNN.k_nearest_neighbors.__init__(self,in_k,dataset,alg)
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
            adding = False
            rd.shuffle(old_points)
            for i, point in enumerate(old_points):
                point = self.edited_class_remover(point_map([point]))
                self.classify([point])
                if point.class_type != old_points[i].class_type:
                    new_points.append(point)
                    old_points.remove(point)
                    adding = True

        self.d_map = point_map(new_points)