"""
Square dance
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""
import numpy as np
import scipy.ndimage


def get_competition_interest(dance_floor):
    # print(dance_floor)
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
    # make a convolution with cells above, below, left and right
    kernel = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    neighbors_average_skill = scipy.ndimage.convolve(dance_floor*is_alive, kernel, mode='constant', cval=0.0)
    n_neighbors = scipy.ndimage.convolve(is_alive, kernel, mode='constant', cval=0.0)
    n_neighbors = np.maximum(n_neighbors, 1)
    neighbors_average_skill = neighbors_average_skill.astype(float)/n_neighbors
    print()
    print(dance_floor)
    print(is_alive)
    print(neighbors_average_skill)
    eliminated_competitors = np.logical_and(dance_floor < neighbors_average_skill, is_alive)
    return eliminated_competitors


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        r, c = [int(x) for x in input().split(' ')]
        dance_floor = np.array([[int(x) for x in input().split(' ')] for _ in range(r)], dtype=int)
        print(f"Case #{i}: {get_competition_interest(dance_floor)}")