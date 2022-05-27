#Exercise 1: Write a program to read through a file and print the contents
#of the file (line by line) all in upper case. 

fhand = open("test.txt")

for lines in fhand: 
    contents = lines.rstrip().upper()
    print(contents)

#An Error returns: Built in method upper of str object at 0x0000016A1446EC10

    
