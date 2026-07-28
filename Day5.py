# If statement
age = 16
if age >= 18:
    print ("you are an adult")

#If Else odd/even
num = 0
if num % 2 == 0:
    print ("Even")
else:
    print ("Odd")

# ElIf statement 
mark = 85
if mark >= 90:
    print ("First Class")   
elif mark >= 70:
    print ("Average")
elif mark >= 50:
    print ("Lower")
else:
    print ("Failed")

# Nested If
age = 17
id = True
if age >= 18:
    if id:
        print ("You can watch The Movie")
    else:
        print ("Buy a Ticket")

else:
    print ("Too young/not elligible")