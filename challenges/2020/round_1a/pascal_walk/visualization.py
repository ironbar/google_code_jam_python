import matplotlib.pyplot as plt

from code import find_pascal_walk

def plot_walk(walk):
    x = [i[1] for i in walk]
    y = [i[0] for i in walk]
    plt.plot(x, y, marker='o')
    for r, k in walk:
        plt.text(k, r, get_cell_number(r, k))
    plt.plot([1, walk[-1][0], 1, 1], [1, walk[-1][0], walk[-1][0], 1], color='red')
    plt.show()

def get_cell_number(r, k):
    if k == 1 or k == r:
        return 1
    return get_cell_number(r - 1, k - 1) + get_cell_number(r - 1, k)

walk = find_pascal_walk(int(1e8))
plot_walk(walk)