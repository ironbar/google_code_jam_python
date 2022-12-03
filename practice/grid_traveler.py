"""
https://www.youtube.com/watch?v=oBt53YbR9Kk

We can break down the problem into smaller subproblems, and store the results of each subproblem,
so that we don't have to recompute them when we need them again.
"""
import functools

@functools.lru_cache(maxsize=None)
def get_number_of_different_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return get_number_of_different_paths(m - 1, n) + get_number_of_different_paths(m, n - 1)


print(get_number_of_different_paths(3, 2))
for n in range(1, 10):
    print(n, get_number_of_different_paths(n ,n))
