import math
import random



class data_point():

    def __init__(self, k, data):
        self.k = k
        self.nearest = []
        self.class_type = data[-1]
        self.data = data[:-1]



    def get_k_nearest(self, neighbors):
        points = []
        for neighbor in neighbor:
            points.append([self.euclidiean_dist(neighbor), neighbor.class_type])
        points = sorted(points[0])
        for i in range(k):
            self.nearest.append(points[i])



    def euclidiean_dist(self, other):
        total = 0
        for i in range(len(self.data)):
            total += ((self.data[i] - other.data[i])**2)
        return math.sqrt(total)


    def max_class_occurrences(self):
        for i in range(len(self.nearest)):
            



