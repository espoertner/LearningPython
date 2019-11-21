#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order.
def stringBackwards():
    string = input("Type a long phrase or sentence you want to read in reverse. ")
    splitString = string.split()
    reverseStringList = []
    for value in reversed(splitString):
        reverseStringList.append(value)
    reverseString = " ".join(reverseStringList)
    return reverseString
print(stringBackwards())