# GeoJSON_Download
Performs API calls from a GeoJSON endpoint and writes that file to disk. 

## How To Use
The original inception of this was created as a simple solution to pull GeoJSON files from the Pennsylvania Department
of Transportation's [PennShare](https://data-pennshare.opendata.arcgis.com/) Data Repository.

Initially this was written to be a relatively quick way to pull multiple GeoJSON files from a single repository. It
required the user to manually code in the parameters for the download function into the script. While this was a quick
solution, it was a bit clunky by requiring the user to consistently edit the function parameters. 

The code has been entirely refactored. This code is now entirely based around defined functions. 
It now reads in user input for file names and GeoJSON endpoints and reads the user input values into a nested dictionary.
This dictionary is then iterated through to create files with the respective filenames and then will insert the data 
from the GeoJSON endpoint into each corresponding file. 

## Script Workflow

1. Prints initial timestamp
2. Prompts user for where they'd like to establish a working directoy
3. Creates a working directory for all files to be downloaded into
4. Prompts user for number of files to be downloaded
5. Prompts user to input FILENAME, URL for each geojson to be downloaded
    - Initializes blank dictionary
    - User inputs each pair of FILENAME/URL
    - User input is read into a nested dictionary
6. Iterates through the nested dictionary and creates a file, and then inserts data from GeoJSON endpoint into the file
and writes to disk. 
7. Prints final time stamp


*Note: The term "GeoJSON endpoint" refers to the URL where the GeoJSON file can be downloaded from.*

## Example output



    Initiating Data Refresh 
    Current time:  2021-08-24 12:16:20.407291  

    Please input the location you'd like to save your files.
    /Home/User/Documents/
    You entered: /Home/User/Documents/
    How many files would you like to download?
    1
    Numbers of files to read in: 1 

    enter FILENAME: PA_Municipal_Boundaries
    enter URL: https://opendata.arcgis.com/datasets/6de644ae6a07465c97d24ed91812db8d_2.geojson

    Downloaded: PA_Municipal_Boundaries


    Time to execute program:  0:00:25.147668

## Required Packages:

All packages required through this script are included in the Python3 standard library

1. datetime
2. json
3. os
4. urllib
5. urllib.request