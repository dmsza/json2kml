#####################################################################################
# Python script to convert Google Maps JSON file to Sygic "items.dat" favorites
# Copyright (C) 2017 Dimitri Souza
# https://github.com/dmrsouza/json2kml
#####################################################################################
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3 as published by
# the Free Software Foundation.
#####################################################################################
   
import json
import sys
import codecs
import sqlite3
import os
import math
import time

inputFile = "Saved Places.json"
outputFile = "items.dat"

# JSON Encoding is UTF-8. Change stdout to UTF-8 to prevent encoding error
# when calling print titles inside the loop
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print ('Opening file "'+inputFile+'"')

with open (inputFile) as jsonFile:
    data = json.load (jsonFile)
    
print ('Creating file "'+outputFile+'"')
if os.path.isfile(outputFile):
    os.remove (outputFile)
sqlConn = sqlite3.connect(outputFile)
sqlCmd = sqlConn.cursor()
sqlCmd.execute ('''CREATE TABLE items (
                    [id] INTEGER PRIMARY KEY,
                    [data] TEXT,
                    [lon] INTEGER,
                    [lat] INTEGER,
                    [type] INTEGER,
                    [priority] INTEGER,
                    [created] INTEGER NOT NULL,
                    [category] INTEGER NOT NULL,
                    [servicedata] TEXT)''')
sqlConn.commit()

count = 0
for place in data["features"]:
    if place["geometry"]["type"] == "Point":
        title = place["properties"]["Title"]
        print ('Parsing place "'+title+'"')
        
        placeLocation = place["properties"]["Location"]
        lon = place["geometry"]["coordinates"][0]
        lat = place["geometry"]["coordinates"][1]
        
        if "Address" in placeLocation:
            address = placeLocation ["Address"]
        else:
            address = "N/A"

        # Lon/Lat: Sygic uses an integer + 5 decimals without decimal point
        lonStrSygic = str(math.trunc(lon))+str(math.trunc(100000*math.copysign(math.modf(lon)[0],1)))
        latStrSygic = str(math.trunc(lat))+str(math.trunc(100000*math.copysign(math.modf(lat)[0],1)))

        insertCmd = "INSERT INTO items VALUES ("
        insertCmd = insertCmd + str (count+1) + "," #ID
        insertCmd = insertCmd + '"' + title + '!#$' + title + '",' #Data
        insertCmd = insertCmd + lonStrSygic + "," #Lon
        insertCmd = insertCmd + latStrSygic + "," #Lat
        insertCmd = insertCmd + "779," #Type
        insertCmd = insertCmd + "-1000000," #Priority
        insertCmd = insertCmd + str(int(time.time())) + "," #Created
        insertCmd = insertCmd + "0," #Category
        insertCmd = insertCmd + "'')" #Servicedata
        
        sqlCmd.execute(insertCmd)
        #print (insertCmd) #Debug

        count += 1
        
print ('Saving file "'+outputFile+'"')

sqlConn.commit()
sqlConn.close() 

print ('Done! Total of '+str(count)+' places saved to Sygic Favorites file.')
