#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program 
#creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
#Desired Output --> cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith("From "):continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) +1

bigcount = None
bigword = None
for x,y in count.items():
   if bigcount == None or y> bigcount:
     bigword = x
     bigcount = y
print(bigword, bigcount)




