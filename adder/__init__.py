import numpy as np


def add(x: np.int32, y: np.int32):
    return x + y

def sub(x, y):
    return x-y;

def divide(x,y):
    if(y!=0):
        return float(x)/float(y)
    else:
        return 0
