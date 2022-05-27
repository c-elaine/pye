'''total = 0
count = 0 
while True: 
    inp = input("Enter a number....")
    if inp == "Done":
        break
    value = float(inp)
    total = total + value 
    count = count + 1
average = total / count 
print ("Average: ", average)'''

#New Version, that uses more memory 

numList = list()
while True: 
    inp = input("Enter a number....")
    if inp == "Done" :
        break
    value = float(inp)
    numList.append(value)
average = sum(numList) / len(numList) 
print("Average: ", average)

