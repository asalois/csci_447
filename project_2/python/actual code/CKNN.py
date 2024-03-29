import KNN
import numpy as np
import random as rd
from DATAPOINT import data_point
from POINTMAP import point_map

class condensed_knn(KNN.k_nearest_neighbors):
    def __init__(self, in_k, dataset, alg):
        KNN.k_nearest_neighbors.__init__(self,in_k,dataset,alg)
        self.condense_set()


    def edited_class_remover(self,in_set):      # removes the class from set 
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
            for i, point in enumerate(old_points):              # go through all of our points         
                point = self.edited_class_remover(point_map([point]))
                point =  self.classify(point)[0]
                if point.class_type != old_points[i].class_type:    # if it isn't classified right add it to the map
                    new_points.append(point)
                    old_points.remove(old_points[i])
                    adding = True                   # we need to add more points

        self.d_map = point_map(new_points)