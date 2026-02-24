#factorial calculator
#input from user
n = int(input("Enter a number: "))

# checking negative number
if n < 0:
    print("Factorial is not defined for negative numbers")

# factorial of 0 is 1 so
elif n == 0:
    print("0! = 1")

else:
    fact = 1
    print(str(n) + "! =", end=" ")

# loop from n to 1
    for i in range(n, 0, -1):
        fact = fact * i
        print(i, end="")
        
        if i != 1:
            print(" x ", end="")

    print(" =", fact)