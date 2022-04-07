from random import randint

initialScore = 100
randomNum = randint(1, 100)


def checkUserGuess(userGuess):
    global initialScore
    if (randomNum == userGuess):
        return True
    else:
        if(randomNum < userGuess):
            initialScore = initialScore - 10
            print("Your guess is larger than the actual number.")
        else:
            initialScore = initialScore - 10
            print("Your guess is smaller than the actual number.")
        return False


def game():
    userGuess = input("Enter your Guess: ")
    if not(userGuess.isdigit()):
        print("\n", "No number provided", "\n")
        return
    nthUserGuess = int(userGuess)
    if(checkUserGuess(nthUserGuess) != True):
        if (initialScore > 0):
            game()
        else:
            print("\n", "Too many tries, Game over!!!", "\n")
    else:
        valueToPrint = "Your score was: " + str(initialScore) + "/100"
        print("\n", valueToPrint, "\n")
        print("You got it!")


game()
