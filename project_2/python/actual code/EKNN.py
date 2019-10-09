import KNN
import numpy as np
from DATAPOINT import data_point
from POINTMAP import point_map

class edited_knn(KNN.k_nearest_neighbors):

    def __init__(self, in_k, dataset, alg):
        KNN.k_nearest_neighbors.__init__(self,in_k,dataset,alg)
        self.alg = alg # This is only used for clustering, but we declare it everywhere so the driver can handle everything
        # edited_set = self.edit_data_set(self.d_map.points)
        self.edit_two()
        


    def edited_class_remover(self,in_set):
        classless_data = []
        for point in in_set.points:
            classless_data.append(point.data[:])
        return classless_data


    def edit_two(self):
        prev_map = point_map([0]) # Instatiating this to length 1, so the while loop doesn't explode
        cur_map = self.d_map
        cur_iter = 0
        map_to_return = self.d_map
        while (abs(len(cur_map.points)-len(prev_map.points)) > int(round(len(self.d_map.points) * .4))): # This is maybe a little bit hacky, but basically it stops looping if the change in size between the previous and current runs are less than 4% of the size of the original set
            cur_iter += 1
            print("Iteration " + str(cur_iter))
            prev_map = cur_map
            temp_points = self.edited_class_remover(cur_map)
            cur_map = point_map(self.classify(temp_points))
            for i, point in enumerate(cur_map.points):
                if point.class_num != map_to_return.points[i].class_num: # This is also maybe a little hacky, but it prevents out of bounds errors after we start to remove points
                    cur_map.points.remove(point)
                    map_to_return.points.remove(map_to_return.points[i]) # This function got nastier and nastier as I tried to fix bugs. Sorry if it's horrible.
            

        self.d_map = cur_map


    def edit_data_set(self,data_to_edit):
        points_to_classify = []
        nearest = []
        for line in data_to_edit:
            points_to_classify.append(data_point(line.data[:], ''))

        
        for i in range(len(points_to_classify)):
            nearest = self.get_k_nearest(points_to_classify[i])
            nearest = sorted(nearest, key= lambda l:l[1], reverse=True)
            #occurence_length = int(nearest[0][1])
            #occurence_counter = [0 for i in range(occurence_length)]
            occurrence_counter = np.full(50,0) # This is declared ahead of time to avoid any potential issues with out of bounds errors that might occur if dynamically declaring
            for i in range(len(self.d_map.points)):
                occurrence_counter[int(nearest[i][-1])] += 1 # We cast this particular index to int, since no classes in these sets are of float value
            max_occurrence = np.argmax(occurrence_counter)
            points_to_classify[i].class_num = max_occurrence
            if data_to_edit[i].class_num != points_to_classify[i].class_num:
                points_to_classify.remove(points_to_classify[i])

        print(len(points_to_classify))
        return points_to_classify