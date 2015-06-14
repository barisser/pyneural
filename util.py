import random
import numpy as np
import math

def random_range():
    return random.random()*2-1.0

def random_array_range(x, y):
    a = np.random.rand(x, y)
    c = np.ones((x, y))
    b = np.multiply(a, 2)
    d = np.subtract(b, c)
    return d

def random_array_range3d(x, y, z):
    a = np.random.rand(x, y, z)
    c = np.ones((x, y, z))
    b = np.multiply(a, 2)
    d = np.subtract(b, c)
    return d

def logistic(x):
    return (1.0 / (1.0 + math.pow(2.7, -1 * x)))

def ones_array_sum(x, y, sum):
    a = np.ones((x,y))
    return a.multiply(a, 1.0/float(sum))

def random_array3d_sum(x,y,z, sum):
    a = random_array_range3d(x,y,z)
    d = np.multiply(a, 1.0/float(sum))
    return d

def logisticize_array(a):
    for i in range(0, len(a)):
        a[i] = logistic(a[i])
    return a
