# json2kml

This is a simple Python 3 script that will convert the list of starred places in Google Maps into a KML file that can be imported into GPS navigation applications (suchs as MAPS.ME).

This script depends on “SIMPLEKML” library (https://simplekml.readthedocs.io/) and it can be installed via pip with the following command line:

pip install simplekml

After this, the following steps must be executed:

1.	Go to Google Takeout (https://takeout.google.com/settings/takeout). 
2.	Click “Select None” and then select “Maps (your places)”. Make sure this is the only option selected.
3.	Google will export a ZIP file. Open this file and extract the file “\Takeout\Maps (your places)\Saved Places.json” to a directory in our PC (do not change the file name).
4.	Download the “json2kml.py” script (https://raw.githubusercontent.com/dmrsouza/json2kml/master/json2kml.py) and save to the same directory where you saved "Saved Places.json".
5.	Opent a command prompt, change the current directory to where the above files were saved, and run the script with the command line “python json2kml.py”
6.	The script will run and will create the file “Saved Places.kml”.
