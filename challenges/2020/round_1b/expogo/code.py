"""
Expogo
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""

def get_shortest_path(goal):
    x, y = goal
    if x == 0 and y == 0:
        return ''
    if is_even(x + y):
        return 'IMPOSSIBLE'

    if is_odd(x):
        if is_odd(y//2):
            # choose the direction that makes x even
            if is_even((x + 1)//2):
                return 'W' + get_shortest_path([(x + 1)//2, y//2])
            else:
                return 'E' + get_shortest_path([(x - 1)//2, y//2])
        else:
            # see if we can finish
            if y == 0 and x + 1 == 0:
                return 'W' + get_shortest_path([(x + 1)//2, y//2])
            if y == 0 and x - 1 == 0:
                return 'E' + get_shortest_path([(x - 1)//2, y//2])
            # choose the direction that makes x odd
            if is_odd((x + 1)//2):
                return 'W' + get_shortest_path([(x + 1)//2, y//2])
            else:
                return 'E' + get_shortest_path([(x - 1)//2, y//2])
    else:
        if is_odd(x//2):
            # choose the direction that makes y even
            if is_even((y + 1)//2):
                return 'S' + get_shortest_path([x//2, (y + 1)//2])
            else:
                return 'N' + get_shortest_path([x//2, (y - 1)//2])
        else:
            # see if we can finish
            if x == 0 and y + 1 == 0:
                return 'S' + get_shortest_path([x//2, (y + 1)//2])
            if x == 0 and y - 1 == 0:
                return 'N' + get_shortest_path([x//2, (y - 1)//2])
            # choose the direction that makes x odd
            if is_odd((y + 1)//2):
                return 'S' + get_shortest_path([x//2, (y + 1)//2])
            else:
                return 'N' + get_shortest_path([x//2, (y - 1)//2])


def is_odd(n):
    return n % 2 == 1


def is_even(n):
    return n % 2 == 0


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        goal = [int(x) for x in input().split(' ')]
        shortest_path = get_shortest_path(goal)
        if shortest_path.endswith('IMPOSSIBLE'):
            shortest_path = 'IMPOSSIBLE'
        print(f"Case #{i}: {shortest_path}")
