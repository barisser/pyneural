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
    a = np.ones((x, y))
    return a.multiply(a, 1.0/float(sum))

def random_array3d_sum(x, y, z, sum):
    a = random_array_range3d(x, y, z)
    d = np.multiply(a, 1.0/float(sum))
    return d

def logisticize_array(a):
    for i in range(0, len(a)):
        a[i] = logistic(a[i])
    return a

def change_base(n, digits, base):
    a = []
    while n > 0:
        r = n % base
        n = n - r
        n = n / base
        a.append(r)
    a = a[::-1]
    if len(a) < digits:
        a = [0] * (digits - len(a)) + a
    return np.asarray(a)

def base_to_n(b, base):
    b = b[::-1]
    n = 0
    s = 1
    for x in b:
        n = n + s * x
        s = s * base
    return n

def 2d_neg_array_to_pos_1d(a, r):
    a = a.flatten()
    b = len(a)
    c = np.ones((1, b))
    a = np.add(a, c)
    a = np.multiply(a, r / 2)
    return a
