import KNN

class edited_knn(KNN.k_nearest_neighbors):

    def __init__(self, in_k, dataset):
        KNN.k_nearest_neighbors.__init__(self,in_k,dataset)
        self.edited_set = []


    def edit_data_set(self,):
        points_to_classify = []
        nearest = []
        occurrence_counter = []
        for line in data_to_classify:
            points_to_classify.append(data_point(line[:], ''))

        for point in points_to_classify:
            nearest = self.get_k_nearest(point)
            nearest = sorted(nearest, key= lambda l:l[1], reverse=True)
            occurence_length = int(nearest[0][1])
            occurence_counter = [0 for i in range(occurence_length)]
            for i in range(length(self.d_map)):
                occurence_counter[int(nearest[i][1] - 1)] += 1 # We cast this particular index to int, since no classes in these sets are of float value
            max_occurrence = np.argmax(occurence_counter)
            point.class_type = max_occurrence

        return points_to_classify