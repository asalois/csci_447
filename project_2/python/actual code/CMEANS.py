import numpy as np 
import random as rd 
import math
import EKNN

class c_means(EKNN.edited_knn):
    def __init__(self, kNum, numCentroids, dataMap):
        self.kNum = kNum
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
                    l[x] = index
                    unique = True
        return l

