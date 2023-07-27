# CALLING A JSON API: #In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will 
# prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A 
# place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
#   Creating an empty dictionary called 'parms'
    parms = dict()
#	The assignment of a key variable called address within the parms dictionary.
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
 #  This line constructs the URL for the API call. It appends the encoded parameters from the parms dictionary to the serviceurl. 
 #  The urllib.parse.urlencode() function converts the dictionary into a URL-encoded query string format, which is necessary for making the 
 #  API call with the required parameters.
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')#

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place_id = js['results'][0]['place_id']
    print(place_id)

# This Python script is a simple geocoding application that allows you to input a location (address) and retrieve its corresponding geographical information, 
# particularly the "place_id" associated with that location. The script uses either a Google Places API key or a default service URL, depending on whether 
# the "api_key" variable is set to a valid API key or not.

#Here's a breakdown of how the script works:

# 1.  The script begins by importing necessary modules: urllib.request, urllib.parse, urllib.error for handling URLs and json for parsing JSON data.

# 2.  The variable api_key is set to False, indicating that there is no Google Places API key provided initially.

# 3.  If an API key is not provided (api_key is False), the script sets a default service URL to a non-Google API endpoint. Otherwise, if there's an API key 
#     provided, the script uses Google Maps Geocoding API service URL.

# 4.  The script then ignores SSL certificate errors using ssl.create_default_context().

# 5.  The script enters a while loop, prompting the user to enter a location (address) to be geocoded. The loop continues until the user enters an empty string 
#     (just presses Enter without typing anything).

# 6.  Inside the loop, the address input is encoded into a URL parameter using urllib.parse.urlencode(), and the URL to make the API call is constructed using 
#     the service URL and the encoded parameters.

# 7.  The script then sends a request to the geocoding service URL using urllib.request.urlopen() while also passing the SSL context.

# 8.  The response is read and decoded, containing the JSON data returned by the geocoding service.

# 9.  The script tries to parse the JSON data using json.loads(), and if successful, it checks whether the response status is 'OK', indicating a successful 
#     geocoding response.

# 10. If the JSON parsing is successful and the status is 'OK', the script prints the JSON data in a nicely formatted way using json.dumps() with an 
#     indentation of 4.

# 11. The script extracts the "place_id" from the JSON response and prints it on the screen.

# 12. Note: The "place_id" is a unique identifier provided by the geocoding service for a specific location. It is useful when working with Google Maps APIs, 
#     as it allows you to refer to specific places in their database.

# 13. To use this script, you can run it and enter the location you want to geocode when prompted. If you have a Google Places API key, you can uncomment 
#     the relevant line and replace the placeholder with your actual API key. Otherwise, the script will use the default service URL with limited capabilities.
