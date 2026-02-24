#prime number checker
# Part 1 : Check Single Number 

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a Prime number")

elif num == 2:
    print("2 is a PRIME number")

else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a Prime number")


# Part 2 : Prime Numbers in Range 

start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for n in range(start, end + 1):

    if n <= 1:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")