#Take two lists and write a program that returns a list that contains only the elements that are common between the lists
#Without duplicated
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
abOverlap = [value for value in a if value in b]
abCommon = []
for value in abOverlap:
    if value not in abCommon:
        abCommon.append(value)
print(abCommon)
#Generate two random lists of numbers between 1-50 of different lengths, return only the common values
#Without duplicated
import random
d = random.sample(range(1,50), 20)
e = random.sample(range(1,50), 40)
deOverlap = [value for value in d if value in e]
deCommon = []
for value in deOverlap:
    if value not in deCommon:
        deCommon.append(value)
deCommon.sort()
print(deCommon)