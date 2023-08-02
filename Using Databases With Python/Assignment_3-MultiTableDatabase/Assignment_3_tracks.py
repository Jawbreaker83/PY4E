import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

########################################################################################################################################################
#  The script below prompts the user to enter a file name by displaying the message 'Enter file name: '. If the user enters a non-empty string,
#  t assigns the entered filename to the variable fname. Otherwise, it sets fname to 'Library.xml'.
#  The lookup() function is defined to find and return the value associated with a given key in a dictionary d (which is represented as a list 
#  of child elements). It iterates through the children of the dictionary (assuming the XML structure), looking for a <key> element with text matching 
#  the provided key. Once the key is found, the next element (which should contain the value) is returned. If the key is not found, the function returns None.
#  To use the lookup() function properly, you need to provide it with a dictionary (list of elements) that represents an XML element with key-value pairs, 
#  such as the dictionaries found in the iTunes Library XML file. For example, you could use it like this:

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None
########################################################################################################################################################

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : 
        continue

    print(name, artist, genre, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        (name, album_id, genre_id, length, rating, count ) )

    conn.commit()

############################################################################################################################################################

#  This Python script is designed to parse an iTunes Library XML file and populate a SQLite database with the track information from the XML file. 

#  1.  The script starts by importing the required modules, xml.etree.ElementTree for XML parsing and sqlite3 for working with SQLite databases.

#  2.  It establishes a connection to the SQLite database and creates four tables named Artist, Genre, Album, and Track.

#  3.  The script prompts the user to enter the name of the iTunes Library XML file to be processed. If no filename is provided, it defaults to 'Library.xml'.

#  4.  The lookup() function is defined to extract values from the XML file using the provided key.

#  5.  The script opens the XML file, extracts all the nested dictionaries, and stores them in the all variable.

#  6.  It then iterates through each dictionary (representing a track) in the XML file.

#  7.  For each track, it extracts the values for Name, Artist, Genre, Album, Play Count, Rating, and Total Time using the lookup() function.

#  8.  If any of the essential fields (Name, Artist, or Album) are missing for a track, the track is skipped, and the script moves on to the next one.

#  9.  If the essential fields are available, the script proceeds to insert or ignore the corresponding data into the Artist, Genre, and Album tables. 
#      It uses the INSERT OR IGNORE clause to avoid inserting duplicate values.

#  10.  After inserting the artist, genre, and album data (if they don't already exist), the script retrieves the corresponding artist_id, genre_id, 
#       and album_id from their respective tables.

#  11.  Finally, the script inserts or replaces the track information into the Track table with the data gathered from the XML file.

#  12.  After processing all the tracks in the XML file, the script commits the changes to the database.

