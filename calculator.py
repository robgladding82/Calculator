""" A very basic calculator function that allows users to perform addition, subtraction, multiplication, and
division, running in a loop until the user chooses to exit. The user is prompted to select an operation and enter
2 numeric value as operands. Invalid numerical inputs are handle and division by zero is prevented. At the end of
each calculation the user is asked if they would like to perform another calculation and the program either loops
or exits depending on their selection. If the user enters an invalid input at the continuation prompt they will be
repeatedly asked until a valid input is entered.
"""

# Function for addition.
def add(x, y):
    return x + y

# Function for subtraction.
def sub(x, y):
    return x - y

# Function for multiplication.
def mul(x, y):
    return x * y

# Function for division.
def div(x, y):
    """ Condition to check if y = zero to prevent division by zero.
    if zero is entered an error message displays and user is asked
    if they would like to start again. """
    if y == 0:
        return "Cannot divide by zero."
    return x / y

# Main calculator function to control flow of the program.
def cal():
    # While loop to allow the calculator to restart if the user wishes.
    while True:
        # Prompt user to select an operator.
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        # User enters choice 1,2,3 or 4.
        opp = input("Enter choice: ")

        # Validates the operation choice ensuring opp = 1, 2, 3, or 4.
        if opp == "1" or opp == "2" or opp == "3" or opp == "4":
        # Try block to handle potential errors. Prompts user to enter operands.
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
        # If input can't be converted to float, catches error, returns error message and restarts function.
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

        # Conditional statements to perform the chosen operation with the entered operands.
            if opp == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif opp == "2":
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            elif opp == "3":
                print(f"{num1} * {num2} = {mul(num1, num2)}")
            elif opp == "4":
                print(f"{num1} / {num2} = {div(num1, num2)}")
        # Returns error message if the users operation choice is invalid and restarts function.
        else:
            print("Input not valid. Please enter 1, 2, 3 or 4.")
            continue

        # Loop to ask user if they wish to carry out another calculation.
        while True:
            repeat = input("Do you wish to carry out another calculation? (y/n)").lower()

        # If they select "n" the program is exited.
            if repeat == "n":
                print("Exiting program")
                return
        # If they select "y" we break out of this loop and go back to the beginning of cal().
            elif repeat == "y":
                break

        # If they enter anything else an error message display and the question repeats.
            else:
                print("Invalid choice. Enter y or n")

# Calls the cal function to start the program.
cal()
