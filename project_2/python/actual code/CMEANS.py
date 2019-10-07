import numpy as np 
import random as rd 
import math
import EKNN

class c_means(EKNN.edited_knn):
    def __init__(self, k, numCentroids, dataMap):
        self.kNum = k
        EKNN.edited_knn(k, dataMap)
        self.numC = numCentroids
        self.data_Map = dataMap
        self.c_means_map = ''
    
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
                index = rd.randint(0,len(self.data_Map))
                if index not in l:
                    l.append(index)
                    unique = True
        return l

    def calcCentoids(self):
        children = []
        for k in self.data_Map:
            pointBelongsToo = self.data_point()
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
