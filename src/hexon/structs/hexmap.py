from pathlib import Path
from .hexagon import Hexagon
from .coordinates import AxialCoord, Point, axial_ring
from . import orientation_types


def find_offset(hex: Hexagon, size: int) -> Point:
    """
    Finds the offset for a given hexagon, which is the point
    that should be subtracted from all points in the hexagon
    to get the actual position of the hexagon on the screen.

    Parameters:
        hex: The hexagon to find the offset for.
        size: The size of the hexagon.

    Returns:
        The offset for the given hexagon.
    """
    if hex.orientation == orientation_types.pointy:
        offset = Point(
            hex.hex_corner(size, 4).x,
            hex.hex_corner(size, 5).y,
        )
    else:
        offset = Point(
            hex.hex_corner(size, 3).x,
            hex.hex_corner(size, 4).y,
        )
    return offset


class HexMap:
    """
    Base Map class.
    """

    def __init__(
        self, hex_size: int, orientation: orientation_types, seed: int
    ) -> None:
        """
        Initializes a HexMap object.

        Parameters:
            hex_size: The size of each hexagon.
            orientation: The orientation of the hexagons.
            seed: The seed for the random number generator.
        """
        self.hexagons = {}
        self.hex_size = hex_size
        self.orientation = orientation
        self.seed = seed


class RectHexMap(HexMap):
    """
    Rectangular HexMap.
    """

    def __init__(
        self,
        width: int,
        height: int,
        hex_size: int,
        orientation: orientation_types = orientation_types.pointy,
        seed: int = 0,
    ):
        """
        Creates a hex map with the given width and height, with hexagons of the given size and orientation.
        The hex map is seeded with the given seed.

        Parameters:
            width: The width of the hex map.
            height: The height of the hex map.
            hex_size: The size of each hexagon.
            orientation: The orientation of the hexagons.
            seed: The seed for the random number generator.
        """
        super().__init__(hex_size, orientation, seed)
        self.width = width
        self.height = height

        origin = Hexagon(AxialCoord(0, 0), hex_size, orientation)

        self.top_left = find_offset(origin, hex_size)

        self.origin = Hexagon(AxialCoord(0, 0), hex_size, orientation, self.top_left)

        self.hexagons[self.origin.coords] = self.origin

        if orientation == orientation_types.pointy:
            for h in range(height):
                q = -(h // 2)
                for w in range(width):
                    node = Hexagon(
                        AxialCoord(q + w, h), hex_size, orientation, self.top_left
                    )
                    self.hexagons[node.coords] = node
        else:
            for h in range(height):
                for w in range(width):
                    node = Hexagon(
                        AxialCoord(w, h - (w // 2)),
                        hex_size,
                        orientation,
                        self.top_left,
                    )
                    self.hexagons[node.coords] = node

    def __repr__(self) -> str:
        ordered_hexagons = []
        if self.orientation == orientation_types.pointy:
            for h in range(self.height):
                q = -(h // 2)
                for w in range(self.width):
                    ordered_hexagons.append(self.hexagons[AxialCoord(q + w, h)])
        else:
            for h in range(self.height):
                for w in range(self.width):
                    ordered_hexagons.append(self.hexagons[AxialCoord(w, h - (w // 2))])
        return f"RectHexMap(width={self.width}, height={self.height}, hex_size={self.hex_size}, orientation={self.orientation}, hexagons={ordered_hexagons})"

    def draw(self, path: Path):
        """
        Draws the hex map as a PNG image and saves it to the given path.

        Parameters:
            path: The path where the image should be saved.
        """
        from PIL import Image, ImageDraw
        from math import sqrt, ceil

        if self.orientation == orientation_types.pointy:
            im_height = (
                ceil(self.hex_size * 2 + (self.height - 1) * self.hex_size * 3 / 2) + 1
            )
            if self.height == 1:
                im_width = ceil(sqrt(3) * self.width * self.hex_size) + 1
            else:
                im_width = (
                    ceil(
                        sqrt(3) / 2 * self.hex_size
                        + sqrt(3) * (self.width) * self.hex_size
                    )
                    + 1
                )
        else:
            if self.width == 1:
                im_height = ceil(sqrt(3) * self.height * self.hex_size) + 1
            else:
                im_height = (
                    ceil(
                        sqrt(3) / 2 * self.hex_size
                        + sqrt(3) * (self.height) * self.hex_size
                    )
                    + 1
                )
            im_width = (
                ceil(self.hex_size * 2 + (self.width - 1) * self.hex_size * 3 / 2) + 1
            )

        im = Image.new("RGBA", (im_width, im_height))

        draw = ImageDraw.Draw(im)

        for hex in self.hexagons.values():
            hex.draw(draw)

        im.save(path)


class CircularHexMap(HexMap):
    """
    Circular (hexagonal) HexMap
    """

    def __init__(
        self,
        radius: int,
        hex_size: int,
        orientation: orientation_types = orientation_types.pointy,
        seed: int = 0,
    ):
        """
        Creates a circular hex map with the given radius, with hexagons of the given size and orientation.
        The hex map is seeded with the given seed.

        Parameters:
            radius: The radius of the circular hex map.
            hex_size: The size of each hexagon.
            orientation: The orientation of the hexagons.
            seed: The seed for the random number generator.
        """
        super().__init__(hex_size, orientation, seed)
        self.radius = radius
        self.center = Hexagon(AxialCoord(0, 0), hex_size, orientation)

        offset = find_offset(self.center, hex_size)

        self.hexagons[self.center.coords] = self.center
        for r in range(1, radius + 1):
            ring = axial_ring(AxialCoord(0, 0), r)
            for hex in ring:
                self.hexagons[hex] = Hexagon(hex, hex_size, self.orientation)
                h_offset = find_offset(self.hexagons[hex], hex_size)
                offset = Point(min(offset.x, h_offset.x), min(offset.y, h_offset.y))

        for hex in self.hexagons.values():
            hex.offset = offset

    def __repr__(self) -> str:
        ordered_hexagons = []
        for r in range(self.radius + 1):
            ring = axial_ring(self.center.coords, r)
            for hex in ring:
                ordered_hexagons.append(self.hexagons[hex])
        return f"CircularHexMap(radius={self.radius}, hex_size={self.hex_size}, orientation={self.orientation}, hexagons={ordered_hexagons})"

    def draw(self, path: Path):
        """
        Draws the hex map as a PNG image and saves it to the given path.

        Parameters:
            path: The path where the image should be saved.
        """
        from PIL import Image, ImageDraw
        from math import sqrt, ceil

        height = 2 * self.radius + 1
        width = 2 * self.radius + 1

        if self.orientation == orientation_types.pointy:
            im_height = (
                ceil(self.hex_size * 2 + (height - 1) * self.hex_size * 3 / 2) + 1
            )
            im_width = ceil(sqrt(3) * (width) * self.hex_size) + 1
        else:
            im_width = (
                ceil(self.hex_size * 2 + (height - 1) * self.hex_size * 3 / 2) + 1
            )
            im_height = ceil(sqrt(3) * (width) * self.hex_size) + 1

        im = Image.new("RGBA", (im_width, im_height))

        draw = ImageDraw.Draw(im)

        for hex in self.hexagons.values():
            hex.draw(draw)

        im.save(path)
