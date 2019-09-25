# K Nearest Neighbors 

### DataPoint - an element/instance from the input data set, put into an object
data: float[] - values of features  
classType: int -  the class of the data


### Map - holds all the DataPoints
nearK: integer - hyperparameter for tuning the algorithm. It is the number of nearest neighbors (which we choose) for which the map looks for  
points: DataPoint[] - a list of all the points, essentially the map  

generate() - creates the map (named points) from all the training data.   
classify() - This will classify an unknown datapoint. Classification will likely happen by calling getKNearest(), then euclidian() on each of the nearest neighbors and the unknown point. Then the most likely class is calculated and the classType of the dataPoint is updated. 
euclidian() - calculates and the euclidian distance between two points  
getKNearest() - returns a list of the K nearest points