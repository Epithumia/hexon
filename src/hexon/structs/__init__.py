from enum import Enum


class map_types(str, Enum):
    """
    Possible values:

    - `rect`: Rectangular map
    - `hex`: Hexagonal/Circular map
    """
    rect = "rect"
    hex = "hex"


class orientation_types(str, Enum):
    """
    Possible values:
    
    - `pointy`: Pointy top hexagons
    - `flat`: Flat top hexagons
    """
    pointy = "pointy"
    flat = "flat"
