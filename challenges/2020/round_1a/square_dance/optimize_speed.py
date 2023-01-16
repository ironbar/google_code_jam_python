"""
rm profile.prof; python -m cProfile -o profile.prof optimize_speed.py; snakeviz profile.prof
"""
from code_v3 import get_competition_interest


def create_hard_dance_floor(rows, cols):
    dance_floor = [list(range(1, cols + 1))]
    for i in range(1, rows):
        dance_floor.append([1 for _ in range(cols)])
        dance_floor[-1][-1] = i + cols
    return dance_floor


dance_floor = create_hard_dance_floor(300, 300)
get_competition_interest(dance_floor)