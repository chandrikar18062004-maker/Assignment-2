#age calculator
#ask user for their birth year
birth_year=int(input("Enter your birth year:"))
current_year=2026 #give current year
age=current_year - birth_year #it will display users age
months=age*12 #calculate in months
days=age*365 #calculate in age
hours=age*24 #calculate in hours
minutes=hours*60 #calculate in minutes
years_left=100-age #calculate years until age 100
print("Age:",age,"years") #prints age
print("Age in months:",months) #prints age in monts
print("Age in days:",days) #prints age in days
print("Age in hours:",hours) #prints age in hours
print("Age in minutes:",minutes) #prints age in minutes
print("Years left until age 100:",years_left) #prints year until age 100
