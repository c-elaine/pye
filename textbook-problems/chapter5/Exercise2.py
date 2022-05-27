#Exercise 2: Write another program that prompts for a list of numbers and at
#the end prints out both the maximum and minimum of the numbers instead of the average.

largest = None
smallest = None
numList = list()

while True: 
  try:
    sNum = input("Enter a number: ")
    iNum = int(sNum)
    numList.append(iNum)
  except:
      if sNum != "done":
          print("Error: Please enter a numeric value.")
          continue
      elif sNum == "done":
          print("Done!")
          break
print("Maximum Value: ", max(numList), "Minimum Value: ", min(numList))