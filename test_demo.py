from demo import *
import random

def test_max_min():
    arr = []
    for b in arr:
        arr.append(random.randint(10, 100))

    max = mix_min(arr)
    for x in arr:
        assert(max >= x)
        