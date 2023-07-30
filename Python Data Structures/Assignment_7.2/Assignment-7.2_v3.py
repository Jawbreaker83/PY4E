
total=0
count=0

fname = input("Enter file name: ")

fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : #iteration looking for the 'X-DSAM...' if not found continue however if located run the code;
    	continue
    count=count+1 #counting the lines;
    pos=line.find(':') #to locate the ':' in order to extract the float value within the line;
    value=line[pos+1:] #from the position + 1 to the end of the line perform the extraction;
    total=total+float(value)
    avg=total/count
print("Average spam confidence:",avg)
