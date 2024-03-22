#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    right = 0
    left = 0
    n = len(arr[0])
    # Write your code here
    for i in range(n):
        right += arr[i][i]
        left += arr[i][n-i-1]

    return print(abs(right - left))

diagonalDifference(
                    [
                        [1,2,3],
                        [1,2,3],
                        [1,2,3]
                    ]
                   )


