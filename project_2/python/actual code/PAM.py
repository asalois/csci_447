import EKNN 
import random as rd 
from DATAPOINT import data_point

class pam(EKNN.edited_knn) : 
    def __init__(self, in_k, data_set, alg):
        EKNN.edited_knn.__init__(self,in_k,data_set,alg)
        self.pam_map =''
        if alg == 1: # doing regression so use 1/4 the size of the dataset
            self.num_medoids = int(round(len(data_set)/4))
        else : # otherwise use the size of the map (the final number of points left over from EKNN)
            self.num_medoids = len(self.d_map.points)
    
    # randomly set the positions of the initial medoids given an array of the indexes
    def place_initial_medoids (self, indexes):
        med_map = []
        for x in range (0,len(indexes)):
            med_map.append(self.d_map[indexes[x]])
        self.pam_map = med_map
        
    # find the random points to use for the starting points ensuring no repetition
    def unique_random_points(self, num_to_make):
        rand_points = []
        for x in range(0,num_to_make):
            unique = False
            while not unique:
                index = rd.randint(0,len(self.d_map))
                if index not in rand_points:
                    rand_points.append(index)
                    unique = True
        return rand_points

    # the main loop of the algorithm 
    def recompute(self):
        max_passes = int(0.1 * len(self.d_set)) # max passes (if the medoids don't stop changing) to kick out equal to 10% the dataset (tuneable)

        while(max_passes > 0): # TODO include a way to break out when the distortion levels off
            data_distort_med = [] # TODO this is just a placeholder for now, it will also hold the datapoint and the medoid it belongs to
            # assign points to medoids
            for x in self.d_map: # TODO ensure this actually goes through all the points in the orginal dataset (in the form of datapoints), not the map from EKNN
                medoid_assigned_to = data_point('','')
                shortest_distance = 9223372036854775807
                for m in self.pam_map: # find which medoid the datapoint is closest to
                    dist = self.euclidian(x.data,m.data)
                    if(dist < shortest_distance):
                        medoid_assigned_to = m
                        shortest_distance = dist
                # TODO TODO track the assigned point and calculate and track its distortion(square of the shortest distance)
                # TODO TODO possibly make the indixes of the medoids part of the class so it can be edited and checked (swapped points cannot be medoids)
            #----
            max_passes -= 1
            # Testing
