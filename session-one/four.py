'''
    File name: four.py
    Author: Ishan Chhabra
    Date created: 7/20/2019
    Python Version: 3.7
'''

import math
# taking input...
str = input()

# delimiter is comma.
list = str.split(",")

# constants...
C = 50
H = 30

# looping through list...
for D in list:
    Q = round(math.sqrt(((2*C*int(D))/H)))
    print(Q)
