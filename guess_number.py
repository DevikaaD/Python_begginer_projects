import random

top_of_range = input("Enter the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please enter a number greater than zero next time")
        quit()
else:
    print("Please enter a number")
    quit()

random_number = random.randrange(0,top_of_range)

guesses = 0

while True:
    guesses +=1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter a number")
        continue
    if user_guess == random_number:
        print("You guessed right!")
        break

    elif user_guess>random_number:
        print("You guessed above the number, guess a smaller number next time!")
    else:
        print("You guesses a lower number, guess a larger number next time!")

print("You got it in", guesses, "guesses")