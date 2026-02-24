#number system function
#1. factorial
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#2. check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#3. fibonacci (nth number)
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a = 0
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b
#4. sum of digits
def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total
#5. reverse number
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
#6. Armstrong number
def is_armstrong(n):
    power = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp = temp // 10
    return total == n
#7. gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# 8. lcm
def lcm(a, b):
    return (a * b) // gcd(a, b)
# 9. perfect number
def is_perfect_number(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
# 10. menu
def math_menu():
    while True:
        print("\n--- Number System Menu ---")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = int(input("Enter choice: "))

        if choice == 10:
            break

        elif choice == 1:
            n = int(input("Enter number: "))
            print("Result:", factorial(n))

        elif choice == 2:
            n = int(input("Enter number: "))
            print("Result:", is_prime(n))

        elif choice == 3:
            n = int(input("Enter position: "))
            print("Result:", fibonacci(n))

        elif choice == 4:
            n = int(input("Enter number: "))
            print("Result:", sum_of_digits(n))

        elif choice == 5:
            n = int(input("Enter number: "))
            print("Result:", reverse_number(n))

        elif choice == 6:
            n = int(input("Enter number: "))
            print("Result:", is_armstrong(n))

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", gcd(a, b))

        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", lcm(a, b))

        elif choice == 9:
            n = int(input("Enter number: "))
            print("Result:", is_perfect_number(n))

        else:
            print("Invalid choice")

math_menu()