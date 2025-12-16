"""
🕒 Project Title:

Countdown Timer (Basic Clock)

Project Description:

The Countdown Timer (Basic Clock) is a simple Python mini-project that allows the user
to enter a number of seconds, and the program counts down until it reaches zero. This
project helps beginners understand how to use loops, conditional statements, and time delays.


This project can be the foundation for more advanced applications such as:
A digital clock, a Pomodoro timer, workout timer, or part of a game.

Sample Input & Output
Input:
______Countdown Timer______

Enter the number of seconds to countdown: 3

Output:

Time left: 3 seconds
Time left: 2 seconds
Time left: 1 seconds

Time's up!
3 seconds countdown completed successfully!

Countdown finished.Do you want to continue(y/n): y
Enter the number of seconds to countdown: 3.5
Invalid input. Please enter a whole number
Enter the number of seconds to countdown: 5
Time left: 5 seconds
Time left: 4 seconds
Time left: 3 seconds
Time left: 2 seconds
Time left: 1 seconds

Time's up!
5 seconds countdown completed successfully!

Countdown finished.Do you want to continue(y/n): n
Exiting...

Process finished with exit code 0

"""
import time

def start_countdown(seconds):
    for count in range(seconds,0,-1):
        print(f"Time left: {count} seconds ",end='\n')
        time.sleep(1)

    print(f"\nTime's up!\n{seconds} seconds countdown completed successfully!\n")
    return True

def get_user_input():
    print("______Countdown Timer______\n")
    should_continue = True
    while(should_continue):
        try:
            seconds = int(input("Enter the number of seconds to countdown: "))
            start_countdown(seconds)
            choice = input("Countdown finished.Do you want to continue(y/n): ").lower().strip()
            if choice !='y':
                should_continue = False
                print("Exiting...")
                return

        except ValueError:
             print("Invalid input. Please enter a whole number")

if __name__ =="__main__":
    get_user_input()
