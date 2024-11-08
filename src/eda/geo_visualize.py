import folium
import geopandas as gpd
from shapely.geometry import box

from utils.config import Config
from utils.log import Logger
from utils.files import open_file

config = Config()
logger = Logger(__name__, config["log_level"])()


def filter_by_bounds(data: gpd.GeoDataFrame, bounds: tuple) -> gpd.GeoDataFrame:
    """
    Filters the GeoDataFrame to include only points within the specified bounds.

    Parameters:
    data (GeoDataFrame): The data to filter.
    bounds (tuple): A tuple (minx, miny, maxx, maxy) defining the bounding box.

    Returns:
    GeoDataFrame: Filtered GeoDataFrame with points within the bounds.
    """
    logger.debug(f"Filtering data by bounds: {bounds}")
    bbox = box(*bounds)

    if len(data) == 0:
        logger.error("No data found in the input GeoDataFrame. Check the input data.")
        return data

    # Filter data by checking if geometry is within the bounding box
    before_length = len(data)
    filtered = data[data.geometry.within(bbox)]
    logger.info(f"Filtered out {before_length - len(filtered)} rows outside the bounds")

    if len(data) == len(filtered):
        logger.warning("All data is within the specified bounds. No data was filtered.")

    if len(filtered) == 0:
        logger.error(
            f"All data was filtered out. Check that the bounds {bounds} are correct."
        )

    return filtered


def create_map(
    data: gpd.GeoDataFrame,
    location=config["tucson_center_coordinates"],
    zoom_start=12,
    popup_field=None,
    save_path=None,
):
    """
    Create a folium map with markers for each point in the input GeoDataFrame.

    Parameters:
    data (GeoDataFrame): The data to plot, must contain 'geometry' column.
    location (list): Latitude and longitude to center the map on. Default is Tucson, AZ.
    zoom_start (int): Initial zoom level for the map.
    popup_field (str, optional): Column name to use for the marker popups. If None, no popups.
    save_path (str or Path, optional): Path to save the generated map HTML file. If None, defaults to 'crime_map.html'.

    Returns:
    folium.Map: A map with a marker for each point in data.
    """
    logger.info(f"Creating map centered at {location} with zoom level {zoom_start}...")
    crime_map = folium.Map(location=location, zoom_start=zoom_start)

    logger.debug("Filtering out rows with missing or non-Point geometry")
    data = data[data.geometry.notnull() & (data.geometry.type == "Point")]

    logger.info(f"Adding {len(data)} points to the map")
    for _, row in data.iterrows():
        # Retrieve the popup content if specified and available
        popup_text = row[popup_field] if popup_field and popup_field in row else None
        folium.Marker([row.geometry.y, row.geometry.x], popup=popup_text).add_to(
            crime_map
        )

    if save_path is None:
        logger.debug("save_path not provided. Defaulting to 'crime_map.html'")
        save_path = "crime_map.html"

    # Save map to HTML
    crime_map.save(save_path)
    logger.info(f"Map saved at {save_path}")

    open_file(save_path)

    return crime_map
