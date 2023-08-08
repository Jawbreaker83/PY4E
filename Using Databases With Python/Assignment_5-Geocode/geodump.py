#  Processes the data stored in the geodata.sqlite database and generates a JavaScript file that can be used for displaying markers on a map. A breakdown of 
#  what this script does:

#  1.  Importing Required Libraries: The script imports the sqlite3, json, and codecs libraries.

#  2.  Database Connection: The script connects to the SQLite database named geodata.sqlite and creates a cursor object.

#  3.  Retrieving Data from the Database: The script executes a SQL query to select all data from the "Locations" table in the database.

#  4.  Creating JavaScript File: The script opens a file named where.js using UTF-8 encoding for writing. This file will contain JavaScript code that 
#      defines an array named myData to store location data.

#  5.  Loop Through Database Rows: The script iterates through the rows retrieved from the database. For each row, it:

#  5.1  Decodes the geodata column and tries to parse it as JSON.

#  5.2  Checks if the JSON data contains a "status" field with a value of "OK." If not, it continues to the next row.

#  5.3  Retrieves latitude (lat) and longitude (lng) information from the parsed JSON.

#  5.4  Removes single quotes from the formatted address to avoid potential issues.

#  5.5 Creates a string in the format [lat, lng, 'formatted_address'] to represent a location point.

#  5.6 Writing to JavaScript File: The script writes the formatted location point string to the where.js file. It also handles formatting the
#      JavaScript array structure correctly, adding commas between elements and handling the array's opening and closing brackets.

#  5.7 Cleanup and Output: After processing all rows, the cursor is closed, and the JavaScript file is closed. The script prints the number of records
#      processed and written to the where.js file.

#  5.8 Completion Message: The script suggests opening the where.html file in a browser to view the data on a map.

#  This script essentially reads geolocation data from the SQLite database, extracts relevant information, and generates a JavaScript file that can be 
#  used to visualize the data on a map using markers. To complete the visualization, you'd need to create an HTML file (likely named where.html) that 
#  includes the generated where.js script and integrates it with a mapping library like Google Maps or Leaflet to display the markers on a map.

##########################################################################################################################################################

import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

