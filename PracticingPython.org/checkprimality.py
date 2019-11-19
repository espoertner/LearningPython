#Ask the user for a number and determine whether the number is prime or not. 
#A prime number is a number that has no divisors.
userNumber = input("Type a number to see if it's prime. ")
userNumInt = int(userNumber)
if userNumInt > 1:
    for i in range(2, userNumInt//2):
        if (userNumInt % i) == 0:
            print(userNumber + " is not a prime number.")
            break
    else:
        print(userNumber + " is a prime number.")
else:
    print(userNumber + " is not a prime number")