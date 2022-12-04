"""
Spiraling Into Control
https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15a74
"""
import sys
sys.setrecursionlimit(10000)
from functools import lru_cache


def can_reach_center_with_desired_steps(k, room):
    if k == 0:
        if room == 1:
            return True, []
        else:
            return False, []

    shortcut = get_shortcut(room)
    if shortcut is not None:
        can_reach, path = can_reach_center_with_desired_steps(k - 1, shortcut)
        if can_reach:
            return True, path + [[room, shortcut]]
    return can_reach_center_with_desired_steps(k - 1, room - 1)

@lru_cache(maxsize=None)
def get_shortcut(room):
    n = get_n(room)
    if is_shortcut_available(room, n):
        group = (room - (n - 2)**2) // (n - 1)
        shortcut_len = 4 * n - 11 + 2 * group
        return room - shortcut_len

def get_n(room):
    for n in range(3, 10000, 2):
        if room <= n ** 2:
            return n

def is_shortcut_available(room, n):
    normalized_room = room - (n - 2)**2
    return (normalized_room) % (n - 1) > 0 and normalized_room > 1



# for room in range(2, 50):
#     print(f'{room}\t{get_n(room)}\t{get_valid_moves(room)}')

# assert not can_reach_center_with_desired_steps(9, 9)
# assert can_reach_center_with_desired_steps(8, 9)
# assert can_reach_center_with_desired_steps(7, 8)

assert not can_reach_center_with_desired_steps(3, 5**2)[0]
assert can_reach_center_with_desired_steps(4, 5**2)[0]
assert not can_reach_center_with_desired_steps(5, 5**2)[0]
assert can_reach_center_with_desired_steps(6, 5**2)[0]

for n in range(3, 10000, 2):
    print(n)
    assert can_reach_center_with_desired_steps(n - 1, n**2)[0]
    assert not can_reach_center_with_desired_steps(n - 2, n**2)[0]


t = int(input())
for i in range(1, t + 1):
    n, k = [int(x) for x in input().split(' ')]
    can_reach, path = can_reach_center_with_desired_steps(k, n**2)
    if can_reach:
        print(f"Case #{i}: {len(path)}")
        for room, shortcut in path[::-1]:
            print(f"{n**2 - room + 1} {n**2 - shortcut + 1}")
    else:
        print(f"Case #{i}: IMPOSSIBLE")
