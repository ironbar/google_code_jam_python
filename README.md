# Google Code Jams

This repository contains:

- My solutions with python code to the problems from the [Google Code Jams](https://codingcompetitions.withgoogle.com/codejam)
- Resources to learn and prepare the challenges
- A scrapper to download information from the languages used by the participants in the challenges

The goal is to improve my algorithmic skills and to see if python can be a competitive language.
The statistics so far so that the best competitors use mainly C++.

The strategy will be to always write a working solution for every problem I try to solve. I might
look into the analysis section if needed but I should always write a working solution. If I only
read the analysis but not write a solution I will not learn anything.

## Strategy

- I should read each problem slowly two times taking notes. Pay attention to the examples to avoid
  misunderstandings.
- It may have sense to read all the problems at the start of the challenge and start by the problem
  that seems easier.

## Environment

```bash
conda create -n google_code_jam python=3.7 numpy scipy matplotlib pypy -c conda-forge
pip install snakeviz
```

In the [FAQ](https://codingcompetitions.withgoogle.com/codejam/faq) I get the following documentation about the environments:

```
Python 3:
3.7.3 (package: python3.7)
 numpy 1.19.3 (pip install numpy)
 scipy 1.5.3 (pip install scipy)
 python3 Solution.py
PyPy 3:
7.0.0, Python 3.5.3 (package: pypy3)
 numpy and scipy are unavailable
 pypy3 Solution.py
```

## Testing the solutions

```bash
# run the script with input data
cat input.txt | python code.py
# run the script with input data and compare the output with the expected output
cat input.txt | python code.py > pred.txt ; echo "Script output is: "; cat pred.txt; echo "Comparison with required output"; diff output.txt pred.txt; rm pred.txt
```

## Python dependencies

The known python dependencies are: `numpy, scipy`

## Resources

- [Google Code Jam — How To Prepare by Konopka Kodes](https://konopkakodes.medium.com/google-code-jam-study-guide-a8c58baf6397)
- [▶️ Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1638s)
- [Online judge](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3) is a web platform with
  a lot of problems to solve. It is a good place to practice and to learn new algorithms.

### Dynamic programming

[Dynamic programming by favtutor](https://favtutor.com/blogs/dynamic-programming)

Toy problems:

- Fibonacci
- Grid traveler
- Can sum, how sum and best sum

Sample problems:

- [Spiralling into control](https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15a74)

## 2023 New year Resolutions

The following table summarizes what was needed on 2022 to pass the rounds.

| Round         | Participants | Requirements to pass round |
|---------------|--------------|----------------------------|
| Qualification | ∞            | 30                         |
| 1             | ∞            | 34/100 @ 1:51              |
| 2             | 4500         | 25/100 @ 1:19              |
| 3             | 1001         | 71/100 @ 1:28              |
| Finals        | 26           |                            |

- 2023 resolution: get to round 3. This might be achieved by solving 2 problems each round
- 2024 resolution: get to final round. To achieve this I should be able to solve 3 problems in 2.5 hours.
  Thus I need to be fast, experienced and to have good templates.

To be able to achieve this goals I should do one challenge per week.
