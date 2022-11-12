import random

low=1
high=100
guesses=0
number = random.randint(low, high)

while True:
    
    guess = int(input("Guess a number between " + str(low) + " and " + str(high) + " : "))
    guesses = guesses + 1
    if guess > number:
        print("You guessed too high...")
    elif guess < number:
        print("You guessed too low...")
    else:
        print("Hurray! You guessed the correct number...")
        break
print(f"The number of tries it took you is {guesses}")