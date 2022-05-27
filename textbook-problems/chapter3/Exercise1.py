#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the 
#hourly rate for hours worked above 40 hours. 

userHours = float(input("Enter the hours you worked: "))
userRate = float(input("Enter your rate: "))

grossPay = userHours * userRate

if userHours > 40.0:
    grossPay = (userRate * 1.5) * userHours
print("You earned: ", grossPay, " today")