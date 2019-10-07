import numpy as np 
import random as rd 
import math
import EKNN
from DATAPOINT import data_point

class c_means(EKNN.edited_knn):
    def __init__(self, k, dataMap):
        self.kNum = k
        EKNN.edited_knn(k, dataMap)
        self.d_set = dataMap
        self.c_means_map = ''
        self.numC = len(self.d_map)
        self.placeInitialC(self.numC,self.uniqueRdmPnts(self.numC),self.d_set)
        self.ttr = 100
        for x in range(0,100):
            self.calcCentoids()
    
    def placeInitialC (self, numC, indexes, dataMap):
        point_map = []
        for z in range (0,numC):
            point_map.append(dataMap[indexes[z]])
        self.c_means_map = point_map
        
    def uniqueRdmPnts(self, numToMake):
        l = []
        for x in range(0,numToMake):
            unique = False
            while not unique:
                index = rd.randint(0,len(self.d_map))
                if index not in l:
                    l.append(index)
                    unique = True
        return l

    def calcCentoids(self):
        children = []
        for k in self.d_set:
            pointBelongsToo = data_point('','')
            shortestDist = 9223372036854775807
            for i in self.c_means_map:
                if(self.euclidian(k.data,i.data) < shortestDist):
                    pointBelongsToo = i
            children.append([k, pointBelongsToo])

        for cluster in self.c_means_map:    
            points = []
            for point in children:
                if(point[1] == cluster):
                    points.append(point[0])
            ind = self.c_means_map.index(cluster)
            self.c_means_map[ind].data = self.findAverage(points)

    def findAverage(self,points):
        newData = []
        for x in range (0,len(points[0].data)):
            newData.append(0)
            avg = []
            for point in points:
                avg.append(point.data[0])
            value = sum(avg) /len(avg)
            newData[x] = value
        return newData

    