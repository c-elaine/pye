#Exercise 4: What is the purpose of the "def" keyword in Python?
#Answer: The "def" keyword indicates the defintion of a function. --> B)Indicates the 
#start of a function. 

#Exercise 5: What will the following Python program print out?
'''
Answer: 
def fred():
print("Zap")
def jane():
print("ABC")
jane()
fred()
jane()

Print out: D --> ABC, Zap, ABC
'''

#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and 
# create a function called computepay which takes two parameters
#(hours and rate)

#Try and except for incorrect input. 
try:
 userHours = float(input("Enter the number of hours you worked: "))
 userRate = float(input("Enter your rate of pay: "))
 grossPay = userHours * userRate
except:
    print("Error: You did not enter a numeric value.")
    exit()

def computePay(userHours, userRate):
 if userHours > 40:
    grossPay = (userHours * 1.5) * userRate
 else:
    grossPay = userHours *userRate
print("You have earned: ", grossPay)
