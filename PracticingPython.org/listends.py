#Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
#For practice, write this code inside a function.
a = [5, 10, 15, 20, 25]
def firstLastItem(OriginalList):
    length = len(OriginalList)
    newList = [OriginalList[0], OriginalList[length-1]]
    print (newList)
firstLastItem(a)