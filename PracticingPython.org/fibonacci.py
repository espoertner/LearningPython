#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Take this opportunity to think about how you can use functions. 
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
sequenceNumber = int(input("How many numbers of the Fibonnaci sequence would you like to know? "))
def generateFibonnaci(x):
    counter = 0
    fibonnaciSequence = []
    while counter < x:
        if len(fibonnaciSequence) < 2:
            fibonnaciSequence.append(1)
            counter += 1
        else:
            newValue = (fibonnaciSequence[len(fibonnaciSequence)-1]) + (fibonnaciSequence[len(fibonnaciSequence)-2])
            fibonnaciSequence.append(newValue)
            counter += 1
    print(fibonnaciSequence)
generateFibonnaci(sequenceNumber)