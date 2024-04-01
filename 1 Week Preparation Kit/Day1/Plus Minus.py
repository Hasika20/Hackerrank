#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    #Write your code here
    n=len(arr)
    countp=0
    countn=0
    countz=0
    for i in arr:
        if i<0:
            countn+=1
        elif i>0:
            countp+=1
        else:
            countz+=1
    resp = "{:.6f}".format(countp / n)
    resn = "{:.6f}".format(countn / n)
    resz = "{:.6f}".format(countz / n)
    print(resp)
    print(resn)
    print(resz)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
