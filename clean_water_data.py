# function that cleans up data files from https://waterdata.usgs.gov/

import pandas as pd
import os
import csv
import re

def clean_water_data (file):
    # notebook_path = os.path.abspath(file)
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in '%s': %s" % (cwd, files))

    fhand = open(file, 'r')
    count=0
    _list = []

# Skips comments from the file
    for text in fhand:
        if not text.startswith("#"):
            count +=1
            _list.append(text)


# Skips more header information and then cleans up the tab delimited data.
# Nan values are in the form '-', this changes them to '0'
    count =2
    dict_w = {}
    for row in _list[2:]:
        dict_w[count] = re.findall('(.*?)s*[\t]', _list[count])
        item_ = []

        for item in dict_w[count]:
            item = item.replace('-', '0')
            item_.append(item)

        dict_w[count] = item_
        count += 1

    x = count - 1
    entry_length = len(dict_w[x])
    for item in dict_w.values():
        if len(item) != entry_length:
            print("ERROR --> NOT ENOUGH ENTRIES ")

    return(dict_w, len(dict_w))


# This code takes a dictionary and makes it a pandas data frame
# It also writes a copy in csv form

def make_water_df (w_dict, name):
    df= pd.DataFrame(data = w_dict)
    df = df.transpose().reset_index()
    # this assumes that dictionary headers are in the first row
    df = df.rename(columns=df.iloc[0])
    # this drops any old indexes from the index reset_index
    # df.drop(columns=['index'], inplace=True)
    df = df[1:]
    df.to_csv(name+ '.csv')
    return df


## This code tests that the dictionary was made
water_dict = None
y = None

while True:
    file_to_use= input("Enter water data filename: ")
    if len(file_to_use) < 1: break
    water_dict = None
    y = None
    water_dict, y = clean_water_data(file_to_use)
    print(y)
    file_save_as= input("Enter CSV filename: ")
    test_df = make_water_df(water_dict, file_save_as)
    print(test_df.head())
