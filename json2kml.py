###############################################################################
# Python script to convert Google Maps JSON file to a KML file
# Copyright (C) 2017 Dimitri Souza
# https://github.com/dmrsouza/json2kml
###############################################################################
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3 as published by
# the Free Software Foundation.
###############################################################################

import json
import simplekml
import sys
import codecs
import html

inputFile = "Saved Places.json"
outputFile = f'{inputFile[:-5]} [json2kml.py].kml'

# JSON Encoding is UTF-8. Change stdout to UTF-8 to prevent encoding error
# when calling print titles inside the loop
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print(f'Opening file "{inputFile}"')

with open(inputFile, encoding='utf8') as jsonFile:
    data = json.load(jsonFile)

kml = simplekml.Kml()
kml.document.name = outputFile

count = 0
for place in data["features"]:
    if place["type"] == "Feature":
        title = html.escape(place["properties"]["Title"])
        print(f'Parsing place "{title}"')

        placeLocation = place["properties"]["Location"]
        lon = place["geometry"]["coordinates"][0]
        lat = place["geometry"]["coordinates"][1]

        if "Address" in placeLocation:
            address = html.escape(placeLocation["Address"])
        else:
            address = None

        kml.newpoint(name=title, coords=[(lon, lat)], address=address)
        count += 1

print(f'Saving file "{outputFile}"')
kml.save(outputFile)

print(f'Done! Total of {count} places saved to the KML file.')
