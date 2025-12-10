"""
Goal:

The program will generate a complete multiplication table for a number specified by the user,
 up to a specified range (e.g., up to 10). This exercise uses a for loop to repeatedly perform
 and print the multiplication operation.

 Sample input and  Output
Enter the number for the multiplication table:	7
Enter the limit :	5

Multiplication Table for 7 up to 5:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35

"""
def display_multiplication_table(value,limit):
    for row_limit in range (1,limit+1):
        print(f"{value} * {row_limit} =  {value*row_limit}")


def program_start():
    """Main loop to control the execution and continuation"""
    print("Welcome to Multiplication Table Generator!")
    should_continue = True
    while(should_continue):

        value = int(input("Enter the number for multiplication table: "))
        limit = int(input("Enter the limit: "))

        if limit<=0:
            print("Limit must be a positive number. Please try again.")
            continue #skip to the next iteration of the loop

        display_multiplication_table(value, limit)

        #Get the continuation choice
        choice = input("Do you want to continue(y/n): ").lower().strip()

        #Check the choice and update the flag
        if choice !='y':
            should_continue = False
    print("Exiting the program...")

if __name__ == "__main__":
    program_start()
