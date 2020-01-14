import random

def max_min(arr):
    j = 1
    max = 0
    while j < len(arr):
        if arr[j] > arr[max]:
            max = j
        j += 1
    return arr[max]

