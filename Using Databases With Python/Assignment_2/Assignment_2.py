# Counting Organizations.  This application will read the mailbox data (mbox.txt) and count the number of email messages per organization 
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

# When you have run the program on mbox.txt upload the resulting database file above for grading.  If you run the program multiple times in testing or with
# different files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.  The data file for this application is the same as in 
# previous assignments: http://www.py4e.com/code3/mbox.txt.  Because the sample code is using an UPDATE statement and committing the results to the database
# as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data 
# to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of 
# operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
#############################################################################################################################################################

import sqlite3

conn = sqlite3.connect('mbox_emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    org = pieces[1].split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

#  This Python script connects to an SQLite database named 'assignment2.sqlite', creates a table called 'Counts', and then reads a file 
#  (default: 'mbox-short.txt') to find email addresses, extract the domain names (org), and count the occurrences of each domain. The top 10 
#  domains with the highest counts are then printed.

#  1.  Import the sqlite3 module, which allows Python to work with SQLite databases.

#  2.  Connect to the SQLite database named 'assignment2.sqlite' using sqlite3.connect() and create a cursor object to interact with the database.

#  3.  If the 'Counts' table already exists in the database, it will be dropped (deleted) using cur.execute('DROP TABLE IF EXISTS Counts').

#  4.  Create a new 'Counts' table with columns 'org' (TEXT) and 'count' (INTEGER) using cur.execute(). This table will be used to store the email domain counts.

#  5.  Ask the user to input a file name. If the user does not provide any input, the script will use the default file name 'mbox-short.txt'.

#  6.  Open the file using open() in a loop and iterate through each line in the file.

#  7.  Check if the line starts with 'From: '. If it does not, skip to the next line.

#  8.  If the line starts with 'From: ', extract the email domain (org) by splitting the line and getting the second element (index 1) after 
#      splitting the line by '@'.

#  9.  Query the 'Counts' table to see if the domain (org) already exists in the table using cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)).

#  10.  If the domain does not exist, insert a new row into the 'Counts' table with the domain and an initial count of 1 using cur.execute('''INSERT INTO Counts 
#       (org, count) VALUES (?, 1)''', (org,)).

#  11.  If the domain already exists in the 'Counts' table, update the count by incrementing it by 1 using cur.execute('UPDATE Counts SET count = count + 1 
#       WHERE org = ?', (org,)).

#  12.  Commit the changes to the database using conn.commit().

#  13.  Create an SQL query to select the top 10 domains and their corresponding counts from the 'Counts' table, ordered by count in descending order.

#  14.  Execute the SQL query using cur.execute() and print the results using a loop.

#  15.  Close the cursor and the connection to the database using cur.close().

#  16.  This script reads the file, counts the occurrences of each domain, and prints the top 10 domains along with their counts.