#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour, minute, second_period = s.split(':')
    second, period = second_period[:2], second_period[2:]
    hour = int(hour)
    if period == 'AM':
        if hour == 12:
            hour = 0
    elif period == 'PM':
        if hour != 12:
            hour += 12
    hour_str = str(hour).zfill(2)
    minute_str = minute.zfill(2)
    second_str = second.zfill(2)
    military_time = f"{hour_str}:{minute_str}:{second_str}"
    
    return military_time 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
