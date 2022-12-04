"""
title_of_the_problem_here
url_of_problem_here

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""
from functools import lru_cache
import numpy as np
import scipy


def main(numbers):
    return None


t = int(input())
for i in range(1, t + 1):
    numbers = [int(x) for x in input().split(' ')]
    print(f"Case #{i}: {main(numbers)}")