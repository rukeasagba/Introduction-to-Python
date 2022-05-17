#Assignment 3
#Question 1

def Average(data): 
    avg = sum(data) / len(data) 
    return avg
  
data = [28,42,67,89,100] 
average = Average(data) 
  
print("The mean is", average)
    

#Question 2

def get_median(data):
    # sort the list
    data_sorted = data.sort()
    # find the median
    if len(data) % 2 != 0:
        # total number of values are odd
        # subtract 1 since indexing starts at 0
        m = int((len(data)+1)/2 - 1)
        return data[m]
    else:
        m1 = int(len(data)/2 - 1)
        m2 = int(len(data)/2)
        return (data[m1]+data[m2])/2
# create a list
data = [28,42,67,89,100] 
# get the median
print("The median is", get_median(data))

#Question 3

def variance(data):
# Number of observations
    n = len(data)
# Mean of the data
    mean = sum(data) / n
# Square deviations
    deviations = [(x - mean) ** 2 for x in data]
# Variance
    variance = sum(deviations) / n
    return variance

data = [28,42,67,89,100] 
print("The variance is", variance(data))


#Question 4

def stdev(data):
    var = variance(data)
    std_dev = (var)**0.5
    return std_dev

data = [28,42,67,89,100] 
print("The standard deviation is", stdev(data))


#Question 5

def skew(data):
    skew_data = 3*(Average(data) - get_median(data))/stdev(data)
    return skew_data

data = [28,42,67,89,100] 
print("The skew is", skew(data))
