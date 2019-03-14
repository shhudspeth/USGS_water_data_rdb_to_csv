# USGS_water_data_rdb_to_csv
A project that takes rdb data from USGS's website https://waterdata.usgs.gov/ and converts it to csv.


Included in this repo are jupyter notebooks that are used to  explore the data and set up the process to 
convert the rdb data to csv (and any future additional analyses). Also included is a python script to run that takes a name of already downloaded water use rdb file and converts it to csv as well. 

There are rdb files as samples (downloaded state data is renamed california_rdb and often the direct download is water_use_2) as well as the converted csv files (usually renamed _state_.csv) . 

More information about the data can be found at https://water.usgs.gov/watuse/WU-Category-Changes.html. The website knows that 
their data is in outdated formats and they are working on updating it. This program is intended to address the need
to put the file in a more updated format. 
