# Google Code Jams

This repository contains:

- My solutions with python code to the problems from the [Google Code Jams](https://codingcompetitions.withgoogle.com/codejam)
- Resources to learn and prepare the challenges
- A scrapper to download information from the languages used by the participants in the challenges

The goal is to improve my algorithmic skills and to see if python can be a competitive language.
The statistics so far so that the best competitors use mainly C++.

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

[Google Code Jam — How To Prepare by Konopka Kodes](https://konopkakodes.medium.com/google-code-jam-study-guide-a8c58baf6397)

### Dynamic programming

[Dynamic programming by favtutor](https://favtutor.com/blogs/dynamic-programming)

Sample problems:

- [Spiralling into control](https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15a74)
