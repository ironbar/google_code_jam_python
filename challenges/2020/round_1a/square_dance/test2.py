import time
import numpy as np


from code import get_competition_interest


np.random.seed(7)
for cols, rows in [(10, 10), (10, 20), (20, 20), (20, 40), (40, 40), (40, 80), (80, 80)]:
    times = []
    for _ in range(100):
        dance_floor = np.random.randint(1, int(1e6), size=(rows, cols))
        start = time.time()
        get_competition_interest(dance_floor)
        times.append(time.time() - start)
    average_time = sum(times) / len(times) * 1000
    print(f"Average time for {cols}x{rows} dance floor: {average_time:.1e} ms, time constant: {average_time / (rows * cols):.1e} ms")

"""
With random dance floors the order is O(RC)
Average time for 10x10 dance floor: 2.8e+00 ms, time constant: 2.8e-02 ms
Average time for 10x20 dance floor: 4.7e+00 ms, time constant: 2.3e-02 ms
Average time for 20x20 dance floor: 6.9e+00 ms, time constant: 1.7e-02 ms
Average time for 20x40 dance floor: 1.2e+01 ms, time constant: 1.4e-02 ms
Average time for 40x40 dance floor: 1.7e+01 ms, time constant: 1.1e-02 ms
Average time for 40x80 dance floor: 2.6e+01 ms, time constant: 8.0e-03 ms
Average time for 80x80 dance floor: 3.9e+01 ms, time constant: 6.2e-03 ms
"""
