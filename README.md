# Export Google Maps saved/starred/favorite locations to KML/CSV/Sygic

This repository contain 4 [Python 3](https://www.python.org/downloads/) scripts that can be used to **export starred locations from Google Maps to other formats** which then can be imported by GPS navigation apps or other POI convertion tools. The three scrips are:

* **csv2kml**: Export Favorites / Flagged Places / Want To Go / and custom lists.

* **json2kml**: this script converts the list of starred/saved places (a.k.a. POIs) from Google Maps into a **KML file** that can be imported into various GPS navigation applications (suchs as MAPS.ME).

* **json2csv**: this script converts the list of starred/saved places (a.k.a. POIs) from Google Maps into a **CSV** (*Comma Separated Values*) file that can be imported into some POI convertion tools or edited directly in Excel.

* **json2sygic**: this script converts the list of starred/saved places (a.k.a. POIs) from Google Maps into the internal format used by Sygic Android to save its favorites (**"items.dat"**) file.

## How to export Google Maps saved/starred locations to a JSON file

1.	Go to Google Takeout (https://takeout.google.com/settings/takeout). 
2.	Click “Select None” and then select
- “Maps (your places)”.
- "Saved" Collections of saved links (images, places, web pages, etc.) from Google Search and Maps
3.	Google will export a ZIP file. Save this file to your local disk, open it and extract the file “\Takeout\Maps (your places)\Saved Places.json” to a directory in your PC (do not change the file name).

## csv2kml

Google Takeout stores several files as CSV:

- Saved/Favourite places.csv
- Saved/Flag.csv
- Saved/Want to go.csv

First you need a Google API key:

- If needed, greated a Google Cloud Project
- Enable Places API
- Goto <https://console.cloud.google.com/apis/credentials>
- Click: Create credentials
- Copy API key
- Run this and paste to save key:

    install -D /dev/stdin -m 600 ~/.private/google-api

This script depends on `mako` so `pip3 install mako`.

Run it like this:

    ./csv2kml.py sample/takeout.csv > output.kml 

Checked `failed.csv` for entries we were not able to convert.

## json2kml

This script depends on [“SIMPLEKML” library] (https://simplekml.readthedocs.io/) and it can be installed via pip with the following command line (on Windows you may need to run this command in Command Prompt _Admin_):
```
pip install simplekml
```
After this, the following steps must be executed to generate the KML file from the Google Maps starred/saved locations:

1. First go to Google Takeout and save the _"Saved Places.json"_ file to a folder on your local disk. More details in the above section ["How to export Google Maps saved/starred locations"] (#how-to-export-google-maps-savedstarred-locations-to-a-json-file).
2. Download and save the Python script [json2kml.py] (https://raw.githubusercontent.com/dmrsouza/json2kml/master/json2kml.py) to the same folder where the file _"Saved Places.json"_ is located.
3. Open a command prompt, change the current directory to where the above files were saved, and run the script with the command line `python json2kml.py`
4.	The script will run and will create the file _“Saved Places.kml”_.

## json2csv

1. First go to Google Takeout and save the _"Saved Places.json"_ file to a folder on your local disk. More details in the above section ["How to export Google Maps saved/starred locations"] (#how-to-export-google-maps-savedstarred-locations-to-a-json-file).
2. Download and save the Python script [json2csv.py] (https://raw.githubusercontent.com/dmrsouza/json2kml/master/json2csv.py) to the same folder where the file _"Saved Places.json"_ is located.
3. Open a command prompt, change the current directory to where the above files were saved, and run the script with the command line: `python json2csv.py`
4. The script will run and will create the file _“Saved Places.csv”_.
5. Use this file with other convertion tools or open it in Excel.

## json2sygic

1. First go to Google Takeout and save the _"Saved Places.json"_ file to a folder on your local disk. More details in the above section ["How to export Google Maps saved/starred locations"] (#how-to-export-google-maps-savedstarred-locations-to-a-json-file).
2. Download and save the Python script [json2sygic.py] (https://raw.githubusercontent.com/dmrsouza/json2kml/master/json2sygic.py) to the same folder where the file _"Saved Places.json"_ is located.
3. Open a command prompt, change the current directory to where the above files were saved, and run the script with the command line `python json2sygic.py`
4. The script will run and will create the file _“items.dat”_.
5. Copy the file _“items.dat”_ to your Android device. See notes below for more details about the folder to where this file must be copied. **IMPORTANT**: when overwriting "items.dat" files, **all current Sygic favorites _will be lost_**. Keep this in mind.

**Notes:**

* In Android devices, Sygic saves the favorites to file "items.dat" (it's a SQLite3 database). This file is located in folder _"/Sygic/Res/db/items.dat"_ if Sygic is configured to use internal storage or in folder _"/Android/data/com.sygic.aura/files/Res/db/items.dat"_ if Sygic is configured to use external SD card.
* This script creates a new "items.dat" file with all saved places from Google. This file needs to be copied to one of the above foldres.
* **IMPORTANT**: when overwriting "items.dat" files, **all current Sygic favorites _will be lost_**. Keep this in mind.

