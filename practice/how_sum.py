"""
https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1638s
"""
import functools

@functools.lru_cache(maxsize=None)
def how_sum(target, numbers):
    if target < 0:
        return None
    elif target == 0:
        return []
    for number in numbers:
        ret = how_sum(target - number, numbers)
        if ret is not None:
            return ret + [number]

print(how_sum(8, (5, 3)))
