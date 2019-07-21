'''
    File name: five.py
    Author: Ishan Chhabra
    Date created: 7/20/2019
    Python Version: 3.7
'''

# taking input...
str = input()

# delimiter is comma...
list = str.split(",")

# sorting...
list.sort()

# printing it out to the user...
print(','.join(list))
