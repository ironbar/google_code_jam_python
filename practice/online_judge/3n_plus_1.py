import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def get_3n_plus_1_sequence(n):
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [n] + get_3n_plus_1_sequence(n // 2)
    else:
        return [n] + get_3n_plus_1_sequence(3 * n + 1)


def main():
    for line in sys.stdin:
        i, j = map(int, line.split())    # For each input line
        sequences = []
        for n in range(i, j + 1):
            sequences.append(get_3n_plus_1_sequence(n))
        max_cycle_length = max(map(len, sequences))
        print(f"{i} {j} {max_cycle_length}")


if __name__ == "__main__":
    main()