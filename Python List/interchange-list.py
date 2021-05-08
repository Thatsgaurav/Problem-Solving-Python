# Python program to interchange first and last elements in a list

# Given a list, write a Python program to swap first and last element of the list.

# Examples:

# Input: [12, 35, 9, 56, 24]
# Output: [24, 35, 9, 56, 12]

# Input: [1, 2, 3]
# Output: [3, 2, 1]
# 1: Find the length of the list and simply swap the first element with (n-1)th element. Approach


def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


newList = [12, 35, 9, 56, 24]
print(swapList(newList))
