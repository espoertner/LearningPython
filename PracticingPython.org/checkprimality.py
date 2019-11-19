#Ask the user for a number and determine whether the number is prime or not. 
#A prime number is a number that has no divisors.
#Known issue:
#Throws ValueError when non-numbers are typed
userNumber = input("Type a number to see if it's prime. ")
userNumInt = int(userNumber)
def checkPrimality(n):
    if userNumInt > 1:
        for i in range(2, userNumInt//2):
            if (userNumInt % i) == 0:
                return False
        else:
            return True
    else:
        return False
if (checkPrimality(userNumInt)) == True:
    print(userNumber + " is a prime number.")
else:
    print(userNumber + " is not a prime number.")