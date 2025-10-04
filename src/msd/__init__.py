"""MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes.

This package provides tools for working with the Modified Swiss Dwellings (MSD) dataset,
a large-scale floor plan dataset containing layouts of multi-apartment dwellings.
"""

__version__ = "0.1.0"

# Import main constants
from msd.constants import (
    ZONING_MAPPING,
    ROOM_MAPPING,
    ZONING_NAMES,
    ROOM_NAMES,
    ZONING_ROOMS,
    COLORS_ZONING,
    COLOR_MAP_ZONING,
    CMAP_ZONING,
    COLORS_ROOMTYPE,
    COLOR_MAP_ROOMTYPE,
    CMAP_ROOMTYPE,
)

# Import graph utilities
from msd.graphs import (
    polygon_to_list,
    polygon_to_array,
    extract_access_graph,
    get_geometries_from_id,
)

# Import utility functions
from msd.utils import (
    save_pickle,
    load_pickle,
    colorize_floorplan,
    find_floor_boundary,
)

# Import plotting functions
from msd.plot import (
    set_figure,
    plot_polygon,
    plot_shapes,
    plot_graph,
    plot_floor,
)

__all__ = [
    # Constants
    "ZONING_MAPPING",
    "ROOM_MAPPING",
    "ZONING_NAMES",
    "ROOM_NAMES",
    "ZONING_ROOMS",
    "COLORS_ZONING",
    "COLOR_MAP_ZONING",
    "CMAP_ZONING",
    "COLORS_ROOMTYPE",
    "COLOR_MAP_ROOMTYPE",
    "CMAP_ROOMTYPE",
    # Graph utilities
    "polygon_to_list",
    "polygon_to_array",
    "extract_access_graph",
    "get_geometries_from_id",
    # Utility functions
    "save_pickle",
    "load_pickle",
    "colorize_floorplan",
    "find_floor_boundary",
    # Plotting functions
    "set_figure",
    "plot_polygon",
    "plot_shapes",
    "plot_graph",
    "plot_floor",
]
