import geopandas as gpd

import src.eda.geo_visualize as geo_viz

from utils.config import Config
from utils.log import Logger
from utils.files import open_file


config = Config()
logger = Logger(__name__, config["log_level"])()

# Load shapefile or GeoJSON
crime_data = gpd.read_file("../data/arrests/Tucson_Police_Arrests_-_2021_-_Open_Data.geojson")  # Or use .geojson or .kml

# Display basic information and plot
# print(crime_data.head())
# crime_data.plot()

# ----------------------------------- clean ---------------------------------- #

# Remove rows with missing geometry
crime_data = crime_data[crime_data.geometry.notnull()]

# Restrict to just Tucson for faster rendering (optional)
crime_data = geo_viz.filter_by_bounds(crime_data, config["tucson_bounds"])

# Create a map with popups for each charge description
geo_viz.create_map(crime_data, popup_field='chrgdesc')

