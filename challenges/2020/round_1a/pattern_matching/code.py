"""
Pattern matching
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b3034

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""

def find_string_matching_all_patterns(patterns):
    suffixes = [p.split('*')[-1] for p in patterns]
    prefixes = [p.split('*')[0] for p in patterns]
    centers = [get_center_pattern(p) for p in patterns]
    common_suffix = find_common_suffix(suffixes)
    common_prefix = find_common_prefix(prefixes)
    if common_suffix is None or common_prefix is None:
        return '*'
    return common_prefix + ''.join(centers) + common_suffix


def find_common_suffix(suffixes):
    longest_suffix = max(suffixes, key=len)
    for suffix in suffixes:
        if not longest_suffix.endswith(suffix):
            return None
    return longest_suffix


def find_common_prefix(prefixes):
    longest_prefix = max(prefixes, key=len)
    for prefix in prefixes:
        if not longest_prefix.startswith(prefix):
            return None
    return longest_prefix


def get_center_pattern(pattern):
    splits = pattern.split('*')
    if len(splits) > 2:
        return ''.join(splits[1:-1])
    return ''


t = int(input())
for i in range(1, t + 1):
    n_patterns = int(input())
    patterns = [input() for _ in range(n_patterns)]
    print(f"Case #{i}: {find_string_matching_all_patterns(patterns)}")
