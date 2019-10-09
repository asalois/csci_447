import EKNN 
import KNN # If the _init_ of this is changed this statement shouldn't be needed
import random as rd 
from DATAPOINT import data_point

class pam(EKNN.edited_knn) : 
    # numMedoids is an optional input. If no number is given this will run EKNN to determine the number of medoids
    def __init__(self, in_k, dataset, numMedoids = ''):
        """
        This is very likely to break right here. There is also a good chance that this if may 
        not be needed. Since the data map will have to be regenerated after EKNN uses it (because
        for some reason we don't store it in a different variable) EKNN can likely be _init_ed
        either way and a bool for if it will be used can be instantiated and used later.
        """
        if numMedoids == '': 
            EKNN.edited_knn.__init__(self,in_k,dataset)
            self.numMedoids = len(self.d_map)
        else :
            KNN.k_nearest_neighbors.__init__(self,in_k,dataset)
            self.numMedoids = numMedoids
        self.pamMap =''
    
    # randomly set the positions of the initial medoids given an array of the indexes
    def placeInitialMedoids (self, indexes):
        medMap = []
        for x in range (0,len(indexes)):
            medMap.append(self.d_map[indexes[x]])
        self.pamMap = medMap
        
    # find the random points to use for the starting points ensuring no repetition
    def uniqueRdmPnts(self, numToMake):
        randomPoints = []
        for x in range(0,numToMake):
            unique = False
            while not unique:
                index = rd.randint(0,len(self.d_map))
                if index not in randomPoints:
                    randomPoints.append(index)
                    unique = True
        return randomPoints

    # the main loop of the algorithm 
    def recompute(self):
        maxPasses = int(0.1 * len(self.d_set)) # max passes (if the medoids don't stop changing) to kick out equal to 10% the dataset (tuneable)

        while(maxPasses > 0): # TODO include a way to break out when the distortion levels off
            distortion = [] # TODO this is just a placeholder for now, it will also hold the datapoint and the medoid it belongs to
            # assign points to medoids
            for x in self.d_map: # TODO ensure this actually goes through all the points in the orginal dataset (in the form of datapoints), not the map from EKNN
                pointBelongsTo = data_point('','')
                shortestDist = 9223372036854775807
                unDistortion = 9223372036854775807
                for m in self.pamMap: # find which medoid the datapoint is closest to
                    dist = self.euclidian(x.data,m.data)
                    if(dist < shortestDist):
                        pointBelongsTo = m
                        shortestDist = dist
                # TODO TODO track the assigned point and calculate and track its distortion(square of the shortest distance)
                # TODO TODO possibly make the indixes of the medoids part of the class so it can be edited and checked (swapped points cannot be medoids)
            #----
            maxPasses -= 1
