# Python number guessing game
import random
lowest_num = 1
height_num = 100
answer = random.randint(lowest_num, height_num)
guesses = 0
is_running = True

print("Python number guessing game. ")
print(f"Select a number between {lowest_num} and {height_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > height_num:
            print("Number is out of range")
            print(f"Please select a number between {lowest_num} and {height_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest_num} and {height_num}")