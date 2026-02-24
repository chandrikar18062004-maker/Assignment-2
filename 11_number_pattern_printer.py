#number pattern printer
#pattern choice and height from user
choice = int(input("Enter pattern number 1-4: "))
n = int(input("Enter height: "))
#pattern 1
if choice == 1:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

#pattern 2
elif choice == 2:
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")
        print()

#pattern 3
elif choice == 3:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()

#pattern 4
elif choice == 4:
    for i in range(1, n + 1):
        #increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        #decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

else:
    print("Invalid choice")