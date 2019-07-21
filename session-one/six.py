'''
    File name: six.py
    Author: Ishan Chhabra
    Date created: 7/20/2019
    Python Version: 3.7
'''
import math
from functools import reduce

# function to calculate average...


def average(list):
    return reduce(lambda x, y: x + y, list) / len(list)


# initialising variables...
n = 5
list = []

# taking multiple line inputs...
for i in range(0, n):
    list.append(int(input()))

# printing it out to the user...
print(average(list))
