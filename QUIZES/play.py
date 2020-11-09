#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_bob = 0
    score_ana = 0
    check = 0
    while check <= len(a):
        if a[check] > b[check]:
            score_bob += +1
            check += +1
        if a[check] < b[check]:
            score_ana += +1
            check += +1
        else:
            check += +1
    return score_bob, score_ana


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
