import time
import numpy as np


from code import get_competition_interest

np.random.seed(7)
dance_floor = np.random.randint(1, int(1e6), size=(1000, 1000))
start = time.time()
print(get_competition_interest(dance_floor))
print(time.time() - start)
"""
Initial implementation takes 2.43 seconds
Replacing the convolutions by additons reduces the time to 1.42 seconds, but it's not enough to pass the challenge
"""