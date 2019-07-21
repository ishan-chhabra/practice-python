'''
    File name: three.py
    Author: Ishan Chhabra
    Date created: 7/20/2019
    Python Version: 3.7
'''

# Initializing list...
list = []

# Creating range from 2000 to 3200 with a step of 1...
x = range(2000, 3200, 1)

# Looping through...
for n in x:
    # Conditional logics...
    if n % 7 == 0 and n % 5 != 0:
        list.append(n)

# Printing it out to the user...
print(list)
