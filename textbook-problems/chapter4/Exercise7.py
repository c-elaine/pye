#Exercise 7: Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.



#Below is a function created with the parameter studentScore. 
#It serves the purpose of evaluating certain conditions and returns the appropriate string.

def computerGrade(studentScore):
    if studentStore >= 0.9:
     print("Well Done! You achieved a Grade A.")
    elif studentStore >= 0.8:
     print("Nicely Done! You've achieved a Grade B")
    elif studentStore >= 0.7:
     print("Grade C!")
    elif studentStore >= 0.6:
     print("Unfortunate, you've achieved a Grade D. With a little extra work you'll be fine!")
    elif studentStore > 0.6:
     print("Oh no. You've failed and achieved a Grade F.")
    else:
     print("Error: Your score should be between 0.0 and 1.0")
    return 

#try and except for if user input is not numerical. Also below gives the parameter an argument.
#a value what will be given from input by the user. 
try:
    studentStore = float(input("Enter your score: "))
    computerGrade(studentStore)
except:
    print("Error: You did not enter a numeric value.")
    exit()

