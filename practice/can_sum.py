"""
https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1638s

Notice that I had to use tuples to be able to use memoization
"""
import functools

@functools.lru_cache(maxsize=None)
def can_sum(target, numbers):
    if target < 0:
        return False
    elif target == 0:
        return True
    return any(can_sum(target - number, numbers) for number in numbers)

assert can_sum(47, (5, 3))
assert not can_sum(300, (7, 14))
