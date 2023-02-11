"""
Overexcited fan
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/0000000000317409

- The city is a grid of streets with all the blocks of the same size.
- Peppurr's tour starts at an intersection that is X blocks east and Y blocks north of the intersection where you are currently located.
- Peppurr moves one block each turn
- We can move one block or stand still
- Peppur trajectory is known

¿Can we intercept Peppur? ¿In how many turns?

I believe this is pretty easy. We can compute the manhattan distance to the origin from Peppur at
each turn. If the distance is equal or smaller to the turn then we could reach that position.

I have been able to solve this challenge in around 23 min

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""

def get_minimun_number_of_turns_to_intercept_peppur(x, y, trajectory):
    for idx, direction in enumerate(trajectory):
        x, y = update_position(x, y, direction)
        manhattan_distance = abs(x) + abs(y)
        turn = idx + 1
        if manhattan_distance <= turn:
            return turn
    return 'IMPOSSIBLE'


def update_position(x, y, direction):
    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    return x, y


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        x, y, trajectory = [x for x in input().split(' ')]
        x, y = int(x), int(y)
        print(f"Case #{i}: {get_minimun_number_of_turns_to_intercept_peppur(x, y, trajectory)}")