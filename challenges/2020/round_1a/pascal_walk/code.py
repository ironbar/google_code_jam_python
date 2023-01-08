"""
Pascal walk
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353

The sum of all the elements of row r is 2**(r-1). For example:

| r | sum |
|---|-----|
| 1 | 1   |
| 2 | 2   |
| 3 | 4   |
| 4 | 8   |
| 5 | 16  |

In the worst case we are asked to reach a value of 1e9. 2**30 is the closest value to 1e9. So we could
reach that number just by going down to row 30 and then going right 30 times. So there is a lot of
room because we are allowed to go move up to 500 steps.

We might take each number and transform it into a binary number. Then we can go down the pascal triangle
and only loop over the rows that have a 1 in the binary representation of the number.
However there is a problem because when we go down we have to pass over rows that are not included in
the binary representation and they sum 1.

Maybe I can solve it iteratively. When I reach a certain row if that row is inside the binary representation
of the remaining path. I could test this for smaller numbers and if it works it might work for larger numbers.

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""

def find_pascal_walk(path_length):
    walk = [[1, 1]]
    path_length -= 1
    while len(walk) < 500 and path_length > 0:
        row = walk[-1][0] + 1
        bin_representation = bin(path_length)[2:][::-1]
        if len(bin_representation) > row - 1 and bin_representation[row - 1] == "1":
            row_cells = [[row, i + 1] for i in range(row)]
            if walk[-1][1] == 1:
                walk.extend(row_cells)
            else:
                walk.extend(row_cells[::-1])
            path_length -= 2 ** (row - 1)
        else:
            if walk[-1][1] == 1:
                walk.append([row, 1])
            else:
                walk.append([row, walk[-1][1] + 1])
            path_length -= 1
    return walk


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        path_length = int(input())
        print(f"Case #{i}:")
        for step in find_pascal_walk(path_length):
            print(" ".join(map(str, step)))

