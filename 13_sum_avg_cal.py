#sum average calculator
#ask how many numbers user wants to enter
count = int(input("How many numbers:"))
total = 0 
maximum = 0
minimum = 0
# loop to take numbers
for i in range(1, count + 1):
    num = int(input("Enter number " + str(i) + ": "))
    
    total = total + num   # adding to total
    if i == 1:
        maximum = num
        minimum = num
    else:
#checking for maximum
        if num > maximum:
            maximum = num
        
#check for minimum
        if num < minimum:
            minimum = num

#calculate average
average = total / count
#results
print("\nSum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
