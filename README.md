# Various-Python-2.x
Contains small scripts for various purposes written mostly in Python 2.7


### Abruf2.py

*Date: 2011*

Used to extract point data to use for cliamte diagrams later.

Uses ESRI ASCII rasters (quite specific 3600x3200) in Gauss-Kruger coordinates (EPSG:31467)
and calculates for a specific Hochwert/Rechtswert pair monthly averages.

Script uses all files in input folder (no in script control over start and end-points)


### AVHRR_rename.py

*Date: 2015*

Simple renaming script, used specifically for AVHRR files to convert in ENVI format

Basically adds a file extension (.BSQ) to each file and copies it to a new folder. Also,
the same header file is renamed to match each new BSQ-file and copied to folder as well
