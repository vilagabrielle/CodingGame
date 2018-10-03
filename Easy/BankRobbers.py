import sys
import math
import numpy as np


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
v = int(input())
timevault= []

for i in range(v):
    c, n = [int(j) for j in input().split()]
    timevault.append(10**n * 5**(c-n))


time_rob= timevault[0:r]
for i in range(v-r):
    time_rob[time_rob.index(min(time_rob))]= min(time_rob) + timevault[i+r]

timefinal = max(time_rob)


print(timefinal)
