import numpy as np 
import random as rd 
import math
import EKNN
from DATAPOINT import data_point
from POINTMAP import point_map

class c_means(EKNN.edited_knn):
    
    def __init__(self,in_k,data_set,alg):
        EKNN.edited_knn.__init__(self,in_k,data_set,alg)
        self.d_set = data_set
        self.c_clusters = ''
        self.k = in_k
        if alg == 1:
            self.numC = int(round(len(dataSet)/4))
        elif alg == 0:
            self.numC = len(self.d_map.points)
        first_points = self.mini_gen(rd.sample(data_set,numC))
        first_points


    def mini_gen(self, data_in):
        point_list = []
        for line in self.d_set:
            point_list.append(data_point(line[:-1], line[-1]))
        return point_list

    def calculate_centroids(self, points_in):
        children = []
        for point in points_in:
            point_belongs_to = ''
            shortest_dist = np.inf()
            for i in self.