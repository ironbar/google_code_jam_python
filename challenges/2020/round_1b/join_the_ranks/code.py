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

A        B
B   ->   A
C        C

The problem asks for the number of minimum operations to sort the deck, and for the sequence that sorts the deck. The operation are encoded by the A and B values.

After manually solving the provided samples I have the feeling that the heuristic to solve this problem
is to first focus on the bottom of the deck. We need to select A and B so we send the lower rank cards
to the bottom of the deck. This should be easy to code, but I don't know if it's optimal.

https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/
This blog talks about sorting algorithms but does not say anything about optimality

In the analysis there is an explanation of how optimality is verified.
On a first step they approach the problem from the perspective of the number of adjacent cards with
different ranks. At the start this number is `R*S - 1`, all the cards are next to another of a different rank.
When the deck is sorted this number is reduced to `R -1`.
When performing the sorting operation we can decrease this number by at most two.
So to get from `R*S - 1` to `R -1` we need at least `ceil((R*S - R)/2)` operations.
That is the lower bound. If we can find a method that is guaranteed to work with that number of operations
the problem is solved.

So they find a lower bound and then they look for a method that works in that lower bound.

Why did they choose that representation of the problem?
It is true that reducing the number of adjacent cards with different ranking will results in clusters of
the same value. But we also have to consider the order of the clusters.
They may have chosen that representation because the sorting operation modifies the adjacent cards.

They say that they are going to apply the operations while maintaining this rule. For two consecutive
cards X, Y either `Y = X` (already grouped) or `Y = (X + 1) % R`. This will ensure that when we minimize
the differences between adjacent cards the deck will be sorted.

I had to spend an entire morning on this problem. And strangely it only passes test set 1.

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""


def optimal_sort(r, s):
    deck = []
    for _ in range(s):
        deck.extend(list(range(1, r + 1)))
    operations = []
    while number_of_different_adjacent_cards(deck) > r - 1:
    # for _ in range(2):
        a, b = find_a_and_b(deck)
        # print(deck, a, b)
        deck = valid_operation(a, b, deck)
        operations.append([a, b])
    # print(deck)
    return operations


def number_of_different_adjacent_cards(deck):
    number = 0
    for i in range(len(deck) - 1):
        if deck[i] != deck[i + 1]:
            number += 1
    return number


def find_a_and_b(deck):
    """
    We repeatedly perform the following operation, as long as the number of adjacent pairs of cards of the same rank is less than R - 1 and the operation would not pick up the bottom card of the deck: find the largest block of consecutive cards from the top that contains exactly 2 different ranks to use as pile A. By the invariant, this will be one or more cards with rank X, followed by one or more cards with rank (X+1) mod R. Then, starting from the first card from the top that is not on pile A, take as pile B the largest block of consecutive cards that does not contain any cards of rank X, plus all consecutive cards of rank X that immediately follow that block. Notice that at least one such card of rank X must exist; otherwise, by the invariant, the number of adjacent pairs of cards of different ranks would already be R-1.

    We can show that this operation reduces the number of adjacent cards of different ranks by 2 every time it does not pick up the bottom card of the deck. To show this, notice that the bottom of pile B is a card of rank X and the first card left over in the deck is, by the invariant, (X + 1) mod R. That means that the new adjacent pairs are two cards of rank X (the bottom of pile B and the top of pile A) and two cards of rank (X + 1) mod R (the bottom of pile A and the top of the leftover deck). The broken adjacent pairs are — by definition of piles A and B — both of cards of different rank. Therefore, the number of adjacent pairs of cards of different rank decreases by 2 with this operation.

    Suppose that performing the operation would pick up the bottom card of the deck. That means that all cards of rank X are in two contiguous blocks at the top and bottom of the deck before the operation is performed. In addition, since this is the first time the bottom card of the deck is picked up for an operation, X = R. Because of the invariant, that requires every other rank to be in a single contiguous block. In this ordering, there are exactly R adjacent pairs of cards with different ranks. Instead of the operation above, we finish by making pile A consist of the largest block of consecutive cards of rank R, starting at the top, and pile B be the rest of the deck. After performing the operation, R - 1 pairs of adjacent cards of different ranks remain (by a similar argument as before, ignoring the broken and created pairs that involved the leftover deck, since there is none leftover) and the final card of the deck is still R.
    """
    x = deck[0]
    y = None
    for idx, value in enumerate(deck):
        if y is None:
            if value == x:
                continue
            else:
                y = value
        else:
            if value == y:
                continue
            else:
                break
    a = idx

    b = None
    is_x_found = False
    for idx, value in enumerate(deck[a:]):
        if not is_x_found:
            if value == x:
                is_x_found = True
        else:
            if value != x:
                b = idx
                break

    # special ending case
    if b is None:
        for idx, value in enumerate(deck):
            if value != x:
                a = idx
                break
        return a, len(deck) - a
    return a, b



def valid_operation(a, b, deck):
    return deck[a:a+b] + deck[:a] + deck[a+b:]




if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        r, s = [int(x) for x in input().split(' ')]
        operations = optimal_sort(r, s)
        print(f"Case #{i}: {len(operations)}")
        for operation in operations:
            print(f'{operation[0]} {operation[1]}')
