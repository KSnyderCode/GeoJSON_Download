# PennShare_Data_Download
Downloads GeoJSON files from PennDOT's PennShare Portal

## How To Use
This was created as a simple solution to pull GeoJSON files from the Pennsylvania Department of Transportation's [PennShare](https://data-pennshare.opendata.arcgis.com/) Data Repository.

This was written to be a relatively quick way to pull multiple GeoJSON files from a single repository as opposed to having to pull many shapefiles. It establishes a working directory where the user specifies and then does the rest! 

## Required Packages:

Most packages should come with the standard python 3 installation. 

    datetime
    json
    os
    time
    urllib
    urllib.request
