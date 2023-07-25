#In this program, we start by prompting the user to enter the file name. The program attempts to open the file 
#and handles the case when the file is not found.
#Then, using a for loop, we iterate over each line in the file. For lines starting with "X-DSPAM-Confidence:", 
#we find the position of the colon character (":") and extract the floating-point value after it. We accumulate the count and sum 
#of these values in total_count and total_value variables.
#After processing all lines, we close the file and check if any lines were found. If so, we compute the average value by 
#dividing the sum (total_value) by the count (total_count) and print the result. If no lines were found, we print a corresponding message.

file_name = input("Enter the file name: ")

try:
    file_handle = open(file_name, 'r')
except FileNotFoundError:
    print("File not found.")
    quit()

total_count = 0
total_value = 0.0

for line in file_handle:
    if line.startswith("X-DSPAM-Confidence:"): 
        colon_pos = line.find(":") #variable to locate the position of the ":" and to extract the floating-point value following it;
        value = float(line[colon_pos+1:].strip()) #create a new variable and look for the colon position +1 and then strip away all nonprintable characters;
        total_count += 1
        total_value += value

file_handle.close()

if total_count > 0:
    average_value = total_value / total_count
    print("Average spam confidence:", average_value)
else:
    print("No lines starting with 'X-DSPAM-Confidence:' found.")
