"""
Given an array of integers, find the sum of its elements.

The first line contains an integer, n, denoting the size of the array.
The second line contains n space-separated integers representing the array's elements.

"""

import os
import math
import re
import sys
import math

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()