'''
    File name: two.py
    Author: Ishan Chhabra
    Date created: 7/20/2019
    Python Version: 3.7
'''

# taking inputs...
n = int(input())
i = 1

# initializing dictionary...
dict = {}

# looping through till n...
while(i <= n):
    dict.update({i: (i*i)})
    i = i + 1

# printing...
print(dict)
