#Exerice 3: Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error message.
#If the score is between 0.0 and 1.0, print a grade using the following table:

'''
>= 0.9 is Grade A
>= 0.8 is Grade B
>= 0.7 is Grade C
>= 0.6 is Grade D
< 0.6 is Grade F
'''
#Answer:
#Try and Except used for if the input does not follow requirements. 
try: 
 userScore = float(input("Enter score: "))
 scores = userScore
except: 
    print("Please enter a numeric value.")
    exit()

#If statement checks whether the input given is between the required ranges, if so: it will print a grade.

if userScore >= 0.9:
    print("Well Done! You achieved a Grade A!")
elif userScore >= 0.8:
    print("Not bad, you got a Grade B!")
elif userScore >= 0.7:
    print("Sweet! You achieved a Grade C")
elif userScore >= 0.6:
    print("Ahh. Perhaps a little more practise is needed. You achieved a Grade D.")
elif userScore < 0.6:
    print("Oh no! Unfortunately you've failed. Grade F.")
else:
    print("Error: The score you have entered is out of range.")
    
#This exercise is a example of chained conditionals. 