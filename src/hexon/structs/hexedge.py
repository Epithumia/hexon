from .coordinates import AxialCoord


class HexEdge:
    def __init__(self, coords: AxialCoord, direction: int):
        self.coords = coords
        self.direction = direction
        self.properties = dict()

    def __repr__(self) -> str:
        return f"HexEdge(coords={self.coords}, direction={self.direction}, properties={self.properties})"
