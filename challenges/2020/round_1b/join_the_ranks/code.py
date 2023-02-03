"""
Join the ranks
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b64

R: Rank
S: Suit
R*S number of total cards, all unique
(r, s) is how a card is represented

The deck is sorted. First by suit, second by rank. The order is increasing.
Thus given any R, S we can recreate the initial state of the deck.

We want to reorder the deck by rank, without caring about the suit.
This simplifies the state representation because we can remove the suit information.

To reorder the deck we can only apply this special operation:

1. Take A cards from the top with A>=1
2. Take B cards from the remaining deck with B>=1
3. Place the A cards on the top of the remaining deck (C)
4. Place the B cards on the top of A+C deck

The problem asks for the number of minimum operations to sort the deck, and for the sequence that sorts the deck. The operation are encoded by the A and B values.

After manually solving the provided samples I have the feeling that the heuristic to solve this problem
is to first focus on the bottom of the deck. We need to select A and B so we send the lower rank cards
to the bottom of the deck. This should be easy to code, but I don't know if it's optimal.

Elapsed time so far: 35 min

TODO: implement code with that approach and see if it works
TODO: read this blog about sorting algorithms https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/

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


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        numbers = [int(x) for x in input().split(' ')]
        print(f"Case #{i}: {main(numbers)}")