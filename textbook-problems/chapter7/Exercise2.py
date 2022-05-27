'''
Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
90 CHAPTER 7. FILES
values from these lines. When you reach the end of the file, print out
the average spam confidence.
'''

userInput = input("Enter a file name: ")
userFile = open(userInput)

index = 1

for lines in userFile:
    if lines.startswith("X-DSPAM-Confidence:"):
        startLine = lines.find(":") #Finds the position of the :
        lastChar = lines.find("5") + 1 
        hostLine = lines[startLine+1:lastChar]
        print(hostLine)
        
        