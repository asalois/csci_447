'''This is an extension of base KNN, using the editing method of traning set reduction'''

import KNN
import numpy as np
from DATAPOINT import data_point
from POINTMAP import point_map

class edited_knn(KNN.k_nearest_neighbors):

    def __init__(self, in_k, dataset, alg):
        KNN.k_nearest_neighbors.__init__(self,in_k,dataset,alg)
        self.alg = alg # This is only used for clustering, but we declare it everywhere so the driver can handle everything
        # edited_set = self.edit_data_set(self.d_map.points)
        if alg==0:
            self.edit_two()
        

    '''takes in an array of points, then strips them of their class so they can be reclassified while building the edited set'''
    def edited_class_remover(self,in_set):
        classless_data = []
        for point in in_set.points:
            classless_data.append(point.data[:])
        return classless_data

    '''This edits the dataset by subtracting points from the training set if they cannot be correctly classified by the rest of the set'''
    def edit_two(self):
        prev_map = point_map([0]) # Instatiating this to length 1, so the while loop doesn't explode
        cur_map = self.d_map
        cur_iter = 0
        map_to_return = self.d_map
        while (abs(len(cur_map.points)-len(prev_map.points)) > int(round(len(self.d_map.points) * .04))): # This is maybe a little bit hacky, but basically it stops looping if the change in size between the previous and current runs are less than 4% of the size of the original set
            cur_iter += 1
            print("Iteration " + str(cur_iter))
            prev_map = cur_map
            # temp_points = self.edited_class_remover(cur_map)
            reclassed_points = []
            for point in cur_map.points:
                unclassed_point = self.edited_class_remover(point_map([point]))
                back_map = self.d_map
                self.d_map.points.remove(point)
                reclassed_points.append(self.classify(unclassed_point))
                self.d_map = back_map
            for i, point in enumerate(cur_map.points):
                if point.class_type != map_to_return.points[i].class_type: # This is also maybe a little hacky, but it prevents out of bounds errors after we start to remove points
                    cur_map.points.remove(point)
                    map_to_return.points.remove(map_to_return.points[i]) # This function got nastier and nastier as I tried to fix bugs. Sorry if it's horrible.

        self.d_map = map_to_return
