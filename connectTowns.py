# Problem Statement
# https://www.hackerrank.com/challenges/connecting-towns/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
# How many paths are there from city  to the last city in the list, modulo 1234567
# n = 4
# routes = [3, 4, 5]
# 3 roads to city 1, 4 roads to city  2
# 2 testes de caso
# n = 3
# routes = [1, 3]
# 1*3 mod 1234567
# 2 * 2 * 2 mod 1234567
def connectingTowns(n, routes):
      # Write your code here 
      multi = [0] * (n - 1)
      paths = 1
      for i in range(n - 1):
            paths *= routes[i]

      return paths % 1234567
    
  


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        print(str(result) + '\n')

