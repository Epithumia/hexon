from enum import Enum


class map_types(str, Enum):
    rect = "rect"
    hex = "hex"


class orientation_types(str, Enum):
    pointy = "pointy"
    flat = "flat"
