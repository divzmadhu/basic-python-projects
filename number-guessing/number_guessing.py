"""
🎯 Project Description

This project combines a simple pre-game countdown with an interactive number guessing game.
The application first executes a brief countdown timer to build anticipation. Once the timer
completes, the main game begins. In the game, a secret random number is generated within a
defined range. The user's goal is to guess this hidden number. The program provides feedback to
the user after each guess, indicating whether the guess was correct, high, or  low,
 continuing until the number is correctly identified.

Stage	Sample Input (User)	Sample Output (Program)
Pre-Game Countdown

Get Ready!

Time left: 3

Time left: 2

Time left: 1

GO!
Game Start	I'm thinking of a number between 1 and 10. Can you guess it?
Guess 1 	3	Your guess of 3 is low.
Guess 2 	8	Your guess of 8 is high.
Guess 3 	5	Congratulations! You guessed the number 5 in 3 attempts.
"""
import time
import random
seconds = 3

def countdown(seconds):
    print("Get Ready!")
    for count in range(seconds,0,-1):
        print(f"Time left: {count}")
        time.sleep(1)
    print("Go!")

def number_guess(random_number):
    flag = 0
    hit = 1
    while(True):
        if hit <= 3:
            user_input = input(f"Guess {hit}: ")
            try:
                guess = int(user_input)
                    #int(input(f"Guess {hit}: ")))
                if guess < 1 or guess > 10:
                    raise ValueError("Out of Range")
                elif guess == random_number:
                    flag = 1
                    print(f"Congratulations! You guessed the number {guess} in {hit} attempts.")
                    break
                elif guess < random_number:
                    print(f"Your guess of {guess} is low.")
                elif guess > random_number:
                    print(f"Your guess of {guess} is high.")
                hit = hit + 1

            except ValueError as e:
                if str(e) == "Out of Range":
                    print("Wrong Input! Enter a number between 1 and 10")
                elif "." in user_input:
                    print("Wrong Input: You entered a decimal. Please enter a whole number")
                else:
                    print("Wrong Input: That wasn't even a number!")
        elif hit>3:
            print(f"Sorry {hit-1} attempts over! You Loose.")
            break

def program_start():

    print("Pre-Game Countdown!")
    should_continue = True
    while(should_continue):
        try:
            countdown(seconds)
            print("Game Start!")
            print("I'm thinking of a number between 1 and 10. Can you guess it?")
            random_number =  random.randint(1,10)
            number_guess(random_number)
            while(True):
                choice = input("Do you want to continue(y/n)? ").lower().strip()
                if choice == 'y':
                    break
                    #return True
                if choice == 'n':
                    should_continue =False
                    print("Exiting....")
                    return
                else:
                    print("Invalid input. Either enter 'y' or 'n'.... ")
                    #raise ValueError("Invalid choice")

        except (ValueError,TypeError) as e:
            print(f"Error caught1:{e}!")
            should_continue = False


if __name__ == "__main__":
    program_start()
