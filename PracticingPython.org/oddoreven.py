#testing if a number the user inputs is odd or even
num = int(input("Type a number to find out if it's odd or even. e.g. 3457. \n"))
# % is a remainder operator in python {} .format help avoid needing to make num a string
if (num % 2) == 0:
    print("{0} is an even number.".format(num))
else:
    print("{0} is an odd number.".format(num))
#testing if a number the user inputs is a multiple of four
numFour = int(input("Type a number to find out if it's a multiple of 4. e.g. 9862. \n"))
if (numFour % 4) == 0:
    print("{0} is a multiple of four.".format(numFour))
else:
    print("{0} is not a multiple of four.".format(numFour))
#testing if two numbers the user imputs are multiples of each other
firstNum = int(input("See if one number divides into another. Type the number to check. e.g. 873. \n"))
checkNum = int(input("Now type the number you want to divide by. e.g. 9. \n"))
if (firstNum % checkNum) == 0:
    print("{0} is evenly divisible by {1}.".format(firstNum,checkNum))
else:
    print("{0} is not evenly divisible by {1}.".format(firstNum,checkNum))