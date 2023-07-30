import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts(email TEXT, count INTEGER)''')

fname = input('Enter File Name: ')
if (len(fname) <1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split()
	email = pieces[1]
	cur.execute('SELECT count FROM Counts WHERE email = ?',(email,))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (email, count)
			values(?,1)''',(email,))
	else:
		cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?',
					(email,))
	conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])

cur.close()

#  This Python code uses SQLite to create a database, read an input file (or use a default file if not provided), parse the file to find email addresses, 
#  and then count the occurrences of each email address in the file. Finally, it prints the top 10 email addresses with their respective counts in 
#  descending order. Here's a step-by-step explanation of the code:

#  The code imports the sqlite3 module to work with SQLite databases.

#  It establishes a connection to the database file named 'emaildb.sqlite'.

#  A cursor is created to interact with the database.

#  The code checks if a table named "Counts" exists in the database and, if it does, drops it to start fresh.

#  The code creates a new table called "Counts" with two columns: "email" of type TEXT and "count" of type INTEGER.

#  The user is prompted to enter a file name, and if no input is provided, it uses the default file "mbox-short.txt".

#  The code opens the file specified by the user or the default file "mbox-short.txt".

#  It reads the file line by line and looks for lines that start with "From:".

#  If a line starts with "From:", it extracts the email address from that line.

#  The code then checks if the email address already exists in the database. If it doesn't exist, it inserts a new row with the email address and an initial count of 1. If it exists, it updates the count for that email address by incrementing it by 1.

#  After processing all lines in the file, the changes are committed to the database using conn.commit().

#  The code then constructs an SQL query to select the top 10 email addresses with the highest counts in descending order.

#  It executes the query and prints the top 10 email addresses along with their counts.

#  Finally, the cursor is closed.

