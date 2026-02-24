#calculator function
import math 

#function to add
def add(a, b):
    return a + b

#function to subtract
def subtract(a, b):
    return a - b

#function to multiply
def multiply(a, b):
    return a * b

#function to divide
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

#function for modulus
def modulus(a, b):
    return a % b

#function for power
def power(a, b):
    return a ** b

#Bonus Functions
def square_root(a):
    if a < 0:
        return "Cannot find square root of negative number"
    else:
        return math.sqrt(a)

def percentage(a, b):
    return (a * b) / 100

#calculator function
def calculator():
    while True:
        print(" Calculator ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        choice = int(input("Enter choice: "))

        if choice == 9:
            print("Calculator Closed")
            break
#square root needs only one number
        if choice == 7:
            a = float(input("Enter number: "))
            print("Result:", square_root(a))

#percentage needs two numbers
        elif choice == 8:
            a = float(input("Enter total value: "))
            b = float(input("Enter percentage: "))
            print("Result:", percentage(a, b))

        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(a, b))

            elif choice == 2:
                print("Result:", subtract(a, b))

            elif choice == 3:
                print("Result:", multiply(a, b))

            elif choice == 4:
                print("Result:", divide(a, b))

            elif choice == 5:
                print("Result:", modulus(a, b))

            elif choice == 6:
                print("Result:", power(a, b))

            else:
                print("Invalid choice")

calculator()