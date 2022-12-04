"""
Spiraling Into Control
https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15a74
"""
from functools import lru_cache


def can_reach_center_with_desired_steps(k, room):
    if k < 0:
        return False
    if k == 0:
        if room == 1:
            return True
        else:
            return False
    return any(can_reach_center_with_desired_steps(k - 1, move) for move in get_valid_moves(room))


@lru_cache(maxsize=None)
def get_valid_moves(room):
    n = get_n(room)
    if is_shortcut_available(room, n):
        return [room - 1, get_shortcut(room, n)]
    else:
        return [room - 1]

def get_n(room):
    for n in range(3, 10000, 2):
        if room <= n ** 2:
            return n

def is_shortcut_available(room, n):
    normalized_room = room - (n - 2)**2
    return (normalized_room) % (n - 1) > 0 and normalized_room > 1

def get_shortcut(room, n):
    group = (room - (n - 2)**2) // (n - 1)
    shortcut_len = 4 * n - 11 + 2 * group
    return room - shortcut_len

# for room in range(2, 50):
#     print(f'{room}\t{get_n(room)}\t{get_valid_moves(room)}')

# assert not can_reach_center_with_desired_steps(9, 9)
# assert can_reach_center_with_desired_steps(8, 9)
# assert can_reach_center_with_desired_steps(7, 8)


t = int(input())
for i in range(1, t + 1):
    n, k = [int(x) for x in input().split(' ')]
    print(f"Case #{i}: {can_reach_center_with_desired_steps(k, n**2)}")