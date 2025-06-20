import random

secret_number = random.randint(1, 10) 
guesses_left = 5
user_guess = 0 #initialize user guess

while guesses_left > 0: #loop until user is out of guesses
  user_guess = int(input("Guess a number between 1 and 10: ")) #reassign user_guess variable

  if user_guess == secret_number:
    print("Congratulations! You guessed the number!")
    break
  elif guesses_left == 1 and user_guess != secret_number: #let the user know what the number was if the get it wrong on the last guess
    print(f"Incorrect. Game Over! the secret number was {secret_number}")
  elif user_guess > secret_number:
    print("Too high! Try again.")
  else:
    print("Too low! try again.")
  
  guesses_left -= 1 #decrease number of guesses so the loop eventually ends
  
