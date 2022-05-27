#Exercise 3: Write a program to prompt the user for hours and rate per hour 
#to compute gross pay.

userHours = float(input("Enter the number of hours you work: "))
userRate = float(input("What is your rate per hour?: "))

grossPay = (userHours * userRate)
print("Today, you earned:", grossPay)