import random

print("This is a guessing game.")

computerGuess = random.randint(1, 50)
print("The computer guessed" , computerGuess)

humanGuess = input("Guess a number and write it here :")
print("You guessed ", humanGuess, "..mmm, lets see")


