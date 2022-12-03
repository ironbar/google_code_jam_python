"""
https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15a74
"""
import numpy as np
import scipy

def main(numbers):
    return None


t = int(input())
for i in range(1, t + 1):
    numbers = [int(x) for x in input().split(' ')]
    print(f"Case #{i}: {main(numbers)}")