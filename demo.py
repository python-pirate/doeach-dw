import random

def max_min(arr):
    j = 1
    max = arr[0]
    while j < len(arr):
        if arr[j] > max:
            max = arr[j]
        j += 1
    return max