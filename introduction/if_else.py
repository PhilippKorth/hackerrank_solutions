#!/bin/python3

import math
import os
import random
import re
import sys


#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird

def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    n = int(input().strip())

    if is_even(n):
        if n in list(range(6, 21)):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
    
