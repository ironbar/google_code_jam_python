import time
import random


from code_v2 import get_competition_interest

random.seed(7)
for cols, rows in [(10, 10), (10, 20), (20, 20), (20, 40), (40, 40), (40, 80), (80, 80)]:
    times = []
    for _ in range(100):
        dance_floor = [[random.randint(1, int(1e6)) for _ in range(cols)] for _ in range(rows)]
        start = time.time()
        get_competition_interest(dance_floor)
        times.append(time.time() - start)
    average_time = sum(times) / len(times) * 1000
    print(f"Average time for {cols}x{rows} dance floor: {average_time:.1e} ms, time constant: {average_time / (rows * cols):.1e} ms")

"""
With random dance floors the order is O(RC)
Average time for 10x10 dance floor: 5.0e-01 ms, time constant: 5.0e-03 ms
Average time for 10x20 dance floor: 1.1e+00 ms, time constant: 5.3e-03 ms
Average time for 20x20 dance floor: 2.2e+00 ms, time constant: 5.4e-03 ms
Average time for 20x40 dance floor: 4.8e+00 ms, time constant: 6.0e-03 ms
Average time for 40x40 dance floor: 1.0e+01 ms, time constant: 6.5e-03 ms
Average time for 40x80 dance floor: 2.1e+01 ms, time constant: 6.4e-03 ms
Average time for 80x80 dance floor: 4.3e+01 ms, time constant: 6.7e-03 ms
"""
