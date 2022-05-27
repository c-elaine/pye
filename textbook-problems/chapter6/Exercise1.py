#Exercise 1: Write a while loop that starts at the last character in the string and works it's way backwards
#to the first character in the string, printing each letter on a separate line, except backwards. 

userWord = input("Enter: ") #Get the user to type in something....
length = len(userWord) #Create a new variable and place the resulting value of it's length. E.g: User inputs: hello. len function will return the number 5 as there are 5 characters in the word. 
index = 1  


while index <= length:
    lastChar = userWord[length - index] 
    letter = lastChar
    print(letter)
    index = index + 1


   