#Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#Write two different functions to do this - one using a loop and constructing a list, and another using sets
a = [1, 1, 2, 9, 4, 12, 9, 7, 10, 10, 3, 6]
def newListSet(x):
    newListSet = list(set(x))
    return newListSet
def newList(x):
    newList  = []
    for value in x:
        if value not in newList:
            newList.append(value)
    return newList
print(newListSet(a))
print(newList(a))