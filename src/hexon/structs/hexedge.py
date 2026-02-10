from .coordinates import AxialCoord


class HexEdge:
    """
    Edge of an Hexagon
    """
    def __init__(self, coords: AxialCoord, direction: int):
        """
        Initializes a HexEdge with the given coordinates and direction.

        Parameters:
            coords: The axial coordinates of the hexagon the edge is part of.
            direction: The direction of the edge, with 0 being the top-right corner and increasing clockwise.
        """
        self.coords = coords
        self.direction = direction
        self.properties = dict()

    def __repr__(self) -> str:
        return f"HexEdge(coords={self.coords}, direction={self.direction}, properties={self.properties})"
