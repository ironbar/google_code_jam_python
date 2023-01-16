"""
Square dance
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355

In this second version I will build using the information from the analysis. I will create a
data structure that will allow me to check only the dancers whose neighbors have changed. And also
it will allow to efficiently update the neighbors when dancers are eliminated.

My first implementation gets time limit exceeded for test 2. Both with python and pypy.

I might use https://jiffyclub.github.io/snakeviz/ to profile the code and see where the time is spent.

I have created the script `time_complexity.py` and both v1 and v2 are O(RC), thus it seems that
the problem is related to python, not to the time complexity of the algorithm.

I could try to create an v3 version that is faster.

# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
"""

def get_competition_interest(dance_floor):
    representation = create_efficient_representation(dance_floor)
    total_interest = 0
    current_interest = _get_competitors_skills(representation)
    competitors_to_check = set(representation.keys())
    while True:
        total_interest += current_interest
        eliminated_competitors = get_eliminated_competitors(representation, competitors_to_check)
        if not eliminated_competitors:
            break
        current_interest -= _get_competitors_skills(representation, eliminated_competitors)
        competitors_to_check = update_representation(representation, eliminated_competitors)
    return total_interest


def create_efficient_representation(dance_floor):
    representation = dict()
    rows, cols = len(dance_floor), len(dance_floor[0])
    for i in range(rows):
        for j in range(cols):
            representation[(i, j)] = {'skill': dance_floor[i][j]}
            if i > 0:
                representation[(i, j)]['up'] = (i-1, j)
            else:
                representation[(i, j)]['up'] = None
            if i < rows-1:
                representation[(i, j)]['down'] = (i+1, j)
            else:
                representation[(i, j)]['down'] = None
            if j > 0:
                representation[(i, j)]['left'] = (i, j-1)
            else:
                representation[(i, j)]['left'] = None
            if j < cols-1:
                representation[(i, j)]['right'] = (i, j+1)
            else:
                representation[(i, j)]['right'] = None
    return representation


def get_eliminated_competitors(representation, competitors_to_check):
    eliminated_competitors = set()
    for competitor in competitors_to_check:
        competitor_data = representation[competitor]
        neighbors_skills = []
        for neighbor in ['up', 'down', 'left', 'right']:
            if competitor_data[neighbor] is not None:
                neighbors_skills.append(representation[competitor_data[neighbor]]['skill'])
        if neighbors_skills:
            average_neighbors_skill = sum(neighbors_skills) / len(neighbors_skills)
            if competitor_data['skill'] < average_neighbors_skill:
                eliminated_competitors.add(competitor)
    return eliminated_competitors


def update_representation(representation, eliminated_competitors):
    competitors_to_check = set()
    for competitor in eliminated_competitors:
        competitor_data = representation[competitor]

        if competitor_data['up'] is not None:
            competitors_to_check.add(competitor_data['up'])
            representation[competitor_data['up']]['down'] = competitor_data['down']
        if competitor_data['down'] is not None:
            competitors_to_check.add(competitor_data['down'])
            representation[competitor_data['down']]['up'] = competitor_data['up']
        if competitor_data['left'] is not None:
            competitors_to_check.add(competitor_data['left'])
            representation[competitor_data['left']]['right'] = competitor_data['right']
        if competitor_data['right'] is not None:
            competitors_to_check.add(competitor_data['right'])
            representation[competitor_data['right']]['left'] = competitor_data['left']

        del representation[competitor]

    return competitors_to_check.difference(eliminated_competitors)


def _get_competitors_skills(representation, competitors=None):
    if competitors is None:
        return sum(competitor['skill'] for competitor in representation.values())
    else:
        return sum(representation[competitor]['skill'] for competitor in competitors)


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        r, c = [int(x) for x in input().split(' ')]
        dance_floor = [[int(x) for x in input().split(' ')] for _ in range(r)]
        print(f"Case #{i}: {get_competition_interest(dance_floor)}")