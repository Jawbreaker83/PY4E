#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#""From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"" Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.
#Desired Output --> 
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
#######################################################################################################################################

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()#initializing an empty list
di=dict()#initializing a new dictionary object
for line in handle:
    if line.startswith("From "):
        pos=line.find(":")
        lst.append(line[pos-2:pos])
for word in lst:
    di[word]=di.get(word,0)+1
newlst=list()
for key,val in di.items():
    newtup=(key,val)
    newlst.append(newtup)
newlst=sorted(newlst)
for key,val in newlst:
    print(key,val)