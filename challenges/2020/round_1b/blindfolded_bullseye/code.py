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
    try:
        x0, y0 = find_point_inside_dartboard(a)
        x, y = estimate_center_by_searching_edges(x0, y0)
        throw_darts_around_the_center(x, y)
    except Bullseye:
        return


def find_point_inside_dartboard(min_radius, max_x=int(1e9)):
    search_range = list(range(int(max_x//min_radius)))
    search_range = set(search_range + [-x for x in search_range])
    for x in search_range:
        for y in search_range:
            result = throw_dart(x, y)
            if result == 'CENTER':
                return None
            if result == 'HIT':
                return x, y


class Bullseye(Exception):
    pass


def throw_dart(x, y):
    print(x, y)
    sys.stdout.flush()
    result = input()
    if result == 'CENTER':
        raise Bullseye()
    return result


def estimate_center_by_searching_edges(x0, y0, max_x=int(1e9)):
    result = throw_dart(-max_x, y0)
    if result == 'HIT':
        left_edge = -max_x
    else:
        left_edge = binary_edge_search([x0, y0], [-max_x, y0])[0]

    result = throw_dart(max_x, y0)
    if result == 'HIT':
        right_edge = max_x
    else:
        right_edge = binary_edge_search([x0, y0], [max_x, y0])[0]

    result = throw_dart(x0, -max_x)
    if result == 'HIT':
        bottom_edge = -max_x
    else:
        bottom_edge = binary_edge_search([x0, y0], [x0, -max_x])[1]

    result = throw_dart(x0, max_x)
    if result == 'HIT':
        top_edge = max_x
    else:
        top_edge = binary_edge_search([x0, y0], [x0, max_x])[1]

    return (left_edge + right_edge)//2, (bottom_edge + top_edge)//2


def binary_edge_search(hit, miss):
    while manhattan_distance(hit, miss) > 1:
        new_throw = [(hit[0] + miss[0])//2, (hit[1] + miss[1])//2]
        result = throw_dart(*new_throw)
        if result == 'HIT':
            hit = new_throw
        else:
            miss = new_throw
    return hit


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def throw_darts_around_the_center(xc, yc):
    throw_dart(xc, yc)



if __name__ == '__main__':
    t, a, b = [int(x) for x in input().split(' ')]
    for i in range(1, t + 1):
        find_dartboard_center(a, b)