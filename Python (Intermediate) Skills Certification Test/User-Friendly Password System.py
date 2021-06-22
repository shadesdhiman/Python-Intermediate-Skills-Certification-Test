#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def authEvents(events):
    res = []
    # Write your code here
    for i in range(len(events)):
        event_type = events[i][0]
        if event_type == "setPassword":
            key = events[i][1]
            p=131
            m = (10**9)+7
            n = 0
            hash_value = 0
            for i in range(len(key)-1,-1,-1):
                hash_value += ord(key[i])*(p**n)
                n=n+1
            hash_value = hash_value % m
            #print(hash_value)
            
            
            
            hash_value_left_limit =0
            n = 1
            for i in range(len(key)-1,-1,-1):
                hash_value_left_limit += ord(key[i])*(p**n)
                n=n+1
            hash_value_left_limit = hash_value_left_limit % m
            #print(hash_value_left_limit)
            
            n = 1
            hash_value_right_limit = 127
            for i in range(len(key)-1,-1,-1):
                hash_value_right_limit += ord(key[i])*(p**n)
                n=n+1
            hash_value_right_limit = hash_value_right_limit % m
            #print(hash_value_right_limit)

            
        elif event_type == "authorize":
            entered_hash = int(events[i][1])
            if entered_hash == hash_value:
                res.append(1)
            elif entered_hash >= hash_value_left_limit  and entered_hash <= hash_value_right_limit:
                res.append(1)
            else:
                res.append(0)
    return res
                
                
            
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
