#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.
#FIND, EXTRACT, CONVERT TO FLOAT AND THEN PRINT; DONT FORGET THE COUNT STARTS WITH ZERO!!
#Desired Output = 0.8475

text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':') # Find the position of the colon
number_str = text[x +1:].strip() # Extract the number portion after the colon
number=float(number_str) # Convert the extracted value to a floating-point number
print(number) # Print the extracted floating-point number



