import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def get_3n_plus_1_cycle_length(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + get_3n_plus_1_cycle_length(n // 2)
    else:
        return 1 + get_3n_plus_1_cycle_length(3 * n + 1)


def main():
    for line in sys.stdin:
        i, j = map(int, line.split())
        sequences_length = []
        for n in range(min([i, j]), max(i, j) + 1):
            sequences_length.append(get_3n_plus_1_cycle_length(n))
        max_cycle_length = max(sequences_length)
        print(f"{i} {j} {max_cycle_length}")


if __name__ == "__main__":
    main()