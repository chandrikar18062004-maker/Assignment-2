#ticket pricing system
#input from user
age = int(input("Enter age: "))
day = input("Enter day of week: ")
tickets = int(input("Enter number of tickets: "))
#ticket price based on age
if age < 3:
    price = 0
elif age >= 3 and age <= 12:
    price = 150
elif age >= 13 and age <= 59:
    price = 300
else:
    price = 200

print("Base price per ticket: ₹", price)
#discount based on day
#discount only on Friday, Saturday and Sunday
if day == "Friday" or day == "Saturday" or day == "Sunday":
    discount = price * 20 / 100   # 20% discount
else:
    discount = 0

print("Discount per ticket: ₹", discount)
# price after discount
final_price = price - discount
print("Price after discount per ticket: ₹", final_price)
# total amount to pay
total = final_price * tickets
print("Total amount: ₹", total)