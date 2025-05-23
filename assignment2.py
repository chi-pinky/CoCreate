# Lab 2 work
# Let’s build a guess game. 
# In this game we would have a secret number and then ask the user to Guess the secret number. 
# If the user guesses it right before the 5th guess, the user wins and if he doesn’t the user loses the guess. 
# The user can play this game as many times as he wants.


secret_number = 90
number_of_guesses = 5
guesses = 0

while guesses < number_of_guesses:
    guess = int(input("Guess the secret number: ")) 
    if guess == secret_number:
        print("You win!")
        break
    else:
        guesses += 1
        print("Try again.")
if guesses == number_of_guesses:
    print("You lose. The secret number was", secret_number)
