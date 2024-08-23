import numpy as np

def sine(index, length_samples):
    return np.sin(2 * np.pi / length_samples * index)

def triangle(index, length_samples):
    if index < length_samples / 2:
        return -1 + (2 * (1 / (length_samples / 2))) * index
    else:
        return 3 - (2 * (1 / (length_samples / 2))) * index
    
def sawtooth(index, length_samples):
    return  1 - (1 / (length_samples / 2) * index)

def square(index, length_samples):
    if index < length_samples / 2:
        return 1
    else:
        return -1
        
    