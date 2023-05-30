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
    format24 = ''
    hour = s[:2]
    
    if s[-2:] == 'AM':
        if hour == '12':
            hour = '00'
            format24 = hour + s[2:-2]
        else:
            format24 = s[0: -2]
    elif s[-2:] == 'PM':
        if hour != '12':
            hour = int(s[:2]) + 12    
        format24 = str(hour) + s[2:-2]
    
    return format24

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
