from statistics import mean, median,variance,stdev
import math
import sys

def char_type(ch):
    if ch.islower():
        return "lower"
    if ch.isupper():
        return "upper"
    if ch.isdigit():
        return "digit"
    return ch


def randomness(string):
    counts = {}
    types = []
    for i in range(len(string)):
        ch = string[i]
        types.append(char_type(ch))
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    types = list(set(types))
    if len(types) < 3:
        return 1
    count_stat = []
    for ch in counts:
        count_stat.append(counts[ch])
    return variance(count_stat) / len(string)


if __name__ == "__main__":
    threshold = 0.1
    if len(sys.argv) == 3:
        threshold = float(sys.argv[2])
    if randomness(sys.argv[1]) < threshold:
        print(sys.argv[1])


