#!/usr/bin/env python
# coding: utf-8

#download geojson to file on your computer
# Copyright 2021 Tri County Regional Planning Commission

''' import modules / packages '''

import datetime
import json
import os
import urllib
import urllib.request

''' define functions '''

#creates initial timestamp and prints out message
def ts_start():
    global execute_time
    execute_time = datetime.datetime.now()
    print("Initiating Data Refresh \nCurrent time: ", execute_time, " \n")

#calculates elapsed time of entire program and prints that out
def ts_end():
    elapsed_time = datetime.datetime.now() - execute_time
    print("\nTime to execute program: ", elapsed_time)

#read in location from user to create directory
def file_locat():
    global path
    path = input("Please input the location you'd like to save your files.\n")
    print(f'You entered: {path}')

#creates a directory in the path specified before with a date appended to it
#if there is a folder with a matching date already specified,then it will append a timestamp to the end of the filename
def mk_dir():
    global download_dir
    date = datetime.datetime.now().strftime("%d_%b_%Y")
    timestamp = datetime.datetime.now().strftime("_%H-%M-%S")
    directory = "Data_Refresh_" + date
    try:
        download_dir = os.path.join(path, directory)
        os.mkdir(download_dir) 
    except:
        directory = ("Data_Refresh_" + date + timestamp)
        download_dir = os.path.join(path, directory)
        os.mkdir(download_dir)

#reads in filenames & geojson endpoint links into a series of nested dictionaries
def file_input():
    global file_dict
    n = int(input("How many files would you like to download?\n"))
    print("Numbers of files to read in:", n, "\n")
    #initializing blank dictionary
    file_dict = {}
    
    for i in range(n):
        dict_num = i
        dict_var = ("file" + str(dict_num))
        #initializing first nested dictionary
        file_dict[dict_var] = {}
        file_dict[dict_var]['name'] = input("enter FILENAME: ")
        file_dict[dict_var]['url'] = input("enter URL: ")

#takes the nested dictionary previously created and iterates through it
#assigns variables for fname and urlname in order to feed them to the snippet of code in the outer loop
def download():

    for subdict, subdict_val in file_dict.items():  
        for key in subdict_val:
            if key == "name":
                fname = subdict_val[key]
            elif key =="url":
                urlname = subdict_val[key]
            else:
                print("error occured when reading dictionary values")
            
        filename = os.path.join(download_dir,fname)
        pousResponse = urllib.request.urlopen(urlname)
        pousData = json.loads(pousResponse.read())
        theJSON = json.dumps(pousData)
        f = open(f'{filename}.geojson', "w")
        f.write(str(theJSON))
        f.close()
        print(f"\nDownloaded: {fname}\n")
    
''' defining main '''

def main():
    ts_start()
    file_locat()
    mk_dir()
    file_input()
    download()
    ts_end()

''' main execution '''

if __name__ == "__main__":
    main()