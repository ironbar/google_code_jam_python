"""
Square dance
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355

I have the intuition that I have to use the matrix structure to preserve the location of the competitors.
My idea is to compute the average skill of the neighbors row by row, and then transpose and do the same for the columns. I will index using the alive competitors.
I believe this will work although I'm not sure if it will be efficient enough.

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""
import numpy as np


def get_competition_interest(dance_floor):
    is_alive = np.ones_like(dance_floor)
    interest = 0
    while True:
        interest += np.sum(dance_floor*is_alive)
        eliminated_competitors = get_eliminated_competitors(dance_floor, is_alive)
        if np.sum(eliminated_competitors) == 0:
            break
        is_alive[eliminated_competitors] = 0
    return interest


def get_eliminated_competitors(dance_floor, is_alive):
    neighbors_average_skill = get_neighbors_average_skill(dance_floor, is_alive)
    eliminated_competitors = np.logical_and(dance_floor < neighbors_average_skill, is_alive)
    return eliminated_competitors


def get_neighbors_average_skill(dance_floor, is_alive):
    row_n_neighbors, row_neighbors_sum_skill = get_row_neighbors_sum_skill(dance_floor, is_alive)
    col_n_neighbors, col_neighbors_sum_skill = get_row_neighbors_sum_skill(dance_floor.T, is_alive.T)
    n_neighbors = row_n_neighbors + col_n_neighbors.T
    neighbors_sum_skill = row_neighbors_sum_skill + col_neighbors_sum_skill.T
    n_neighbors = np.maximum(n_neighbors, 1)
    neighbors_average_skill = neighbors_sum_skill.astype(float)/n_neighbors
    return neighbors_average_skill


def get_row_neighbors_sum_skill(dance_floor, is_alive):
    n_neighbors = np.zeros_like(dance_floor)
    neighbors_sum_skill = np.zeros_like(dance_floor)
    for i in range(dance_floor.shape[0]):
        is_alive_condition = is_alive[i] == 1
        is_alive_indices = np.arange(dance_floor.shape[1])[is_alive_condition]
        n_neighbors[i, is_alive_indices[1:]] += 1
        n_neighbors[i, is_alive_indices[:-1]] += 1
        neighbors_sum_skill[i, is_alive_indices[1:]] += dance_floor[i, is_alive_indices[:-1]]
        neighbors_sum_skill[i, is_alive_indices[:-1]] += dance_floor[i, is_alive_indices[1:]]
    return n_neighbors, neighbors_sum_skill



if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        r, c = [int(x) for x in input().split(' ')]
        dance_floor = np.array([[int(x) for x in input().split(' ')] for _ in range(r)], dtype=int)
        print(f"Case #{i}: {get_competition_interest(dance_floor)}")