import sys

def main():
    for line in sys.stdin:
        i, j = map(int, line.split())    # For each input line
        max_cycle_length = 1
        print(f"{i} {j} {max_cycle_length}")


if __name__ == "__main__":
    main()