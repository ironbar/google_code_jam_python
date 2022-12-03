"""
url_of_challenge_here
"""
import numpy as np
import scipy

def main(numbers):
    return None


t = int(input())
for i in range(1, t + 1):
    numbers = [int(x) for x in input().split(' ')]
    print(f"Case #{i}: {main(numbers)}")