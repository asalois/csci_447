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
        if alg == 1:                                    #indicates wether or not to use eknn for the number of centroids
            self.numC = int(round(len(data_set)/4))
        elif alg == 0:
            self.numC = len(self.d_map.points)
        self.c_clusters = self.mini_gen(rd.sample(data_set,self.numC))
        self.data_points = self.mini_gen(data_set)
        for x in range(0,10):
            self.calculate_centroids()
        self.d_map = point_map(self.c_clusters)


    def mini_gen(self, data_in):                # Makes a new list of points
        point_list = []
        for line in self.d_set:
            point_list.append(data_point(line[:-1], line[-1]))
        return point_list


    def calculate_centroids(self):              #Calculates the centroids
        children = []
        for point in self.data_points:          #Decides which centoid each data point belongs to
            point_belongs_to = ''
            shortest_dist = np.inf
            for i in self.c_clusters:
                temp_dist = self.euclidian(point.data,i.data)
                if (temp_dist < shortest_dist):
                    shortest_dist = temp_dist
                    point_belongs_to = i
            children.append([point,point_belongs_to])

        for cluster in self.c_clusters:         #Decides which class each centoid belongs to 
            points = []
            for point in children:
                if point[1] == cluster:
                    points.append(point[0])
            ind = self.c_clusters.index(cluster)
            if len(points) > 0:
                self.c_clusters[ind] = self.find_average(points)
    
    def find_average(self,points):                  #finds the average position of data points that belong to a cluster and assigns the new position to the centoid
        new_data = np.full(len(points[0].data),0)
        new_class = 0
        for i in range(len(points[0].data)):        #average the position
            for row in range(len(points)):
                new_data[i] += points[row].data[i]
            new_data[i] = int(round(new_data[i]/len(points)))
        for i in range(len(points)):                #average the class
            new_class += points[i].class_type
        new_class = int(round(new_class/len(points)))
        return data_point(new_data,new_class)       #return the new centroid