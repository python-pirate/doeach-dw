from demo import *
import random

def test_max_min():
    for _ in range(1000):
        arr = []
        for _ in range(10):
            arr.append(random.randint(10, 99))

        max = max_min(arr)
        for x in arr:
            assert(max >= x)
        