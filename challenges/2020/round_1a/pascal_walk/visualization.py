import matplotlib.pyplot as plt
from tqdm import tqdm

from code import find_pascal_walk

def plot_walk(walk_length):
    walk = find_pascal_walk(int(walk_length))
    x = [i[1] - i[0]/2  for i in walk]
    y = [i[0] for i in walk]
    for r, k in tqdm(walk):
        plt.text(k - r/2, r, get_cell_number(r, k))
    plt.plot(x, y, marker='o')
    plt.plot([0.5, walk[-1][0]/2, 1-walk[-1][0]/2, 0.5], [1, walk[-1][0], walk[-1][0], 1], color='orange', alpha=0.5)
    plt.ylabel('Row')
    plt.xlabel('k')
    plt.title(f'Pascal walk for length: {walk_length}')
    plt.show()

def get_cell_number(r, k):
    if k == 1 or k == r:
        return 1
    return get_cell_number(r - 1, k - 1) + get_cell_number(r - 1, k)

# 18, 17, 9, 5
walk_length = 5e2
plot_walk(walk_length)