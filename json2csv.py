#####################################################################################
# Python script to convert Google Maps JSON file to a CSV file
# Copyright (C) 2017 Dimitri Souza
# https://github.com/dmrsouza/json2kml
#####################################################################################
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3 as published by
# the Free Software Foundation.
#####################################################################################
   
import json
import csv
import sys
import codecs

inputFile = "Saved Places.json"
outputFile = "Saved Places.csv"

# JSON Encoding is UTF-8. Change stdout to UTF-8 to prevent encoding error
# when calling print titles inside the loop
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print ('Opening input file "'+inputFile+'"')
with open (inputFile) as jsonFile:
    data = json.load (jsonFile)
    
print ('Creating output file "'+outputFile+'"')   
with open(outputFile, 'wt') as csvfile:
    csvWriter = csv.writer(csvfile,quoting=csv.QUOTE_ALL,lineterminator='\n')
    csvWriter.writerow(['Latitude', 'Longitude', 'Name', 'Address'])
    
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
            
            csvWriter.writerow ([lat,lon,title,address])
            count += 1
        
print ('Done! Total of '+str(count)+' places saved to the CSV file.')
