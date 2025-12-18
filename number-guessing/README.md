# Number Guessing with a timer

> This project combines a simple pre-game countdown with an interactive number guessing game.
The application first executes a brief countdown timer to build anticipation. Once the timer
completes, the main game begins. In the game, a secret random number is generated within a
defined range. The user's goal is to guess this hidden number. The program provides feedback to
the user after each guess, indicating whether the guess was correct, high, or  low, continuing
until the number is correctly identified.This project demonstrates advanced Exception Handling,
Input Validation, and Nested Loop structures.

- Countdown Timer: Adds urgency to the game using a countdown function.
- Recursive Game Loop: Allows players to play multiple rounds without restarting the script.
- Intelligent Input Validation: Handles decimals,and textgracefully without crashing.
- Robust Error Handling: Uses try...except blocks to catch ValueError and TypeError to ensure the program stays running even with "undesired" input.
  
---
## How to Run
1. Clone the repository:
   git clone https://github.com/divzmadhu/basic-python-projects.git
2. Navigate to the folder:
   cd basic-python-projects/number-guessing
3. Run the program:
   python number_guessing.py
---
## Sample Input/Output
**Input:**
```
Pre-Game Countdown!
Get Ready!
Time left: 3
Time left: 2
Time left: 1
Go!
Game Start!
I'm thinking of a number between 1 and 10. Can you guess it?

```

**Output:**
```
Guess 1: 2
Your guess of 2 is low.
Guess 2: 4
Your guess of 4 is low.
Guess 3: 5
Your guess of 5 is low.
Sorry 3 attempts over! You Loose.
Do you want to continue(y/n)? y
Get Ready!
Time left: 3
Time left: 2
Time left: 1
Go!
Game Start!
I'm thinking of a number between 1 and 10. Can you guess it?
Guess 1: 7
Your guess of 7 is high.
Guess 2: 5
Your guess of 5 is high.
Guess 3: 2
Your guess of 2 is low.
Sorry 3 attempts over! You Loose.
Do you want to continue(y/n)? y
Get Ready!
Time left: 3
Time left: 2
Time left: 1
Go!
Game Start!
I'm thinking of a number between 1 and 10. Can you guess it?
Guess 1: 7
Your guess of 7 is high.
Guess 2: 5
Your guess of 5 is low.
Guess 3: 6
Congratulations! You guessed the number 6 in 3 attempts.
Do you want to continue(y/n)? n
Exiting....

Process finished with exit code 0

```
---
## Future Improvements
- Highscore Tracking
- Add difficulty levels
- Real-time countdown using threading 
- GUI version

 ## Author
 
 DJ
 
 Beginner Python Developer
 
 Github: https://github.com/divzmadhu/basic-python-projects
