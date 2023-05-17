#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    queue = []
    queue.append(s[0])
    
    for i in range(1, len(s)):
        if len(queue) != 0 and queue[-1] + s[i] in ['()', '{}', '[]']:
            queue.pop()
            
        else:
            queue.append(s[i])
     
    return 'YES' if len(queue) == 0 else 'NO'

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
