#temperature converter
#list of options 
while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
#user input to choose
    ch = int(input("Enter your choice: "))
    if ch == 1:
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print("Result:", f)

    elif ch == 2:
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print("Result:", c)

    elif ch == 3:
        c = float(input("Enter Celsius: "))
        k = c + 273.15
        print("Result:", k)

    elif ch == 4:
        k = float(input("Enter Kelvin: "))
        c = k - 273.15
        print("Result:", c)

    elif ch == 5:
        f = float(input("Enter Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print("Result:", k)

    elif ch == 6:
        k = float(input("Enter Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print("Result:", f)

    elif ch == 7:
        print("End")
        break

    else:
        print("Invalid choice")