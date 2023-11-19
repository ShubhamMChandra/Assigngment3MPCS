#Shubham Chandra
#problem 6

from math import *

# points.txt
point1 = (20.900,15.300,20.400)
point2 = (0.600,34.700,8.100)
point3= (12.100,15.800,2.300)
point4=(15.000,5.800,16.900)
point_origin = (0,0,0)

all_tuples = [point1, point2, point3, point4]

#find distances between two points
def distance(tuple1, tuple2):
    #unpack tuples
    x1 = tuple1[0]
    y1 = tuple1[1]
    z1 = tuple1[2]
    x2 = tuple2[0]
    y2 = tuple2[1]
    z2 = tuple2[2]
    # calc distance between tuples
    non_sq_dist = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2)
    distance = sqrt(non_sq_dist)
    return distance

#find the minimum distance between all points
def min_distance(list):
    smallest_dist = 1000000 
    pointa = ""
    pointb = ""
    for point1 in list:
        for point2 in list:
            if point1 == point2:
                pass
            else:
                dist = distance(point1,point2)
                if dist < smallest_dist:
                    smallest_dist = dist
                pointa = point1
                pointb = point2
    return (pointa, pointb) 

print(min_distance(all_tuples)) #returns ((15.0, 5.8, 16.9), (12.1, 15.8, 2.3)) aka points 3 and 4


#find distance between all points and any specified point (we will use origin below)
def min_distance_single(list,single):
    smallest_dist = 1000000
    pointa = ""
    for point1 in list:
        dist = distance(point1,point_origin)
        if dist< smallest_dist:
            smallest_dist = dist
            pointa = point1
    return (point1) 

print(min_distance_single(all_tuples,point_origin)) #returns 15.0,5.8,16.9 aka point 4 is closest to origin
