#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#"X-DSPAM-Confidence:    0.8475".  Count these lines and extract the floating point values from each of the lines and compute the average of 
#those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
#Desired Output --> Average spam confidence: 0.7507185185185187


# Using the for loop the program iterates over each line w/in the file to check if the current line DOES NOT 
#start w/ the given string using the startswith() method; If the line does not start with that string, the loop moves to the 
#next iteration using the continue statement, skipping the remaining code and moving ont to the next line.  If the current line does 
#start with the string "X-DSPAM-Confidence:", the code prints the line using the print() function.  In summary, this code snippet 
# filters and prints only the lines in the file that start with the string "X-DSPAM-Confidence:". It discards any other lines present
#in the file.


fname = input("Enter file name: ")
fh = open(fname) 
for line in fh: 
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
print("Done")
for line in fh:
    count = count + 1
    print('line Count:', count)