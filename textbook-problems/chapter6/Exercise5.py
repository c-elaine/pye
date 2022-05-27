'''
data = "From itskeeliin@gmail.com 1st April 2022"
atPos = data.find("@") #invoking the find method, we assign a variable to contain the length at which the @ symbol occurs. 
print(atPos)

sppos = data.find(" ", atPos) #another variable storing when the first empty space after @ occurs. 
print(sppos)

host = data[atPos+1:sppos] #a variable that contains the index of the letter to the space. 
print(host)
'''

#Exercise 5: Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted string into a floating point number.

strData = 'X-DSPAM-Confidence:0.8475'
strFloat = strData.find(":")
print(strFloat)


strFloatData = strData.find("5") + 1
print(strFloatData)

hostStr = strData[strFloat+1:strFloatData]

print(float(hostStr))

