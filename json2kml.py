#####################################################################################
# Python script to convert Google Maps JSON file to a KML file
# Copyright (C) 2017 Dimitri Souza
# https://github.com/dmrsouza/json2kml
#####################################################################################
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#####################################################################################
   
import json
import simplekml

inputFile = "Saved Places.json"
outputFile = "Saved Places.kml"

print ('Opening file "'+inputFile+'"')

with open (inputFile) as jsonFile:
    data = json.load (jsonFile)
    
    
kml = simplekml.Kml ()

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
        
        kml.newpoint (name=title, coords=[(lon,lat)], address=address)
        count += 1
        
print ('Saving file "'+inputFile+'"')
kml.save (outputFile)

print ('Done! Total of '+str(count)+' places saved to the KML file.')