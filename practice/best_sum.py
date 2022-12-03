"""
https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1638s
"""
import functools

@functools.lru_cache(maxsize=None)
def best_sum(target, numbers):
    if target < 0:
        return None
    elif target == 0:
        return []
    candidates = []
    for number in numbers:
        ret = best_sum(target - number, numbers)
        if ret is not None:
            candidates.append(ret + [number])
    if candidates:
        return min(candidates, key=len)


print(best_sum(47, (5, 3)))
print(best_sum(47, (10, 5, 3)))
print(best_sum(47, (3, 5, 10)))