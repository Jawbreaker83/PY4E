fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for x in line.split():
        if not x in lst:
            lst.append(x)
lst.sort()
print(lst)