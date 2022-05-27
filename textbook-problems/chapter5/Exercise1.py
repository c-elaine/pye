'''
Exercise 1:
Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
'''
'''
while True: 
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")
'''

'''
count = 0 
userTotal = 0

while True: 
    try: 
        userNum = int(input("Enter a numeric value: "))
        count = count + 1
        userTotal = userTotal + userNum
        userAverage = userTotal / count
    except:
        if userNum == "done" or userNum != int:
         print("Done!")
        break
print("Count: ", count, "Total: ", userTotal, "Average: ", userAverage)
'''

#The above solution took 3-4ish days to get correct because of i didn't completely understand loops.
#But eventually we got there by drawing out flow charts, psuedocode and trying and testing multiple
#methods. We just had to give it time to let the brain process the concept. Parsing code is now 
#much easier. (Completed 27th March 2022) 

#Addition: The above code doesn't have the last bit, printing out an error message for anything but
#Integer values. The code, although it works, is messy and adding a new feature is difficult the 
#way it is currently written. Still learning. 

#Solution found on Github: 
'''

def check_for_float(input1, exit = True):  #This function checks serves the purpose of checking input type.
    try:
        val = float(input1)
        return val
    except (ValueError, TypeError):
        print("Error: Please enter a numeric value.")
        if exit: 
            quit()
        return False

if __name__ == "__main__":
    count = 0
    total = 0.0
    average = 0.0

    while True: 
        input_number = input("Enter a number: ")
        if input_number == "done":
            break

        number = check_for_float(input_number, False)
        if not number:
            continue 

        count += 1 
        total = total + number 
    
    if count: 
        average = total / count 
    print(total, count, average)
'''
    #Correction: 

count = 0 
userTotal = 0

while True: 
    try: 
        sNum = input("Enter a numeric value: ")
        intNum = int(sNum) #Convert separately and place in a separate box so we can use 2 types. This was the fix we needed. Separating things out into objects to better handle data. 
        count = count + 1
        userTotal = userTotal + intNum 
        userAverage = userTotal / count
    except:
        if sNum != "done":
            print("Error: Please enter a numerical value.")
            continue
        elif sNum == "done":
         print("Done!")
        break
print("Count: ", count, "Total: ", userTotal, "Average: ", userAverage)

