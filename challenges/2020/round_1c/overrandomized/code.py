"""
Overrandomized
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1

- The server returns a random integer between 1 and M inclusive, M <= 10**U
- Each server replaces the digits by letters. For example CODEJAMFUN would be 0123456789
- The numbers don't have leading zeros, so that gives an easy way to find which letter is zero
- For each server we make 10**4 queries with random M ∈ [1, 10**U - 1]
- We are requested to recover the secret digit to letter translation

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""
from functools import lru_cache
import numpy as np
import scipy


def find_secret_string(queries, responses):
    return None


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        u = int(input())
        queries, responses = [], []
        for _ in range(10000):
            query, response = input().split(' ')
            queries.append(int(query))
            responses.append(response)
        print(f"Case #{i}: {find_secret_string(queries, responses)}")
