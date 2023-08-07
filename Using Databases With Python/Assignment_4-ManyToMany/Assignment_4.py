#  This script creates three tables named User, Course, and Member to store data related to users, courses, and their memberships. The script then 
#  reads data from a JSON file, processes each entry, and inserts or updates the information into the respective tables.

#  A breakdown of what the script is doing:

#  1.  The script imports the required modules json and sqlite3.

#  2.  It establishes a connection to an SQLite database named rosterdb.sqlite and creates a cursor for database operations.

#  3.  The script drops the User, Member, and Course tables if they already exist, and then creates them again with the specified schema.

#  4.  The script prompts the user to enter a file name or uses a default name 'roster_data_sample.json' if no input is provided.

#  5.  The script reads the contents of the JSON file into a string variable str_data and then parses it using json.loads() to obtain a list of lists 
#      named json_data.

#  6.  The script iterates over each entry in the json_data list, extracting the name, title, and role values.

#  7.  For each entry, the script attempts to insert the user's name into the User table using the INSERT OR IGNORE statement to prevent duplicate entries. 
#      It then queries the User table to retrieve the id associated with the user's name.

#  8.  Similarly, the script inserts the course title into the Course table and queries the Course table to retrieve the id associated with the course title.

#  9.  9The script finally inserts or replaces a row in the Member table with the extracted user_id, course_id, and role values.

#  10.  After processing all entries, the script commits the changes to the database using conn.commit().

#############################################################################################################################################################

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title,))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member 
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role))

    conn.commit()