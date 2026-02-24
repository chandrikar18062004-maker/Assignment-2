#grade calculator
#input
#lets assume s1,s2,s3,s4,s5 as different subjects
s1=int(input("Enter marks 1:"))
s2=int(input("Enter marks 2:"))
s3=int(input("Enter marks 3:"))
s4=int(input("Enter marks 4:"))
s5=int(input("Enter marks 5:"))
total=s1+s2+s3+s4+s5 #cal total marks
percentage=total/500*100 #cal percentage
#here we are decide grades based on percentage
if percentage >=90: 
    grade="A+"
elif percentage >=80:
    grade="A"
elif percentage >=70:
    grade="B"
elif percentage >=60:
    grade="C"
elif percentage >=50:
    grade="d"
else:
    grade="F"
#display results
if s1<40 or s2<40 or s3<40 or s4<40 or s5<40:
    result="Fail"
else:
    result="Pass"
print("Marks:",s1,s2,s3,s4,s5) #prints marks for each sub
print("Total matks:",total) #prints total marks
print("Percentage:", percentage,"%") #prints percentage
print("Grade:",grade) #prints grade
print("Result:",result) #prints result