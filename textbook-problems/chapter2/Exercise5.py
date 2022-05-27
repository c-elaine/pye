#Exercise 5: Write a program which prompts the user for a celcius temp, convert the temp to Farenheit
#and print out the converted temperature. 

userTemp = int(input("Enter a temperature in Celsius: "))
tempInFarenheit = userTemp + 32
print(userTemp, " degrees celsius is", tempInFarenheit, " in Farenheit.")