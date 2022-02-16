#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
@description: Convert an Excel sheet to GeoJSON
"""

# Import packages
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame as gdf

# Load the excel sheet as a pandas data frame
excel_data_df = pd.read_excel('../data/file.xlsx') # Your path and file name here

# Convert the pandas data frame into a geopandas data frame 
# Your excel sheet must have columns called "longitude and latitude"
gdf = gpd.GeoDataFrame(
    excel_data_df, geometry=gpd.points_from_xy(excel_data_df.longitude, excel_data_df.latitude))

# Set a CRS for the geopandas data frame
gdf = gdf.set_crs('epsg:4326')

# Set a file name
filename = "file"

# Insert the filename into the path 
url = '../data/{}.geojson'.format(filename)

# Convert the geopandas data frame into a geojson file
gdf.to_file(url, driver='GeoJSON')
