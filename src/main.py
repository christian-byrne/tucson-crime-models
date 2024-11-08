import geopandas as gpd
import glob

import eda.geo_visualize as geo_viz

from utils.config import Config
from utils.log import Logger
from utils.files import open_file


config = Config()
logger = Logger(__name__, "DEBUG")()


def get_filepath(glob_str: str):
    file = glob.glob(str(config.get_proj_root() / glob_str))

    if not file:
        logger.error(f"No file found with glob string: {glob_str}")
        return None

    return str(config.get_proj_root() / file[0])


def load_dataset(glob_str: str):
    filepath = get_filepath(glob_str)
    dataframe = gpd.read_file(filepath)
    logger.info(f"Loaded data from {filepath}")
    logger.debug(
        f"Columns in {filepath.split('/')[-1]}:\n{', '.join(dataframe.columns)}"
    )
    return dataframe


# Load arrests data
arrests_data = load_dataset("data/crime/*Arrests*2017*")

# Remove rows with missing geometry (bad data)
arrests_data = arrests_data[arrests_data.geometry.notnull()]

# Restrict to just Tucson for quick testing/debugging
arrests_data = geo_viz.filter_by_bounds(arrests_data, config["tucson_bounds"])

# Truncate data for quick testing/debugging
arrests_data = arrests_data.head(300)

# Load sidewalks data
sidewalks_data = load_dataset("data/infra*/*Sidewalks*")

# Join Data: add columns in arrests data corresponding to nearest sidewalk ID and distance to that sidewalk
arrests_data = geo_viz.distance_join(
    arrests_data,
    sidewalks_data,
    ref_col_name="nearest_sidewalk_id",
    distance_col_name="distance_to_nearest_sidewalk",
)

# Analyze correlation between distance to nearest sidewalk and arrest charge
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(arrests_data['distance_to_nearest_sidewalk'], kde=True, bins=30)
plt.xlabel('Distance to Nearest Sidewalk (meters)')
plt.ylabel('Frequency')
plt.title('Distribution of Distance to Nearest Sidewalk for Crime Incidents')
plt.show()


# # Create a map with popups for each charge description
# geo_viz.create_map(arrests_data, popup_field="ArrestChargeandDescription")
