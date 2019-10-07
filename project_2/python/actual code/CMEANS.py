import numpy as np 
import random as rd 
import math
from EKNN import edited_knn

class c_means():
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
        for z in range(0,numToMake):
            unique = False
            while not unique:
                index = rd.randint(0,len(self.data_Map))
                if index not in l:
                    l[-1] = index
                    unique = True
        return l
c = c_means()