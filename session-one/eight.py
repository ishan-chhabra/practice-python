'''
    File name: eight.py
    Author: Ishan Chhabra
    Date created: 7/20/2019
    Python Version: 3.7
'''

# initialising variables
net_amount = 0

while True:
    str = input("Enter transaction: ")

    # delimiter is space...
    transaction = str.split(" ")

    # first element is the type while second argument is the amount...
    type = transaction[0]
    amount = int(transaction[1])

    if type == "D" or type == "d":
        net_amount += amount
    elif type == "W" or type == "w":
        net_amount -= amount
    else:
        pass

    str = input("Do you want to continue (Y for yes) : ")
    if not (str[0] == "Y" or str[0] == "y"):
        # break the loop if not Y or y...
        break

# printing it out the user...
print(net_amount)
