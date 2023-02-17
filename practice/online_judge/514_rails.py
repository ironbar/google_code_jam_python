"""
514 Rails
https://onlinejudge.org/external/5/514.pdf
"""


def is_train_configuration_possible(train_conf):
    split_groups = find_split_groups(train_conf)
    print(split_groups)
    input_train_conf = []
    for group in split_groups:
        input_train_conf.extend(group[::-1])
    print(input_train_conf)
    if input_train_conf == list(range(1, len(train_conf) + 1)):
        return 'Yes'
    else:
        return 'No'


def find_split_groups(train_conf):
    groups = []
    current_group = []
    for coach, next_coach in zip(train_conf[:-1], train_conf[1:]):
        current_group.append(coach)
        if coach < next_coach:
            groups.append(current_group)
            current_group = []
    if current_group:
        if train_conf[-1] > current_group[-1]:
            groups.append(current_group)
            groups.append([train_conf[-1]])
        else:
            groups.append(current_group + [train_conf[-1]])
    else:
        groups.append([train_conf[-1]])
    return groups


def main():
    while 1:
        train_length = int(input())
        if train_length == 0:
            break
        while 1:
            train_conf = list(map(int, input().split()))
            if len(train_conf) != train_length:
                print()
                break
            print(is_train_configuration_possible(train_conf))


if __name__ == "__main__":
    main()