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

    logger.info(f"Adding {len(data)} {popup_field} points to the map")
    for _, row in data.iterrows():
        # Retrieve the popup content if specified and available
        popup_text = row[popup_field] if popup_field and popup_field in row else None
        folium.Marker([row.geometry.y, row.geometry.x], popup=popup_text).add_to(
            crime_map
        )

    if save_path is None:
        logger.debug("save_path not provided. Defaulting to 'crime_map.html'")
        save_path = (
            config.get_proj_root()
            / config["paths"]["visualizations"]
            / "crime_map.html"
        )

    # Save map to HTML
    crime_map.save(save_path)
    logger.info(f"Map saved at {save_path}")

    open_file(save_path)

    return crime_map


def join_data(
    left: gpd.GeoDataFrame,
    right: gpd.GeoDataFrame,
    left_key: str,
    right_key: str,
    how: str = "left",
) -> gpd.GeoDataFrame:
    """
    Join two GeoDataFrames based on a common key.

    Parameters:
    left (GeoDataFrame): The left GeoDataFrame to join.
    right (GeoDataFrame): The right GeoDataFrame to join.
    left_key (str): The column name to join on in the left GeoDataFrame.
    right_key (str): The column name to join on in the right GeoDataFrame.
    how (str): The type of join to perform. Default is 'left'.

    Returns:
    GeoDataFrame: A GeoDataFrame with the joined data.
    """
    logger.info(f"Joining data on {left_key} with {right_key} using {how} join")
    joined = left.merge(right, how=how, left_on=left_key, right_on=right_key)

    if len(joined) == 0:
        logger.error(
            f"No data was joined. Check that the keys {left_key} and {right_key} are correct."
        )

    return joined

# NOTE: This approach works well for moderately sized datasets but could become slow for very large ones. For large datasets, spatial indexing or more advanced spatial joins might be needed (e.g., using scipy’s cKDTree for faster nearest-neighbor searches).
def distance_join(
    main_gdf, ref_gdf, ref_col_name="nearest_id", distance_col_name="distance_to"
):
    """
    Adds a column to the main GeoDataFrame with the ID of the nearest feature
    from the reference GeoDataFrame.

    Parameters:
    main_gdf (GeoDataFrame): The main GeoDataFrame, typically with Point geometries (e.g., arrests data).
    ref_gdf (GeoDataFrame): The reference GeoDataFrame to find the nearest feature from (e.g., sidewalks).
    ref_col (str): The name of the new column in main_gdf to store the ID of the nearest feature.
    distance_col (str, optional): If provided, stores the distance to the nearest feature in this column.

    Returns:
    GeoDataFrame: The main GeoDataFrame with an added column for the nearest feature's ID.
    """
    # Ensure both GeoDataFrames are in the same CRS, convert to a metric CRS for distance calculation
    metric_crs = "EPSG:3857"
    main_gdf = main_gdf.to_crs(metric_crs)
    ref_gdf = ref_gdf.to_crs(metric_crs)

    # Prepare the new columns in main_gdf
    main_gdf[ref_col_name] = None
    if distance_col_name:
        main_gdf[distance_col_name] = None

    # For each geometry in main_gdf, find the closest geometry in ref_gdf
    for idx, main_geom in main_gdf.iterrows():
        # Find the nearest geometry in ref_gdf
        nearest_geom = ref_gdf.geometry.distance(main_geom.geometry).idxmin()

        # Add the ID of the nearest geometry (index) to the main_gdf
        main_gdf.at[idx, ref_col_name] = ref_gdf.at[
            nearest_geom, "OBJECTID"
        ]  # or another ID column in ref_gdf

        # Optionally, store the distance to the nearest feature
        if distance_col_name:
            distance = main_geom.geometry.distance(ref_gdf.at[nearest_geom, "geometry"])
            main_gdf.at[idx, distance_col_name] = distance

    # Reproject main_gdf back to the original CRS
    main_gdf = main_gdf.to_crs(ref_gdf.crs)

    return main_gdf
