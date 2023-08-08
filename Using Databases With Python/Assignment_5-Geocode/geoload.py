
#  Python script for retrieving and storing geographical data using the Google Places API (or a fallback service). A breakdown of what the script does:

#  1.  Importing Required Libraries: The script starts by importing several libraries that will be used for different tasks, such as handling HTTP requests, 
#      working with SQLite databases, and processing JSON data.

#  2.  API Key Setup: The script has a section to set up an API key. If no API key is provided, it sets api_key to a default value of 42. If you have a 
#      Google Places API key, you can uncomment the line with your actual API key.

#  3.  Service URL Setup: Depending on whether an API key is provided or not, the serviceurl is set to the appropriate URL for either the Google Maps 
#      Geocoding API or a fallback service.

#  4.  Database Initialization: The script connects to an SQLite database called geodata.sqlite and creates a table named "Locations" with columns "address" 
#      and "geodata" if it doesn't already exist.

#  5.  Ignoring SSL Certificate Errors: SSL certificate verification is disabled using a custom SSL context. This is not recommended in production environments, 
#      but it's used here to allow the script to continue even if SSL certificate errors occur.

#  6.  Reading Input Data: The script reads input data from a file named "where.data." It appears that this file contains addresses, one per line.

#  7.  Processing Addresses: The script iterates through the lines in the input file. For each address, it performs the following steps:

#    7.1  It checks if the address is already present in the database. If it is, the geodata is fetched from the database, and the loop continues to the 
#         next address.

#    7.2  If the address is not found in the database, the script constructs a URL with the address as a query parameter and sends an HTTP request to the 
#         specified service URL.

#    7.3  It reads the response data and parses it as JSON.

#    7.4  If the response status is not "OK" or "ZERO_RESULTS," an error message is printed, and the loop breaks.

#    7.5  If the response status is valid, the address and geodata are inserted into the database, and the loop may pause for a short time after every 
#         10 records.

#    7.6  Final Steps: After processing the addresses, the script suggests running another script named "geodump.py" to read the data from the database 
#         and visualize it on a map.

##############################################################################################################################################################

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
