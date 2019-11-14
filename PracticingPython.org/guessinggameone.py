#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#Extra: Keep the game going until the user types “exit”
#Extra: Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
userGuess = input("I'm thinking of a number between 1 and 9. What is it? To end the game type exit\n")
if userGuess != "exit":
    userInt = int(userGuess)
else:
    print("You can't win if you don't play!")
counter = 0
counterCorrect = 0

while userGuess != "exit":
    computerGuess = random.randint(1,9)
    computerString = str(computerGuess)
    counter += 1
    if userInt > computerGuess:
        print("Your guess was too high.")
    elif userInt < computerGuess:
        print("Your guess was too low.")
    else:
        counterCorrect += 1
        print("Your guess was correct!")
    print("You guessed " + userGuess + " and I picked " + computerString)
    userGuess = input("I'm thinking of a number between 1 and 9. What is it? To end the game type exit\n")
    if userGuess != "exit":
        userInt = int(userGuess)
    else:
        counterStr = str(counter)
        counterCorrectStr = str(counterCorrect)
        print("The game has ended. You played " + counterStr + " time(s) with " + counterCorrectStr + " correct guess(es).")