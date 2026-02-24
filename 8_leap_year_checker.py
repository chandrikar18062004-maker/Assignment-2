#leap year cheaker
#input from user
year = int(input("Enter a year: "))

#check if year is divisible by 4
if year % 4 == 0:
    
# Then check if year is divisible by 100
    if year % 100 == 0:
        
# if divisible by 100 then check 400
        if year % 400 == 0:
            print(year, "is a Leap Year")
            print("Because it is divisible by 400")
        else:
            print(year, "is Not a Leap Year")
            print("Because it is divisible by 100 but not 400")
    
    else:
        print(year, "is a Leap Year")
        print("Because it is divisible by 4 but not 100")

else:
    print(year, "is Not a Leap Year")
    print("Because it is not divisible by 4")