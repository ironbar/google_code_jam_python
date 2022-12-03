"""
Fibonacci without memoization has O(2^n) time complexity, with memoization it has O(n) time complexity.
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(51):
    print(n, fibonacci(n))