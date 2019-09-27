# K Nearest Neighbors 

## Base KNN

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

can make a class for each variant of the function that we are running and have the methods specific to each classification/regression within that calss.

Perform edited nearest neighbors, the number of points that we get is C which is passed into both PAM and cmeans for each data set. Results from PAM and cmeans are used for regression or classification depending upon the data set. 

## Experimental Design   
| algorithm | Classification                                                           | Regression |
| --------- | ------------------------------------------------------------------------ | ---------- |
| Knn       | KNN will perfectly classify data points                                  |            |
| EKnn      | will produce fewer false classifications then KNN                        |            |
| Cknn      | will produce fewer false classifications then KNN                        |            |
| k-mean    | K-means before edited will produce fewer false classifications than Eknn |            |
| pam       | Pam before edited will produce fewer false classifications than Eknn     |            |

# Questions for tomorrow
TODO: Remove questions for tomorrow

> what is regression <-alex

> is our uml correct

> Some of the descriptions aren't entirely clear on the assignment. Does traning set mean the 9/10ths of the data that we get from running 10fcv, or is it actually *all* of the data?

> As none of us understand how math works, being a collection of philosophy, english, business and dance majors, how would we plot the points in our datasets?
