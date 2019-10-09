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
        self.c_clusters = self.mini_gen(rd.sample(data_set,numC))
        self.data_points = self.mini_gen(data_set)
        for x in range(0,100):
            self.calculate_centroids()
        self.d_map = self.c_clusters


    def mini_gen(self, data_in):
        point_list = []
        for line in self.d_set:
            point_list.append(data_point(line[:-1], line[-1]))
        return point_list


    def calculate_centroids(self):
        children = []
        for point in self.data_points:
            point_belongs_to = ''
            shortest_dist = np.inf()
            for i in self.c_clusters:
                temp_dist = self.euclidian(point.data,i.data)
                if (temp_dist<shortest_dist):
                    shortest_dist = temp_dist
                    point_belongs_to = i
            children.append([point,point_belongs_to])

        for cluster in self.c_clusters:
            points = []
            for point in children:
                if point[1] == cluster:
                    points.append(point[0])
            ind = self.c_clusters.index(cluster)
            self.c_clusters[ind].data = self.find_average(points)
    
    def find_average(self,points):
        new_data = []
        for x in range(=,len(points[0].data)):
            new_data.append(0)
            avg = []
            for point in points:
                avg.append(point.data[0])
            value = sum(avg)/len(avg)
            new_data[x] = value
        return new_data