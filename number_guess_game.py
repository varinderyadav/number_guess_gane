import random

random_number = random.randint(1, 100)

attempts = 0
guess = 0


while guess != random_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f" Congratulations bro ! You guessed it in {attempts} attempts.")
