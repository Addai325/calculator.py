# Week Four(4) Python Assignment
# Name: Ransford Addai
# Training ID: 32524

# Importing the calculator module which contains the arithmetic functions
import calculator

# Function to perform addition operation
def addition(a, b):
    return a + b

# Function to perform subtraction operation
def subtraction(a, b):
    return a - b

# Function to perform multiplication operation
def multiplication(a, b):
    return a * b

# Function to perform division operation
def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


# Main function to execute the calculator program
def main():
    print("Hello!!👋 You are welcome to our Basic Calculator!")
    print()

    while True:
        try:
            num_one = float(input("Please enter your first value: "))
            num_two = float(input("Please enter your second value: "))
        except ValueError:
            print("Please enter valid numeric values!😊")
            print()
            continue

        print("These are the available operations")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print()

        try:
            your_choice = input("Please choose the operation to perform: ")
        except ValueError:
            print("Please enter a valid choice!")
            continue

        if your_choice == "1":
            operator = "+"
            result = calculator.addition(num_one, num_two)
        elif your_choice == "2":
            operator = "-"
            result = calculator.subtraction(num_one, num_two)
        elif your_choice == "3":
            operator = "*"
            result = calculator.multiplication(num_one, num_two)
        elif your_choice == "4":
            operator = "/"
            try:
                result = calculator.division(num_one, num_two)
            except ZeroDivisionError as e:
                print(e)
                continue
        else:
            print("Invalid input. Please enter a valid number.😊")
            continue

        print(f"Result: {num_one} {operator} {num_two} = {result}")

        again = input("Do you wish to calculate again (yes/no): ").lower()

        if again == "yes":
            print()
            continue
        elif again == "no":
            print("Thanks for using our calculator. See you next time. Bye!😇")
            break
        else:
            print("Invalid input, please choose between (yes/no)")
            print()

if __name__ == '__main__':
    main()
