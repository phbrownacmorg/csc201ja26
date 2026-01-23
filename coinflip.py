from random import random

def flipheads() -> bool:
    heads = random() < 0.5
    return heads

def main(args: list[str]) -> int:
    numflips = 10
    flip_sequence: list[bool] = []
    for i in range(numflips): # type: ignore
        flip_sequence.append(flipheads())
    print(flip_sequence)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
