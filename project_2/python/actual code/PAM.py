import EKNN 
import random as rd 
from DATAPOINT import data_point

class pam(EKNN.edited_knn) : 
    def __init__(self, in_k, data_set, alg):
        EKNN.edited_knn.__init__(self,in_k,data_set,alg)
        self.pam_map ='' # THIS ISN'T actually a MAP, its a list of points
        if alg == 1: # doing regression so use 1/4 the size of the dataset
            self.num_medoids = int(round(len(data_set)/4))
        else : # otherwise use the size of the map (the final number of points left over from EKNN)
            self.num_medoids = len(self.d_map.points)
        self.generate() # remake the map of all points (instead of using what was made in EKNN)
    
    # randomly set the positions of the initial medoids given an array of the indexes
    def place_initial_medoids (self, indexes):
        med_map = []
        for x in range (0,len(indexes)):
            med_map.append(self.d_map.points.pop([indexes[x]]))
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
        max_passes = int(0.1 * len(self.d_set)) # max passes (if the medoids don't stop changing) to kick out equal to 10% the dataset (tunable)
        distortion = 9223372036854775807 # this is the maximum integer value for the system, and is also used below
        distortion_prime = 9223372036854775807
        old_distortion = 9223372036854775807

        while(max_passes > 0):
            data_distort_med = []
            # assign points to medoids
            for x in self.d_map.points: 
                medoid_assigned_to = data_point('','')
                shortest_distance = 9223372036854775807
                for m in self.pam_map: # find which medoid the datapoint is closest to
                    dist = self.euclidian(x,m)
                    if(dist < shortest_distance):
                        medoid_assigned_to = m
                        shortest_distance = dist
                data_distort_med.append([x,shortest_distance,medoid_assigned_to])
                distortion += shortest_distance # calculate the distortion while finding closest (distances are unsquared)
            # swap-a-roo
            for m in range(len(self.pam_map)):
                for x in range(len(data_distort_med)):
                    #swap points
                    temp_point = self.pam_map[m]
                    self.pam_map[m] = data_distort_med[x][0]
                    data_distort_med[x][0] = temp_point
                    #calc distortion
                    for i in data_distort_med:
                        if(i[-1] != temp_point): # if the medoid wasn't changed then the distance hasn't changed
                            distortion_prime += i[1]
                        else:
                            distortion_prime += self.euclidian(self.pam_map[m],i[0])
                    #if distortion is not decreased then swap back
                    if distortion <= distortion_prime:
                        temp_point = self.pam_map[m]
                        self.pam_map[m] = data_distort_med[x][0]
                        data_distort_med[x][0] = temp_point
                    else:
                        distortion = distortion_prime
            
            if ((old_distortion-distortion)/distortion) < 0.01 :
                break
            max_passes -= 1
            old_distortion = distortion
        self.d_map.points = self.pam_map