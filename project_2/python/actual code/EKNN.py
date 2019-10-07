import KNN
import numpy as np
from DATAPOINT import data_point

class edited_knn(KNN.k_nearest_neighbors):

    def __init__(self, in_k, dataset):
        KNN.k_nearest_neighbors.__init__(self,in_k,dataset)
        edited_set = self.edit_data_set(self.d_map.points)
        self.d_map = edited_set


    def edit_data_set(self,data_to_edit):
        points_to_classify = []
        nearest = []
        occurrence_counter = []
        for line in data_to_edit:
            points_to_classify.append(data_point(line.data[:-1], ''))

        for point in enumerate(points_to_classify):
            nearest = self.get_k_nearest(point)
            nearest = sorted(nearest, key= lambda l:l[1], reverse=True)
            occurence_length = int(nearest[0][1])
            occurence_counter = [0 for i in range(occurence_length)]
            for i in range(len(self.d_map.points)):
                occurence_counter[int(nearest[i][1] - 1)] += 1 # We cast this particular index to int, since no classes in these sets are of float value
            max_occurrence = np.argmax(occurence_counter)
            point.class_type = max_occurrence
            if data_to_edit[point][-1] == point[-1]:
                points_to_classify.remove(point)

        print(len(points_to_classify))
        return points_to_classify