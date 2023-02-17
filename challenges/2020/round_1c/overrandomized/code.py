"""
Overrandomized
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1

- The server returns a random integer between 1 and M inclusive, M <= 10**U
- Each server replaces the digits by letters. For example CODEJAMFUN would be 0123456789
- The numbers don't have leading zeros, so that gives an easy way to find which letter is zero
- For each server we make 10**4 queries with random M ∈ [1, 10**U - 1]
- We are requested to recover the secret digit to letter translation

The key detail is that for the test set 3 there is no information about M. Thus the distribution
should not be random. The point is that if we concatenate two random distributions the output is not
random. There would be more numbers starting by 1 than 2, more starting than 2 than 3 and so on.

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""
import numpy as np


def find_secret_string(queries, responses):
    first_letters = [response[0] for response in responses]
    letters, counts = np.unique(first_letters, return_counts=True)
    secret = ''.join(letters[np.argsort(counts)[::-1]])

    last_letters = [response[-1] for response in responses]
    for letter in last_letters:
        if letter not in secret:
            secret = letter + secret
            break
    return secret


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
