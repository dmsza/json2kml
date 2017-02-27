# Export Google Maps saved/starred locations to KML/CSV/Sygic

This repository contain three Python 3 scripts that can be used to **export starred locations from Google Maps to other formats** which then can be imported on 3rd party GPS navigation apps. The three scrips are:

* **json2kml**: this script converts the list of starred/saved places (a.k.a. POIs) from Google Maps into a KML file that can be imported into various GPS navigation applications (suchs as MAPS.ME).

* **json2csv**: this script converts the list of starred/saved places (a.k.a. POIs) from Google Maps into a CSV (*Comma Separated Values*) file that can be imported into some POI convertion tools or edited directly in Excel.

* **json2sygic**: this script converts the list of starred/saved places (a.k.a. POIs) from Google Maps into the internal format used by Sygic Android to save its favorites ("items.dat") file.


## How to export Google Maps saved/starred locations

1.	Go to Google Takeout (https://takeout.google.com/settings/takeout). 
2.	Click “Select None” and then select “Maps (your places)”. Make sure this is the only option selected.
3.	Google will export a ZIP file. Save this file to your local disk, open it and extract the file “\Takeout\Maps (your places)\Saved Places.json” to a directory in our PC (do not change the file name).
4.	Download one of the scripts below and save to the same directory where you saved "Saved Places.json".

## json2kml

This script depends on “SIMPLEKML” library (https://simplekml.readthedocs.io/) and it can be installed via pip with the following command line:

pip install simplekml

After this, the following steps must be executed to generate the KML file from the Google Maps starred/saved locations:

1. First go to Google Takeout and save the "Saved Places.json" file to the same folder where the script is located. More details in the above section _"How to export Google Maps saved/starred locations"_.
2. Open a command prompt, change the current directory to where the above files were saved, and run the script with the command line _“python json2kml.py”_
3.	The script will run and will create the file _“Saved Places.kml”_.

## json2csv
_[ Documentation in progress... ]_

1. First go to Google Takeout and save the "Saved Places.json" file to the same folder where the script is located. More details in the above section _"How to export Google Maps saved/starred locations"_.
2. Open a command prompt, change the current directory to where the above files were saved, and run the script with the command line _“python json2csv.py”_
3. The script will run and will create the file _“Saved Places.csv”_.
4. Use this file with other convertion tools or open it in Excel.

## json2sygic
_[ Documentation in progress... ]_

1. First go to Google Takeout and save the "Saved Places.json" file to the same folder where the script is located. More details in the above section _"How to export Google Maps saved/starred locations"_.
2. Open a command prompt, change the current directory to where the above files were saved, and run the script with the command line _“python json2sygic.py”_
3. The script will run and will create the file _“items.dat”_.
4. Copy the file _“items.dat”_ to your Android device. See notes below for more details about the folder to where this file must be copied.

Notes:

* In Android devices, Sygic saves the favorites into file "items.dat". This file is located in folder _"/Sygic/Res/db/items.dat"_ if Sygic is configured to use internal storage or in folder _"/Android/data/com.sygic.aura/files/Res/db/items.dat"_ if Sygic is configured to use external SD card.
* This script creates a new "items.dat" file with all saved places from Google. This file needs to be copied to one of the above foldres.
* **IMPORTANT**: when overwriting "items.dat" files, **all current Sygic favorites _will be lost_**. Keep this in mind.

