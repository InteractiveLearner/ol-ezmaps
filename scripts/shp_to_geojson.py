#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
@description: Convert a shapefile to GeoJSON
"""

# Import packages
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame as gdf

# Load the shapefile as a geopandas data frame
gdf = gpd.read_file("../data/file.shp") # Your path and file name here

# Set a CRS for the geopandas data frame
gdf = gdf.to_crs('epsg:4326')

# Set a file name
filename = "file"

# Insert the filename into the path 
url = '../data/{}.geojson'.format(filename)

gdf.to_file(url, driver='GeoJSON')