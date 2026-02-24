#bill splitter
#input
bill=float(input("Enter total bill:")) #total bill amount
people=int(input("Number of people:")) #total number of people
tax=float(input("Tax percentage:")) #tax percentage
tip=float(input("Tip percentage:")) #tip percentage
tax=(bill*tax)/100 #cal tax
after_tax=bill+tax #cal bill after adding tax
tip=(after_tax+tip)/100 #cal tip
final_total=after_tax+tip #cal total bill 
per_person=final_total/people #cal amount per person
print("========= BILL BREAKDOWN ========= ")
print("Subtotal:",round(bill,2)) #display subtotal
print("Tax:",round(tax,2)) #display tax
print("After tax:",round(after_tax,2)) #display after tax
print("Tip:",round(tip,2)) #displays tip percentage
print("Bill:",round(final_total,2)) #displays bill
print("Amount per person:",round(per_person,2)) #displays amount per person

