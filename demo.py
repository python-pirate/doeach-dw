import random

def max_min(arr):
    j = 1
    max = 0
    while j < len(arr):
        if arr[j] > arr[max]:
            max = j
        j += 1
    return arr[max]


def select_sort(arr):
    i = len(arr)
    while i > 1:
        j = 1
        max = 0
        while j < i:
            if arr[j] > arr[max]:
                max = j
            j += 1

        if max != i - 1:
            arr[max], arr[i - 1] = arr[i - 1], arr[max]
        i -= 1
