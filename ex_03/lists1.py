fhand = open() #Opens the specified text file. 

for line in fhand:
    line = line.rstrip() #For every line in the text file, strip it of its new line.
    if not line.startwith("From..."): #If the lines don't start with From... then continue on
        continue
    words = line.split()  #Each line in the text file, split it up each word into a list. 
    print (words[2]) #Print up to but not including the 2nd word. 0-2

#The split function is useful when you want to access certain lines in a string. By putting it in an index
#Then specifing the index of the text. [1]

##The code below gets input from the user about filename, then opens the file and reads the file. 
#Splitting up each word so that it can indivdually read it. 

name = input("Enter the file name...")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for words in words:
        counts[words] = counts.get(words, 0) + 1 #22nd March: Review this line. Not 100% understood.

bigcount = None
bigword = None #Review the use of None 

##This is a maximum loop
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

