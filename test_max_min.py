from demo import *
import random

def test_max_min():
    for _ in range(10000):
        arr = []
        for _ in range(10):
            arr.append(random.randint(10, 99))

        max = max_min(arr)
        for x in arr:
            assert(max >= x)
        
def test_select_sort():
    for _ in range(100000):
        j = 0
        arr = [random.randint(10, 99) for _ in range(10)]
        select_sort(arr)
        
        while j < len(arr) - 1:
            assert(arr[j] <= arr[j + 1])
            j += 1


