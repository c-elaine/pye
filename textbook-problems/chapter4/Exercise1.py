#Exercise 1: Completed in the IDLE
#Exercise 2: Move the last line of this program to the top, so the function
#call appears before the definitions. Run the program and see what error
#message you get.

#Answer: The function has not been defined. Thus the error is a runtime error. 
#Trying to call a function that doesn't exist yet. 

def print_lyrics():
 print("I'm a lumberjack, and I'm okay.")
 print('I sleep all night and I work all day.')

def repeat_lyrics():
 print_lyrics()
 print_lyrics()

repeat_lyrics()

#Exercise3: Move the function call back to the bottom and move the
#definition of print_lyrics after the definition of repeat_lyrics. What
#happens when you run this program?

#Answer: Nothing? Interesting...
