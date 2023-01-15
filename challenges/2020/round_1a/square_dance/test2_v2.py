import time
import random


from code_v2 import get_competition_interest

random.seed(7)
dance_floor = [[random.randint(1, int(1e6)) for _ in range(1000)] for _ in range(1000)]
start = time.time()
assert get_competition_interest(dance_floor) == 1374291958697
print(time.time() - start)
"""
Initial implementation takes 8.46 seconds both with python and pypy
Thus it is slower than the numpy implementation
"""