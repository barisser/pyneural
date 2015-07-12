import math

def hash_to_int(hash):
    r = 1
    for x in hash:
        r = r * ord(x)
    return r
