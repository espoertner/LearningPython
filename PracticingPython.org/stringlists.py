#Ask the user for a string and print out whether this string is a palindrome or not
#A palindrome is a string that reads the same forwards and backwards
string = input("Type a word to see if it is a palindrome.\n")
string = string.lower()
length = (len(string))
reverse = string[length::-1]
print(string + " in reverse is " + reverse)
if string == reverse:
    print(string + " is a palindrome.")
else:
    print(string + " is not a plaindrome.")