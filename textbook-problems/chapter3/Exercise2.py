'''Exercise 2: Rewrite your pay program using try and except so that your program
handles the non-numeric input gracefully by printing a message 
and exiting the program. 
'''
try:
    userHours = float(input("Enter the number of hours you worked: "))
    userRate = float(input("Enter your rate pay: "))
    grossPay = userRate * userHours
except:
    print("Please enter a numeric value.")
    exit()
if userHours > 40.0:
    grossPay = (userRate * 1.5) * userHours
print("You earned: ", grossPay)
