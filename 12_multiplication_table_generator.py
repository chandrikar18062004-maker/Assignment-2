#multiplication table generator
#taking number and range from user
num = int(input("Enter number: "))
end = int(input("Enter range (end): "))
print("\nMultiplication Table of", num)
#loop from 1 to end
for i in range(1, end + 1):
    result = num * i
    print(num, "x", i, "=", result)
