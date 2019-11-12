# write a program that prints out all the elements of the list that are less than 5
# print(i, end=" ") would print all elements on one line
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
# same idea but creating a new list for items more than 5
a2 = [i for i in a if i > 5]
print(a2)
# same idea but with user input
value = int(input("\nType a value to see the number in the list less than that value. e.g. 5 \n"))
for i in a:
    if i < value:
        print(i)