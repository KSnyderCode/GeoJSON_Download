#!/usr/bin/env python
# coding: utf-8


''' Metadata, Copyright, License:
------------------------------------------------------------------------
Name:       PennDOT Data Scrape.py
Purpose:    Download GeoJSON files from PennDOT's PennShare Portal 
Author:     Snyder, Kyle
Created:    10FEB2021
Modified:   22APR2021
Version:    1.2
License:    <Copyright (c) <2021> <Kyle Snyder>

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to 
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE.>
------------------------------------------------------------------------
'''

''' Import python modules '''
import datetime
import json
import os
import time
import urllib
import urllib.request

''' Generate start message and timestamp'''
execute_time = time.time()
start_date = datetime.date.today()
start_time = time.strftime('%H:%M:%S')
print("Initiating Data Refresh \nCurrent date:", start_date, "\nCurrent time: ", start_time)


path = input("Please input the location you'd like to save your files.\n")
print(f'You entered: {path}')


''' Specifying download path'''
directory = "Data_Refresh_" + datetime.datetime.now().strftime("%d_%b_%Y")
try:
    download_dir = os.path.join(path, directory)
    os.mkdir(download_dir) 
except:
    directory = "Data_Refresh_" + datetime.datetime.now().strftime("%d_%b_%Y") + datetime.datetime.now().strftime("_%H-%M-%S")
    download_dir = os.path.join(path, directory)
    os.mkdir(download_dir)

''' Define Functions'''

def download(name, url):
    func_start = time.time()
    filename = os.path.join(download_dir,name)
    pousResponse = urllib.request.urlopen(url)
    pousData = json.loads(pousResponse.read())
    theJSON = json.dumps(pousData)
    f = open(f'{filename}.geojson', "w")
    f.write(str(theJSON))
    f.close()
    func_elapsed = time.time() - func_start
    func_elapsed_print = time.strftime("%H:%M:%S", time.gmtime(func_elapsed))
    print(f"\nDownloaded: {name}, Time Elapsed: {func_elapsed_print}")
    
''' Function Parameters '''
rmsseg_url = "https://opendata.arcgis.com/datasets/d9a2a5df74cf4726980e5e276d51fe8d_0.geojson"
rmsseg_name = "RMSSEG"

localroad_url = "https://opendata.arcgis.com/datasets/51d7bdaccf344502ae549acf9ce6f08b_0.geojson"
localroad_name = "PADOT_LOCAL_ROAD"

rmsintersection_url = "https://opendata.arcgis.com/datasets/9a6e1b6cdd784cbbbad4edc88ea62046_0.geojson"
rmsintersection_name = "RMSINTERSECTION"

''' Function Calls'''
print("Downloading files....")
download(rmsseg_name, rmsseg_url)
download(localroad_name, localroad_url)
download(rmsintersection_name, rmsintersection_url)

''' Final Time Stamp'''
elapsed_time = time.time() - execute_time
print("\nTime to execute program: ", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))




