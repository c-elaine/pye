#Exercise3: Encapsulate this code in a function named count, and generalize it so that it accepts
#the string and the letter as arguements

'''
word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)
'''
word = 'banana'

def count(letter, word): # those in the brackets are the parameters. 
   
    counter = 0 

    for letter in word:
        if letter == 'a':
            counter = counter + 1
            print(counter)
    
input_word = input("Enter a word: ") #these are the arguements. 
input_letter = input("Enter a letter: ")

count(input_letter, input_word) 