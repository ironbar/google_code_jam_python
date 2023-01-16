import time
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

from code import get_competition_interest
from code_v2 import get_competition_interest as get_competition_interest_v2
from code_v3 import get_competition_interest as get_competition_interest_v3

def create_hard_dance_floor(rows, cols):
    dance_floor = [list(range(1, cols + 1))]
    for i in range(1, rows):
        dance_floor.append([1 for _ in range(cols)])
        dance_floor[-1][-1] = i + cols
    return dance_floor


functions = {
    'v1': get_competition_interest,
    'v2': get_competition_interest_v2,
    'v3': get_competition_interest_v3,
}

for version, function in functions.items():

    random.seed(7)
    times = []
    cols_range = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 17, 18, 20, 22, 24, 26, 28, 31, 34, 37, 41, 45, 49, 53, 58, 64, 70, 76, 83, 91, 100, 109, 119, 130, 142, 155, 170, 185, 203, 221, 242, 264, 289, 316]
    for cols in tqdm(cols_range):
        # dance_floor = [[random.randint(1, int(1e6)) for _ in range(cols)] for _ in range(cols)]
        dance_floor = create_hard_dance_floor(cols, cols)
        start = time.time()
        function(dance_floor)
        times.append(time.time() - start)

    plt.scatter([x**2 for x in cols_range], times, label=version)

plt.legend(loc=0)
plt.xscale('log')
plt.yscale('log')
plt.grid(which='both')
plt.xlabel('cols*rows')
plt.ylabel('time (s)')
plt.show()
