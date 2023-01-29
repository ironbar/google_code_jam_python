"""
Blindfolded Bullseye
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b63

If I miss a shot then I know that the center is not within a circle of radius A.
In the other hand if I hit a shot then I know that the center is within a circle of radius B.
I have a limit of memory of 1GB, so I can't store all the points in memory.



# run the script with input data
python interactive_runner.py python3 testing_tool.py 0 -- python3 code.py
"""
import sys

def find_dartboard_center(a, b):
    lower_limit = int(-1e9 + a)
    upper_limit = int(1e9 - a + 1)
    for x in range(lower_limit, upper_limit):
        for y in range(lower_limit, upper_limit):
            print(x, y)
            sys.stdout.flush()
            result = input()
            if result == 'CENTER':
                return


if __name__ == '__main__':
    t, a, b = [int(x) for x in input().split(' ')]
    for i in range(1, t + 1):
        find_dartboard_center(a, b)